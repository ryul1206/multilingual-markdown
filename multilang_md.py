#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import re
import click
import emoji
from collections import OrderedDict  # toc


def remove_emoji(text):
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "]+",
        flags=re.UNICODE,
    )
    return emoji_pattern.sub(r"", text)  # no emoji


def create_toc(_dict, min_, max_, enable_emoji_header, _toc_str="", _level=1):
    for head, child in _dict.items():
        if (min_ <= _level) and (_level <= max_):
            # head
            if not enable_emoji_header:
                head = remove_emoji(head)
            # suburl
            spc = r"[`~!@#$%\^&\*\(\)_=\+\|\[\]\{\}\\\\;:'\",./<>\?]+"
            suburl = re.sub(spc, "", head)
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
        self._base_file = file_name
        fname, base, ename = self._base_file.split(".")

        new_name = fname + ("." + lang + "." if suffix else ".") + ename
        self.full_name = os.path.join(path, new_name)

        self.doc = open(self.full_name, "w", encoding="utf-8")

        self.content = []

        self.toc = OrderedDict()
        self.header_re = re.compile("#+ ")
        self.toc_stack = []
        self.prev_level = 0

        self.success = False

    def __del__(self):
        if self.success:
            self.__save()
        self.doc.close()
        if (not self.success) and (os.path.isfile(self.full_name)):
            os.remove(self.full_name)

    def __repr__(self):
        return self.full_name

    def __save(self):
        for line in self.content:
            if isinstance(line, tuple):  # toc
                min_, max_, enable_emoji_header = line
                self.doc.write(create_toc(self.toc, min_, max_, enable_emoji_header))
            else:
                self.doc.write(str(line))

    def CustomException(self, message):
        return click.ClickException(f"<{self._base_file}> {message}")

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
            msg += f"{self.prev_level}, current_level={level}"
            raise self.CustomException(msg)
        recursive = self.toc
        for x in self.toc_stack:
            recursive = recursive[x]
        recursive[head] = OrderedDict()
        self.toc_stack.append(head)
        self.prev_level = level

    def set_toc(self, _min=1, _max=9, enable_emoji_header=True):
        self.content.append((_min, _max, enable_emoji_header))


