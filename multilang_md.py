# -*- coding: utf-8 -*-

import sys
import os
import re
from collections import OrderedDict  # toc


def search(dir_name):
    base = re.compile('[.]base[.]md')
    for path, folder, files in os.walk(dir_name):
        for file_name in files:
            if base.search(file_name):
                yield (path, file_name)


def remove_emoji(text):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text) # no emoji


def create_toc(_dict, _min, _max, enable_emoji_header, toc_str="", level=1):
    for head, child in _dict.items():
        if (_min <= level) and (level <= _max):
            # head
            if not enable_emoji_header:
                head = remove_emoji(head)
            # suburl
            spc = "[`~!@#$%\^&\*\(\)_=\+\|\[\]\{\}\\\\;:\'\",./<>\?]+"
            suburl = re.sub(spc, '', head)
            suburl = remove_emoji(suburl)
            suburl = suburl.replace('  ', ' ').replace(' ', '-')
            # toc line
            temp = '1. [{}](#{})\n'.format(head, suburl)
            # append
            toc_str += '    '*(level - _min)
            toc_str += temp
        # recursive
        toc_str = create_toc(child, _min, _max, enable_emoji_header, toc_str, level+1)
    return toc_str


class CreateMonolangualDoc(object):
    def __init__(self, path, file_name, lang, suffix=True):
        fname, base, ename = file_name.split(".")
        new_name = fname + ("."+lang+"." if suffix else ".") + ename
        self.full_name = os.path.join(path, new_name)

        self.doc = open(self.full_name, 'w', encoding='utf-8')

        self.content = []

        self.toc = OrderedDict()
        self.header_re = re.compile('#+ ')
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
            if isinstance(line, str):
                self.doc.write(line)
            elif isinstance(line, tuple):  # toc
                # (_min, _max, enable_emoji_header)
                self.doc.write(
                    create_toc(self.toc, line[0], line[1], line[2]))
            else:
                raise NotImplementedError

    def write(self, oneline, codeblock_mark):
        # write
        self.content.append(oneline)
        # check header
        if not codeblock_mark:
            result = self.header_re.match(oneline)
            if result:
                head = oneline[result.end():].replace('\n', '')
                self.append_toc(head, result.end()-1)

    def append_toc(self, head, level):
        if (self.prev_level + 1) == level:  # new child
            pass
        elif self.prev_level == level:  # same level
            self.toc_stack = self.toc_stack[:-1]
        elif self.prev_level > level:  # new elem
            self.toc_stack = self.toc_stack[:(level-1)]
        else:
            msg = "[Error] toc level mismatch. prev_level="
            msg += "{}, current_level={}".format(self.prev_level, level)
            print(msg)
            raise NotImplementedError
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
            self.__doc = open(full_name, 'r', encoding='utf-8')
            self.line_count = 0
            self.last_line = ""

        def __del__(self):
            self.__doc.close()

        def readline(self):
            self.line_count += 1
            self.last_line = self.__doc.readline()
            return self.last_line

    def __init__(self, path, file_name):
        self.full_name = os.path.join(path, file_name)
        self.doc = self.SafetyRead(self.full_name)

        # Initialize configuration
        self.lang_read = {}
        self.lang_doc = {}
        self.no_suffix = ''
        self.pattern = re.compile('[ \t]*<!-- \[\w+\] -->')  # <!-- [oo] -->
        self.init_config(path, file_name)

        # Main converting
        self.converting()
        self.log()

    def log(self):
        print(self.full_name)
        for lang, md in self.lang_doc.items():
            print("\t{}: {}".format(lang, md))

    def init_config(self, path, file_name):
        # re options
        options = [
            (re.compile('<!-- multilangual suffix:[ ]*([\w]+)(, [\w]+)*'),
                self.config_setlang),
            (re.compile('<!-- no suffix:[ ]*([\w]+)'),
                self.config_nosuffix)
        ]
        once = [False for _ in options]
        # check base doc
        while True:
            for i in range(len(options)):
                # if detect some option
                if options[i][0].match(self.doc.last_line):
                    if not once[i]:
                        options[i][1](self.doc.last_line)
                        once[i] = True
                    else:
                        print("[Error] Duplicate config:")
                        print("\t" + self.doc.last_line + "\n")
                        raise NotImplementedError
            # terminal conditions
            # 1. all options were setted
            if not (False in once):
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
                print("[Error] You cannot use [common] and [ignore] as a suffix.")
                raise NotImplementedError
            self.lang_read[x] = False

    def config_nosuffix(self, line):
        lang = line.replace(" ", "")[13:-4]
        self.no_suffix = lang

    def converting(self):
        # set the starting point
        while not self.pattern.match(self.doc.last_line):
            self.doc.readline()
        # converting
        signal = 'common'
        codeblock_re = re.compile('`+')
        codeblock_mark = None
        toc_re = re.compile('<!-- \[\[ multilangual toc:[ \w=~-]+\]\] -->')
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
                    signal = 'common'
                    # toc level
                    level_re = re.compile('level[ ]*=[ ]*([1-9]~[1-9]|~[1-9]+|[1-9]+~?)')
                    level = level_re.search(self.doc.last_line).group()[6:]
                    if level is None:
                        print("[Error] You forgot the level option on the table of contents.")
                        raise NotImplementedError
                    lmin, lmax = (1, 9)
                    if len(level) == 3:  # 1~2
                        lmin, lmax = [int(x) for x in level.split('~')]
                    elif len(level) == 2:
                        if level[0] == '~':  # ~2
                            lmax = int(level[1])
                        else:  # 2~
                            lmin = int(level[0])
                    else:  # 2
                        lmin, lmax = int(level)
                    # toc emoji
                    no_emoji_re = re.compile('no-emoji')
                    enable_emoji = (no_emoji_re.search(self.doc.last_line) == None)
                    # toc record
                    for all_doc in self.lang_doc.values():
                        all_doc.set_toc(
                            _min=lmin,
                            _max=lmax,
                            enable_emoji_header=enable_emoji)
                # detect signal
                elif self.pattern.match(self.doc.last_line):
                    keyword_detected = True
                    signal = self.doc.last_line.replace(" ", "")[5:-5]
            # write
            if not keyword_detected:
                if signal == 'common':
                    for all_doc in self.lang_doc.values():
                        all_doc.write(self.doc.last_line, codeblock_mark)
                elif signal == 'ignore':
                    pass
                else:
                    self.lang_doc[signal].write(
                        self.doc.last_line, codeblock_mark)
            # terminal conditions
            # base doc end
            if not self.doc.readline():
                break

        for md in self.lang_doc.values():
            md.success = True


if __name__ == "__main__":
    assert(sys.version_info[0] is 3)
    base_count = 0
    dir_name = "."
    print("----------------------")
    for p, f in search(dir_name):
        MultilangualDoc(p, f)
        base_count += 1
    print("----------------------")
    print("{} base markdowns were converted.\n".format(base_count))
