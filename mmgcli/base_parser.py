import os
import re
import click
from mmgcli.single_gen import CreateMonolangualDoc


class MultilingualDoc(object):

    class SafetyRead(object):
        def __init__(self, full_name):
            self.__doc = open(full_name, "r", encoding="utf-8")
            self.__checker = open(full_name, "r", encoding="utf-8")
            self.line_count = 0
            self.last_line = ""

        def __del__(self):
            self.__doc.close()
            self.__checker.close()

        def readline(self):
            self.line_count += 1
            self.last_line = self.__doc.readline()
            return self.last_line

        def line_check(self):
            return self.__checker.readline()

    def __init__(self, path, file_name):
        self._base_file = file_name
        self._full_name = os.path.join(path, self._base_file)
        self.doc = self.SafetyRead(self._full_name)

        # Initialize configuration
        self.lang_read = {}
        self.lang_doc = {}
        self.no_suffix = ""
        self.pattern = re.compile(r"[ \t]*<!-- \[\w+(\-\w+)*\] -->")  # <!-- [oo] -->
        self.codeblock_re = re.compile("`+")
        self._init_config(path, self._base_file)

    @property
    def file_name(self):
        return self._base_file

    @property
    def full_name(self):
        return self._full_name

    class HealthCounter(object):
        def __init__(self, suffix_dict):
            self._counter = dict.fromkeys(suffix_dict, 0)

        def is_healthy(self, suffix):
            # check
            self._counter[suffix] += 1
            health = False if any([x > 1 for x in self._counter.values()]) else True
            # reset
            if all([x == 1 for x in self._counter.values()])\
               or any([x > 1 for x in self._counter.values()]):
                self._counter = dict.fromkeys(self._counter, 0)
            return health

        def is_healthy_keyword(self, keyword):
            if keyword == "common":
                if any([x > 0 for x in self._counter.values()]):
                    return False if any([x < 1 for x in self._counter.values()]) else True
            return True

    def check_log(self, verbosity=0):
        keywords = ['common', 'ignore']
        suffixes = list(self.lang_doc.keys())
        unknown = '<Unknown>'

        suffix_counter = dict.fromkeys(self.lang_doc, 0)
        health_counter = self.HealthCounter(self.lang_doc)

        buffer = ""

        line_number = 0
        codeblock_mark = None
        while True:
            line = self.doc.line_check()
            if not line:
                break  # End of doc
            line_number += 1

            # codeblock check (`x`, ```x```)
            codeblock_all = self.codeblock_re.findall(line)
            for mark in codeblock_all:
                if codeblock_mark is None:
                    codeblock_mark = mark
                elif codeblock_mark == mark:
                    codeblock_mark = None

            if (not codeblock_mark) and self.pattern.match(line):
                this = line.replace(" ", "")[5:-5]
                if this in suffixes:
                    suffix_counter[this] += 1
                    if verbosity > 0 and not health_counter.is_healthy(this):
                        buffer += f"\n\tLine {line_number}: This language reappeared before all languages appeared once."
                elif this in keywords:
                    if verbosity > 0 and not health_counter.is_healthy_keyword(this):
                        buffer += f"\n\tLine {line_number}: A common area appeared before all languages come out."
                else:
                    if unknown not in suffix_counter:
                        suffix_counter[unknown] = 0
                    suffix_counter['<Unknown>'] += 1
                    if verbosity > 0:
                        buffer += f"\n\tLine {line_number}: Unknown suffix detected."

        max_tag = max(suffix_counter.values())
        missing = sum(1 if max_tag != x else 0 for x in suffix_counter.values())

        color = "bright_red" if missing else "bright_green"
        message = ""
        if verbosity > 0:
            message = f"\t[X] {missing} language(s) not translated.\n\t    " if missing else "\t[O] "
            message += f"Tag count: {str(suffix_counter)}"
            message += buffer
        return message, color




    def run(self):
        # Main converting
        self._converting()
        self._log()

    def CustomException(self, message):
        return click.ClickException(f"<{self._base_file}> {message}")

    def _log(self):
        click.echo(self._full_name)
        for lang, md in self.lang_doc.items():
            click.echo(f"\t{lang}: {md}")

    def _init_config(self, path, file_name):
        # re options
        options = [
            (
                re.compile(r"<!-- multilingual suffix:[ ]*([\w]+)(, [\w]+)*"),
                self._config_setlang,
            ),
            (re.compile(r"<!-- no suffix:[ ]*([\w]+)"), self._config_nosuffix),
        ]
        option_checked = [False for _ in options]
        # check base doc
        while True:
            for i, _ in enumerate(options):
                # if detect some option
                if options[i][0].match(self.doc.last_line):
                    if option_checked[i]:
                        msg = f"Duplicate config: {self.doc.last_line}\n"
                        raise self.CustomException(msg)
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
        # prepare a single doc
        for lang, _ in self.lang_read.items():
            self.lang_doc[lang] = CreateMonolangualDoc(
                path, file_name, lang, suffix=(lang != self.no_suffix)
            )

    def _config_setlang(self, line):
        langs = line.replace(" ", "")[23:-4].split(",")
        protected_keywords = ["common", "ignore"]
        for x in langs:
            if x in protected_keywords:
                msg = "You cannot use [common] and [ignore] as a suffix."
                raise self.CustomException(msg)
            self.lang_read[x] = False

    def _config_nosuffix(self, line):
        lang = line.replace(" ", "")[13:-4]
        self.no_suffix = lang

    def _converting(self):
        # set the starting point
        while not self.pattern.match(self.doc.last_line):
            self.doc.readline()
        # converting
        signal = "common"
        codeblock_mark = None
        toc_re = re.compile(r"<!-- \[\[ multilingual toc:[ \w=~-]+\]\] -->")
        while True:
            # codeblock check (`x`, ```x```)
            codeblock_all = self.codeblock_re.findall(self.doc.last_line)
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
                    elif len(level) == 1:  # 2
                        lmin = int(level)
                        lmax = lmin
                    else:
                        msg = f"Cannot parse level, value = '{level}'."
                        raise self.CustomException(msg)
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
                    value_lang_doc = self.lang_doc.get(signal)
                    if value_lang_doc:
                        value_lang_doc.write(self.doc.last_line, codeblock_mark)
                    else:
                        msg = f"Missing '{signal}' language. Check your " \
                              f"header 'multilingual suffix'."
                        raise self.CustomException(msg)
            # terminal conditions
            # base doc end
            if not self.doc.readline():
                break

        for md in self.lang_doc.values():
            md.success = True
