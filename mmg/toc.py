import unicodedata
from typing import Dict, Final, List, NamedTuple, Tuple
from urllib.parse import quote
from mmg.utils import REGEX_PATTERN, flag_code_block_lines, remove_emoji, remove_links
from mmg.exceptions import BadConfigError


# Heading anchors are not standardized: every renderer derives its own heading IDs.
#   - "github": lowercased, punctuation stripped, a repeated ID suffixed with -1, -2 ...
#     Correct on GitHub for both .md and .ipynb. Verified against `github-slugger`.
#   - "jupyter": case, punctuation and emojis preserved, non-ASCII percent-encoded, and
#     a repeated ID left as a duplicate. Correct in Jupyter/nbconvert/Colab viewers.
#     Verified against `jupyter nbconvert --to html`.
# "github" stays the default because the overwhelming majority of MMG output is a
# GitHub README; changing the default would silently break those anchors. (Issue #36)
ANCHOR_STYLES: Final[Tuple[str, ...]] = ("github", "jupyter")
DEFAULT_ANCHOR_STYLE: Final[str] = "github"

# What JavaScript's `encodeURI()` leaves unescaped, minus "#" which Jupyter escapes too.
# Measured against nbconvert: "a/b?c&d" and "Hello, World!" survive verbatim, while
# "A # B" becomes "A-%23-B".
JUPYTER_SAFE_CHARS: Final[str] = ";,/?:@&=+$-_.!~*'()"


class TocOptions(NamedTuple):
    """Options parsed from a `multilingual toc` marker."""

    min_level: int
    max_level: int
    no_emoji: bool
    anchor: str = DEFAULT_ANCHOR_STYLE


def parse_toc_options(toc_line: str) -> TocOptions:
    """Parse the toc options.

    Args:
        toc_line (str): Example: `<!-- [[ multilingual toc: level=1~3, no-emoji ]] -->`

    Raises:
        BadConfigError: If the level option is not specified, if the level option is
            invalid, or if the anchor option is not a known style.

    Returns:
        TocOptions: (min_level, max_level, no_emoji, anchor)
    """
    # Level option
    level_option = REGEX_PATTERN["toc_level"].search(toc_line)
    if level_option is None:
        raise BadConfigError("You must specify the level option in the table of contents.")
    level_option = level_option.group(1).replace(" ", "")

    min_level = 1
    max_level = 9
    if len(level_option) == 1:  # "2" (is equivalent to "2~2")
        min_level = max_level = int(level_option)
    elif len(level_option) == 2:  # "2~" or "~3"
        if level_option[0] == "~":
            max_level = int(level_option[1])  # "~3"
        else:
            min_level = int(level_option[0])  # "2~"
    elif len(level_option) == 3:  # "2~3"
        s = level_option.split("~")
        min_level = int(s[0])
        max_level = int(s[1])
    else:
        raise BadConfigError(f"Cannnot parse the level option: {level_option}\nToC line: {toc_line}")

    # Emoji option
    no_emoji = True if REGEX_PATTERN["toc_no_emoji"].search(toc_line) else False

    # Anchor option
    anchor_option = REGEX_PATTERN["toc_anchor"].search(toc_line)
    anchor = anchor_option.group(1) if anchor_option else DEFAULT_ANCHOR_STYLE
    if anchor not in ANCHOR_STYLES:
        raise BadConfigError(
            f"Unknown anchor style: {anchor} (Should be one of {', '.join(ANCHOR_STYLES)}.)\nToC line: {toc_line}"
        )

    # Return
    return TocOptions(min_level, max_level, no_emoji, anchor)


def _slugify(header: str, anchor: str) -> str:
    """Convert a heading text into an anchor slug for the target renderer.

    Args:
        header (str): The heading text, without the leading `#` marks.
        anchor (str): The anchor style, one of `ANCHOR_STYLES`.

    Returns:
        str: The anchor slug, without the leading `#`.
    """
    header = header.strip()  # A markdown heading ignores the blanks around its text.
    if anchor == "jupyter":
        # Measured against nbconvert: every blank becomes a "-", and whatever
        # `encodeURI()` would escape is percent-encoded. Nothing is dropped -- an emoji
        # survives as its percent-encoded bytes, and repeated blanks each produce a "-".
        return quote(header.replace(" ", "-"), safe=JUPYTER_SAFE_CHARS)
    # Verified against `github-slugger`, the reference implementation of the GitHub
    # rules: lowercase, keep only letters, digits, marks, "_", "-" and blanks, then turn
    # each remaining blank into a "-". Everything else -- punctuation, emojis, dashes
    # such as an em dash, and control characters like a tab -- is dropped outright.
    # Note that a blank is never collapsed: "A  B" yields "a--b", not "a-b".
    kept = [char for char in header.lower() if char.isalnum() or char in "_- " or unicodedata.category(char).startswith("M")]
    return "".join(kept).replace(" ", "-")


