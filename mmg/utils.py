import re
import emoji
from typing import List


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


def is_command_tag(line: str) -> bool:
    """
    Check if the line is a command tag.
    Command tag pattern for `mmg`: <!-- [oo] -->

    Args:
        line (str): The line to check.

    Returns:
        bool: True if the line is a command tag.
    """
    _command_tag_regex = re.compile(r"[ \t]*<!-- \[\w+(\-\w+)*\] -->")
    return _command_tag_regex.match(line) is not None


class CodeBlockTracker:
    regex_inline = re.compile(r"`+")
    regex_block_start = re.compile(r"^```[\w]*$")
    regex_block_end = re.compile(r"^```$")

    def __init__(self) -> None:
        self.result = []

    def parse(self, doc: List[str]) -> None:
        """
        Parse the markdwon string and find all code blocks.

        Args:
            doc (List[str]): The markdown string to parse.
        """
        self.result = [False for _ in doc]

        # First, mark all code blocks with three backticks(```).
        is_code_block = False
        for i, line in enumerate(doc):
            if is_code_block:
                self.result[i] = True
                if self.regex_block_end.match(line):
                    is_code_block = False
            elif self.regex_block_start.match(line):
                is_code_block = True
                self.result[i] = True

        # Second, mark all inline code(`, ``, ```) except for the code blocks.
        current_backtick: str = None
        start_line: int = None
        for i, line in enumerate(doc):
            # If the line is in a code block, skip and reset the current backtick.
            if self.result[i]:
                current_backtick = None
                continue
            # If the line is empty, skip and reset the current backtick.
            # The previous backtick will be treated as a normal character.
            if line.strip() == "":
                current_backtick = None
                continue
            # If the line is not in a code block, check if the line contains inline code.
            for backtick in self.regex_inline.findall(line):
                if current_backtick is None:
                    current_backtick = backtick
                    start_line = i
                elif current_backtick == backtick:
                    current_backtick = None
                    for j in range(start_line, i + 1):
                        self.result[j] = True

    def result(self) -> List[bool]:
        """
        Get the result of the code block check.

        Returns:
            List[bool]: A list of booleans indicating whether the line is in a code block.
        """
        return self.result
