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
    "auto_toc": re.compile(r"<!-- \[\[ multilingual toc:[ \w=~-]+\]\] -->"),
    "toc_level": re.compile(r"level\s*=\s*([1-9]\s*~\s*[1-9]|~\s*[1-9]+|[1-9]+\s*~?)"),
    "toc_no_emoji": re.compile("no-emoji"),

    # Code block
    "inline_code": re.compile(r"`+"),
    "code_block_start": re.compile(r"^```[\w]*$"),
    "code_block_end": re.compile(r"^```$"),
}


def remove_emoji(text: str) -> str:
    """
    Remove all emojis from a given string.
    """
    return emoji.get_emoji_regexp().sub(r"", text)


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


def flag_code_block_lines(doc: List[str]) -> List[bool]:
    """ Parse the markdwon string and find all code blocks.

    Args:
        doc (List[str]): The markdown string to parse.

    Returns:
        List[bool]: A list of booleans indicating whether the line is in a code block.
    """
    result = [False for _ in doc]

    # First, mark all code blocks with three backticks(```).
    is_code_block = False
    for i, line in enumerate(doc):
        if is_code_block:
            result[i] = True
            if REGEX_PATTERN["code_block_end"].match(line):
                is_code_block = False
        elif REGEX_PATTERN["code_block_start"].match(line):
            is_code_block = True
            result[i] = True

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
        for backtick in REGEX_PATTERN["inline_code"].findall(line):
            if current_backtick is None:
                current_backtick = backtick
                start_line = i
            elif current_backtick == backtick:
                current_backtick = None
                for j in range(start_line, i + 1):
                    result[j] = True
    return result