class MultilangualDoc(object):
    class SafetyRead(object):
        def __init__(self, full_name):
            self.__doc = open(full_name, "r", encoding="utf-8")
            self.line_count = 0
            self.last_line = ""

        def __del__(self):
            self.__doc.close()

        def readline(self):
            self.line_count += 1
            self.last_line = self.__doc.readline()
            return self.last_line

    def __init__(self, path, file_name):
        self._base_file = file_name
        self.full_name = os.path.join(path, self._base_file)
        self.doc = self.SafetyRead(self.full_name)

        # Initialize configuration
        self.lang_read = {}
        self.lang_doc = {}
        self.no_suffix = ""
        self.pattern = re.compile(r"[ \t]*<!-- \[\w+\] -->")  # <!-- [oo] -->
        self.init_config(path, self._base_file)

        # Main converting
        self.converting()
        self.log()

    def CustomException(self, message):
        return click.ClickException(f"<{self._base_file}> {message}")

    def log(self):
        click.echo(self.full_name)
        for lang, md in self.lang_doc.items():
            click.echo(f"\t{lang}: {md}")

    def init_config(self, path, file_name):
        # re options
        options = [
            (
                re.compile(r"<!-- multilangual suffix:[ ]*([\w]+)(, [\w]+)*"),
                self.config_setlang,
            ),
            (re.compile(r"<!-- no suffix:[ ]*([\w]+)"), self.config_nosuffix),
        ]
        option_checked = [False for _ in options]
        # check base doc
        while True:
            for i in range(len(options)):
                # if detect some option
                if options[i][0].match(self.doc.last_line):
                    if option_checked[i]:
                        msg = f"Duplicate config: {self.doc.last_line}\n"
                        raise self.CustomException(msg)
                    else:
                        options[i][1](self.doc.last_line)
                        option_checked[i] = True
            # terminal conditions
            # 1. all options were setted
            if not (False in option_checked):
                break
            # 2. main doc start
            if self.pattern.match(self.doc.last_line):
                break
            # 3. base doc end
            if not self.doc.readline():
                break
        # create single doc
        for lang, _ in self.lang_read.items():
            self.lang_doc[lang] = CreateMonolangualDoc(
                path, file_name, lang, suffix=(lang != self.no_suffix)
            )

    def config_setlang(self, line):
        langs = line.replace(" ", "")[23:-4].split(",")
        protected_keywords = ["common", "ignore"]
        for x in langs:
            if x in protected_keywords:
                msg = "You cannot use [common] and [ignore] as a suffix."
                raise self.CustomException(msg)
            self.lang_read[x] = False

    def config_nosuffix(self, line):
        lang = line.replace(" ", "")[13:-4]
        self.no_suffix = lang

    def converting(self):
        # set the starting point
        while not self.pattern.match(self.doc.last_line):
            self.doc.readline()
        # converting
        signal = "common"
        codeblock_re = re.compile("`+")
        codeblock_mark = None
        toc_re = re.compile(r"<!-- \[\[ multilangual toc:[ \w=~-]+\]\] -->")
        while True:
            # codeblock check (`x`, ```x```)
            codeblock_all = codeblock_re.findall(self.doc.last_line)
            for mark in codeblock_all:
                if codeblock_mark is None:
                    codeblock_mark = mark
                elif codeblock_mark == mark:
                    codeblock_mark = None
            # detect
            keyword_detected = False
            if not codeblock_mark:
                # detect toc
                if toc_re.match(self.doc.last_line):
                    keyword_detected = True
                    signal = "common"
                    # toc level
                    level_re = re.compile(
                        r"level[ ]*=[ ]*([1-9]~[1-9]|~[1-9]+|[1-9]+~?)"
                    )
                    level_option = level_re.search(self.doc.last_line)
                    if level_option is None:
                        msg = "You forgot the level option on the table of contents."
                        raise self.CustomException(msg)
                    level = level_option.group()[6:]
                    lmin, lmax = (1, 9)
                    if len(level) == 3:  # 1~2
                        lmin, lmax = [int(x) for x in level.split("~")]
                    elif len(level) == 2:
                        if level[0] == "~":  # ~2
                            lmax = int(level[1])
                        else:  # 2~
                            lmin = int(level[0])
                    else:  # 2
                        lmin, lmax = int(level)
                    # toc emoji
                    no_emoji_re = re.compile("no-emoji")
                    enable_emoji = no_emoji_re.search(self.doc.last_line) is None
                    # toc record
                    for all_doc in self.lang_doc.values():
                        all_doc.set_toc(
                            _min=lmin, _max=lmax, enable_emoji_header=enable_emoji
                        )
                # detect signal
                elif self.pattern.match(self.doc.last_line):
                    keyword_detected = True
                    signal = self.doc.last_line.replace(" ", "")[5:-5]
            # write
            if not keyword_detected:
                if signal == "common":
                    for all_doc in self.lang_doc.values():
                        all_doc.write(self.doc.last_line, codeblock_mark)
                elif signal == "ignore":
                    pass
                else:
                    self.lang_doc[signal].write(self.doc.last_line, codeblock_mark)
            # terminal conditions
            # base doc end
            if not self.doc.readline():
                break

        for md in self.lang_doc.values():
            md.success = True


def is_base_md(filename):
    base = re.compile(r"[.]base[.]md")
    return base.search(filename)


def filtered_base_list(filelist):
    for filename in filenames:
        if is_base_md(filename):
            yield filename


def search(dir_name):
    for path, folder, files in os.walk(dir_name):
        for file_name in files:
            if is_base_md(file_name):
                yield (path, file_name)


@click.command()
@click.argument("filenames", nargs=-1, type=click.Path(exists=True))
@click.option(
    "-r",
    "--recursive",
    is_flag=True,
    help="This recursive option searches all subfolders based on current directory and convert all base files.",
)
def cli(filenames, recursive):
    if recursive or filenames:
        base_count = 0
        click.secho("----------------------", fg="cyan")
        if recursive:
            for path, filename in search("."):
                MultilangualDoc(path, filename)
                base_count += 1
        if filenames:
            for filename in filtered_base_list(filenames):
                MultilangualDoc(".", filename)
                base_count += 1
        click.secho("----------------------", fg="cyan")
        click.secho(f" => {base_count} base markdowns were converted.\n", fg="cyan")
    else:
        raise click.UsageError(
            "You have not entered anything. Do 'mmg Foo.base.md' or 'mmg --recursive'."
        )


if __name__ == "__main__":
    assert sys.version_info[0] == 3
    try:
        cli()
    except Exception as e:
        click.echo(e)
