import re
import emoji


def remove_emoji(text: str) -> str:
    """
    Remove all emojis from a given string.
    """
    return emoji.get_emoji_regexp().sub(r'', text)


def remove_links(text: str) -> str:
    # remove: html style
    tag_begin = r"(<a href=)(.(?<!<))+>"
    tag_end = r"<\/a>"
    text = re.sub(tag_begin, "", re.sub(tag_end, "", text))
    # remove: markdown style
    mdurl_pattern = r"\[(?P<TEXT>((?!\]\(.*\]\().)*)\]\(((?!\).*\)).)*\)"
    text = re.sub(mdurl_pattern, lambda m: m.group("TEXT"), text)
    return text
