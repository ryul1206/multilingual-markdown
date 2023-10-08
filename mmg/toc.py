import re
from typing import Tuple, List
from mmg.utils import REGEX_PATTERN, flag_code_block_lines, remove_emoji, remove_links
from mmg.exceptions import BadConfigError


def parse_toc_options(toc_line: str) -> Tuple[int, int, bool]:
    """Parse the toc options.

    Args:
        toc_line (str): Example: `<!-- [[ multilingual toc: level=1~3, no-emoji ]] -->`

    Raises:
        BadConfigError: If the level option is not specified. or If the level option is invalid.

    Returns:
        Tuple[int, int, bool]: (min_level, max_level, no_emoji)
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

    # Return
    return (min_level, max_level, no_emoji)


def create_toc(toc_options: Tuple[int, int, bool], doc: List[str]) -> List[str]:
    """Create a table of contents.

    Args:
        toc_options (Tuple[int, int, bool]): (min_level, max_level, no_emoji)
        doc (List[str]): The markdown string to parse.

    Returns:
        List[str]: The table of contents.
    """
    codeblock = flag_code_block_lines(doc)
    min_level, max_level, no_emoji = toc_options

    # Parse all headers
    toc = []
    prev_level = min_level  # "0" means no header. (1: h1, 2: h2, ...)

    for line_num, line in enumerate(doc):
        if codeblock[line_num]:
            continue
        header_match = REGEX_PATTERN["header"].match(line)
        if header_match:
            header_mark = header_match.group(0)
            cur_level = len(header_mark) - 1

            # Check the level
            if cur_level < min_level:
                continue
            if cur_level > max_level:
                continue
            if cur_level > (prev_level + 1):  # e.g. h1 -> h3 (h2 is skipped)
                continue
            prev_level = cur_level

            # Get the header
            header = line.replace(header_mark, "")
            header = remove_links(header)  # Fix the issue #4 (URL bug)
            # Get the suburl
            special_char = r"[`~!@#$%\^&\*\(\)_=\+\|\[\]\{\}\\\\;:'\",./<>\?]+"
            suburl = re.sub(special_char, "", header)
            suburl = remove_emoji(suburl)
            suburl = suburl.replace("  ", " ").replace(" ", "-")
            suburl = suburl.lower()
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
