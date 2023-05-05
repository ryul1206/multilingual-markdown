import os.path
import re
import click
from collections import OrderedDict  # toc
from .utils import remove_emoji, remove_links


def create_toc(_dict, min_, max_, enable_emoji_header, _toc_str="", _level=1):
    for head, child in _dict.items():
        if (min_ <= _level) and (_level <= max_):
            # head
            if not enable_emoji_header:
                head = remove_emoji(head)
            # Fix the issue #4 (URL bug)
            head = remove_links(head)
            # suburl
            special_char = r"[`~!@#$%\^&\*\(\)_=\+\|\[\]\{\}\\\\;:'\",./<>\?]+"
            suburl = re.sub(special_char, "", head)
            suburl = remove_emoji(suburl)
            suburl = suburl.replace("  ", " ").replace(" ", "-")
            # toc line
            temp = f"1. [{head}](#{suburl})\n"
            # append
            _toc_str += "    " * (_level - min_)
            _toc_str += temp
        # recursive
        _toc_str = create_toc(
            child, min_, max_, enable_emoji_header, _toc_str, _level + 1
        )
    return _toc_str


class CreateMonolangualDoc(object):
    def __init__(self, path, file_name, lang, suffix=True):
        # Resolve a PowerShell bug related to file paths with specific names
        # `mmg` will throw an error when the file_name starts with ".\" or "./".
        if file_name.startswith(".\\") or file_name.startswith("./"):
            file_name = file_name[2:]
        fname, base, ename = file_name.split(".")

        self._this_name = fname + ("." + lang + "." if suffix else ".") + ename
        self.full_name = os.path.join(path, self._this_name)

        self.content = []

        self.toc = OrderedDict()
        self.header_re = re.compile("#+ ")
        self.toc_stack = []
        self.prev_level = 0

        self.success = False

    def __del__(self):
        if self.success:
            doc = open(self.full_name, "w", encoding="utf-8")
            self.__save(doc)
            doc.close()
        # if (not self.success) and (os.path.isfile(self.full_name)):
        #     os.remove(self.full_name)

    def __repr__(self):
        return self.full_name

    def __save(self, target_file):
        for line in self.content:
            if isinstance(line, tuple):  # toc
                min_, max_, enable_emoji_header = line
                target_file.write(create_toc(self.toc, min_, max_, enable_emoji_header))
            else:
                target_file.write(str(line))

    def CustomException(self, message):
        return click.ClickException(f"<{self._this_name}> {message}")

    def write(self, oneline, codeblock_mark):
        # write
        self.content.append(oneline)
        # check header
        if not codeblock_mark:
            result = self.header_re.match(oneline)
            if result:
                head = oneline[result.end():].replace("\n", "")
                self.append_toc(head, result.end() - 1)

    def append_toc(self, head, level):
        if (self.prev_level + 1) == level:  # new child
            pass
        elif self.prev_level == level:  # same level
            self.toc_stack = self.toc_stack[:-1]
        elif self.prev_level > level:  # new elem
            self.toc_stack = self.toc_stack[: (level - 1)]
        else:
            msg = "'Table of Contents' level mismatch. prev_level="
            msg += f"{self.prev_level}, current_level={level}\n"
            msg += f"\tCheck here => {head}"
            raise self.CustomException(msg)
        recursive = self.toc
        for x in self.toc_stack:
            recursive = recursive[x]
        recursive[head] = OrderedDict()
        self.toc_stack.append(head)
        self.prev_level = level

    def set_toc(self, _min=1, _max=9, enable_emoji_header=True):
        self.content.append((_min, _max, enable_emoji_header))