def _heading_slugs(doc: List[str], codeblock: List[bool], anchor: str) -> Dict[int, str]:
    """Assign an anchor slug to every heading of `doc`, the way a renderer would.

    The slugs are resolved over the whole document rather than over the entries that
    end up in the table of contents, because a renderer gives an ID to every heading --
    including the ones this table of contents filters out by level.

    Args:
        doc (List[str]): The whole document.
        codeblock (List[bool]): The code block flags of `doc`.
        anchor (str): The anchor style, one of `ANCHOR_STYLES`.

    Returns:
        Dict[int, str]: The slug of each heading, keyed by its line number.
    """
    slugs: Dict[int, str] = {}
    occurrences: Dict[str, int] = {}
    for line_num, raw_line in enumerate(doc):
        if codeblock[line_num]:
            continue
        line = raw_line.rstrip("\r\n")
        header_match = REGEX_PATTERN["header"].match(line)
        if not header_match:
            continue
        slug = _slugify(remove_links(line[header_match.end() :]), anchor)
        if anchor == "github":
            # GitHub disambiguates a repeated ID by appending "-1", "-2" and so on,
            # retrying until the result is free. Jupyter does not: nbconvert emits the
            # same ID for every repetition, so the slug is left untouched there.
            original = slug
            while slug in occurrences:
                occurrences[original] += 1
                slug = f"{original}-{occurrences[original]}"
            occurrences[slug] = 0
        slugs[line_num] = slug
    return slugs


def create_toc(toc_options: TocOptions, doc: List[str]) -> List[str]:
    """Create a table of contents.

    Args:
        toc_options (TocOptions): (min_level, max_level, no_emoji, anchor).
            A plain 3-tuple is also accepted; `anchor` then falls back to the default.
        doc (List[str]): The markdown string to parse.

    Returns:
        List[str]: The table of contents. The lines carry no line ending.
    """
    codeblock = flag_code_block_lines(doc)
    min_level, max_level, no_emoji, anchor = TocOptions(*toc_options)
    suburls = _heading_slugs(doc, codeblock, anchor)

    # Parse all headers
    toc = []
    prev_level = min_level  # "0" means no header. (1: h1, 2: h2, ...)

    for line_num, raw_line in enumerate(doc):
        if codeblock[line_num]:
            continue
        # A Jupyter cell keeps the line ending inside `source`, while the markdown path
        # feeds `str.splitlines()` output. Drop it here so that it can never leak into
        # the link text or the anchor of a generated ToC entry.
        line = raw_line.rstrip("\r\n")
        header_match = REGEX_PATTERN["header"].match(line)
        if header_match:
            cur_level = len(header_match.group(1))

            # Check the level
            if cur_level < min_level:
                continue
            if cur_level > max_level:
                continue
            if cur_level > (prev_level + 1):  # e.g. h1 -> h3 (h2 is skipped)
                continue
            prev_level = cur_level

            # Get the header
            # > Slice off the leading marks only. Replacing them would also delete any
            # > later "# " of the same shape, e.g. "# A # B" would become "A B".
            header = line[header_match.end() :]
            header = remove_links(header)  # Fix the issue #4 (URL bug)
            # Get the suburl
            suburl = suburls[line_num]
            # No emoji
            if no_emoji:
                header = remove_emoji(header)
                header = header.strip()  # Remove the leading and trailing blanks
                header = header.replace("  ", " ")  # Remove the redundant blanks
            # Get the toc line
            space = "    " * (cur_level - min_level)
            toc_line = f"{space}1. [{header}](#{suburl})"
            toc.append(toc_line)
    return toc
