import re
import emoji
from typing import Final, Dict, List


REGEX_PATTERN: Final[Dict[str, re.Pattern]] = {
    "comment": re.compile(r"<!--.*-->"),
    "header": re.compile(r"^#+\s+"),
    # Config
    "lang_tags": re.compile(r"(<!-- multilingual suffix:)\s*([\w\s,-]+)(?=\s--)"),
    "no_suffix": re.compile(r"<!-- no suffix:\s*([\w-]+)"),
    # Command
    "tag": re.compile(r"<!--\s*\[\s*([\w-]+)\s*\]\s*-->"),
    # Table of Contents
    "auto_toc": re.compile(r"<!--\s*\[\[\s*multilingual toc:[^\]]*\s*]]\s*-->"),
    "toc_level": re.compile(r"level\s*=\s*([1-9]\s*~\s*[1-9]|~\s*[1-9]+|[1-9]+\s*~?)"),
    "toc_no_emoji": re.compile("no-emoji"),
    # Code block (backtick)
    "inline_code": re.compile(r"`+"),
    "cb_begin": re.compile(r"^[ \t]*```[`]*[\w]*$"),
    "cb_end": re.compile(r"^[ \t]*```[`]*$"),
    "cb_backtick_only": re.compile(r"^[ \t]*```[`]*"),
}


def remove_emoji(text: str) -> str:
    """
    Remove all emojis from a given string.
    """
    # return emoji.get_emoji_regexp().sub(r"", text)  # Deprecated in emoji 2.0.0
    return emoji.replace_emoji(text, replace='')


def remove_links(text: str) -> str:
    """
    Remove all links from a given string.
    """
    # remove: html style
    tag_begin = r"(<a href=)(.(?<!<))+>"
    tag_end = r"<\/a>"
    text = re.sub(tag_begin, "", re.sub(tag_end, "", text))
    # remove: markdown style
    mdurl_pattern = r"\[(?P<TEXT>((?!\]\(.*\]\().)*)\]\(((?!\).*\)).)*\)"
    text = re.sub(mdurl_pattern, lambda m: m.group("TEXT"), text)
    return text


def get_size_of_code_block_backtick(line: str) -> int:
    """Get the size of the backtick of a code block.

    Args:
        line (str): The line to check.

    Returns:
        int: The size of the backtick. If the line is not a code block, return 0.
    """
    match_found = REGEX_PATTERN["cb_backtick_only"].match(line.lstrip())
    if match_found:
        return match_found.span()[1]
    return 0


def get_indentation_level(line: str) -> int:
    """Get the size of the indentation of a line.

    Args:
        line (str): The line to check.

    Returns:
        int: The level of indentation. If the line is not indented, return 0.
    """
    # Convert tabs to spaces (4 spaces)
    tmp = line.replace("\t", "    ")
    # Count the number of spaces at the beginning of the line
    space = len(tmp) - len(tmp.lstrip())
    return space // 4


def flag_code_block_lines(doc: List[str]) -> List[bool]:
    """
    Parse the markdwon string and find all code blocks.
    Marked lines will be skipped when parsing the MMG tags.

    Args:
        doc (List[str]): The markdown string to parse.

    Returns:
        List[bool]: A list of booleans indicating whether the line is in a code block.
            (True: in a code block, False: not in a code block)
    """
    result = [False for _ in doc]

    # First, mark all code blocks (not inline, more than 3 backticks).
    last_backtick_size: int = 0  # >= 3
    cb_indent: int = 0
    for i, line in enumerate(doc):
        indent: int = get_indentation_level(line)

        # Previous line is not in a code block
        if last_backtick_size < 3:
            last_backtick_size = get_size_of_code_block_backtick(line)
            if last_backtick_size > 2:
                result[i] = True
                cb_indent = indent
            continue
        # Previous line is in a code block (when line is not empty)
        if (cb_indent > indent) and (line.strip() != ""):
            last_backtick_size = 0
        else:
            result[i] = True
            if (
                cb_indent == indent
                and REGEX_PATTERN["cb_end"].match(line)
                and last_backtick_size <= get_size_of_code_block_backtick(line)
            ):
                last_backtick_size = 0

    # Second, mark all inline code(`, ``, ```) except for the code blocks.
    current_backtick: str = None
    start_line: int = None
    for i, line in enumerate(doc):
        # If the line is in a code block, skip and reset the current backtick.
        if result[i]:
            current_backtick = None
            continue
        # If the line is empty, skip and reset the current backtick.
        # The previous backtick will be treated as a normal character.
        if line.strip() == "":
            current_backtick = None
            continue
        # If the line is not in a code block, check if the line contains inline code.
        # If the line contains inline code, mark the line as True.
        for backtick in REGEX_PATTERN["inline_code"].findall(line):
            if current_backtick is None:
                current_backtick = backtick
                start_line = i
            elif current_backtick == backtick:
                current_backtick = None
                for j in range(start_line, i + 1):
                    result[j] = True
    return result
