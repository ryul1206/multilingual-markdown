from typing import List, Dict, Tuple
from enum import Enum, auto
from mmg.utils import flag_code_block_lines, REGEX_PATTERN
from mmg.config import Config, extract_config_from_md, extract_config_from_jupyter, RESERVED_KEYWORDS
from mmg.toc import parse_toc_options
from mmg.exceptions import BadConfigError


class HealthStatus(Enum):
    NOT_CHECKED = auto()
    HEALTHY = auto()
    UNHEALTHY = auto()


class HealthChecker:
    def __init__(self):
        self._reset()

    def _reset(self):
        self._status: HealthStatus = HealthStatus.NOT_CHECKED
        self._warning: List[str] = []
        self._error: List[str] = []
        self._tag_count: Dict[str, int] = {}

    @property
    def health_status(self) -> str:
        return self._status.name

    @property
    def is_healthy(self) -> bool:
        return self._status == HealthStatus.HEALTHY

    @property
    def warning_messages(self) -> List[str]:
        return self._warning

    @property
    def error_messages(self) -> List[str]:
        return self._error

    @property
    def tag_count(self) -> Dict[str, int]:
        return self._tag_count

    def cli_log(self, file_name: str = None, verbosity: int = 0) -> List[str]:
        """Return the log string of the CLI style.

        Args:
            file_name (str, optional): The file name to show in the log. Defaults to None.
            verbosity (int, optional): The verbosity level from 0 to 2. Defaults to 0.

        Returns:
            str: The log string.
        """
        icon = "✅" if self.is_healthy else "❌"
        if self._tag_count:
            tag_count_max = max(self._tag_count.values())
            num_incomplete = sum(1 if x != tag_count_max else 0 for x in self._tag_count.values())
            if num_incomplete:
                icon = "❌"
        else:
            num_incomplete = 0
            icon = "❌"
        file_name = file_name if file_name else "Anonymous file"
        # Messages
        messages = [f" {icon} {file_name}"]
        if verbosity > 0:
            if num_incomplete:
                messages.append(f"    {num_incomplete} language(s) not translated.")
            messages.append(f"    Tag count: {str(self._tag_count)}")
        if verbosity > 1:
            messages.extend([f"\t{message}" for message in self._error])
            messages.extend([f"\t{message}" for message in self._warning])
        return messages

    def _check_config(self, cfg: Config):
        # Check if there are reserved keywords in lang_tags.
        for keyword in cfg.lang_tags:
            if keyword in RESERVED_KEYWORDS:
                self._error.append(f"Config: Reserved keyword '{keyword}' is used in lang_tags.")
                self._status = HealthStatus.UNHEALTHY
        # Check the `no_suffix` tag` in lang_tags.
        if cfg.no_suffix:
            if cfg.no_suffix not in cfg.lang_tags:
                self._error.append(f"Config: no_suffix '{cfg.no_suffix}' is not in lang_tags.")
                self._status = HealthStatus.UNHEALTHY

    def health_check(self, base: any, cfg: Config = None, extension: str = "md") -> HealthStatus:
        """Check the health based on the current config.

        Args:
            base (any): The base file to check. Markdown(List[str]) or Jupyter(Dict).
            cfg (Config, optional): The config to check. If not given, the config will be extracted from the base_md.
            extension (str, optional): The extension of the base file. "md" or "ipynb". Defaults to "md".

        Returns:
            HealthStatus: The health status. (HEALTHY, UNHEALTHY, NOT_CHECKED)
        """
        # Reset for the current config
        self._reset()
        # Check
        if extension == "md":
            self._health_check_markdown(base, cfg)
        elif extension == "ipynb":
            self._health_check_jupyter(base, cfg)
        # If no tag detected, it is unhealthy.
        if not self._tag_count:
            self._error.append("No tag detected.")
            self._status = HealthStatus.UNHEALTHY
        # If no error detected, the health is healthy.
        self._status = HealthStatus.HEALTHY if self._status != HealthStatus.UNHEALTHY else self._status
        return self._status

    def _health_check_markdown(self, base_doc: List[str], cfg: Config = None):
        # Check the config
        cfg: Config = cfg if cfg else extract_config_from_md(base_doc)
        self._check_config(cfg)
        # Check the doc
        dc = DocChecker(cfg)
        dc.check_doc(base_doc)
        # Get the tag count, warning, and error messages.
        self._tag_count = dc.tag_count
        self._error.extend([f"Line {line_num}: {message}" for line_num, message in dc.error_messages])
        self._warning.extend([f"Line {line_num}: {message}" for line_num, message in dc.warning_messages])

    def _health_check_jupyter(self, base_jn: Dict, cfg: Config = None):
        # Check the config
        cfg: Config = cfg if cfg else extract_config_from_jupyter(base_jn)
        self._check_config(cfg)
        # Make a doc (list of lines)
        # > Because, some people may use multiple language tags in a single Markdown cell,
        # > while others may only use one language tag in a Markdown cell.
        indexing: List[Tuple[int, int]] = []  # indexing[line_num - 1] = (cell_num, cell_line_num)
        doc: List[str] = []
        for i, cell in enumerate(base_jn["cells"]):
            cell_num = i + 1
            # "markdown" cell
            if cell["cell_type"] == "markdown":
                indexing.extend([(cell_num, j + 1) for j, _ in enumerate(cell["source"])])
                doc.extend(cell["source"])
            # "code" cell
            else:
                indexing.append((cell_num, 0))
                doc.append("<!-- [common] -->")
        # Check the doc
        dc = DocChecker(cfg)
        dc.check_doc(doc)
        # Get the tag count, warning, and error messages.
        self._tag_count = dc.tag_count

        def _header(x):
            return f"Cell {x[0]}, Line {x[1]}: "

        self._error.extend([_header(indexing[line_num - 1]) + message for line_num, message in dc.error_messages])
        self._warning.extend([_header(indexing[line_num - 1]) + message for line_num, message in dc.warning_messages])


class DocChecker:
    def __init__(self, cfg: Config):
        self._cfg: Config = cfg
        self._balance_count: Dict[str, int] = dict.fromkeys(cfg.lang_tags, 0)
        self._tag_count: Dict[str, int] = dict.fromkeys(cfg.lang_tags, 0)
        self._tag_count["<Unknown>"] = 0
        self._warning: List[Tuple[int, str]] = []  # (line_num, message)
        self._error: List[Tuple[int, str]] = []  # (line_num, message)
        self._used: bool = False

    @property
    def warning_messages(self) -> List[str]:
        return self._warning

    @property
    def error_messages(self) -> List[str]:
        return self._error

    @property
    def tag_count(self) -> Dict[str, int]:
        # If "<Unknown>" is zero, return the tag count without "<Unknown>".
        if self._tag_count["<Unknown>"] == 0:
            return {k: v for k, v in self._tag_count.items() if k != "<Unknown>"}
        return self._tag_count

    def check_doc(self, doc: List[str]):
        # Check if the DocChecker is already used.
        if self._used:
            raise RuntimeError("The DocChecker can be used only once.")
        self._used = True

        # Flag the code block lines.
        codeblock_flag = flag_code_block_lines(doc)

        # Check the tag line by line.
        for line_num, line in enumerate(doc):
            # Skip the code block lines.
            if codeblock_flag[line_num]:
                continue
            # Normal tags
            detected_tag = REGEX_PATTERN["tag"].search(line)
            if detected_tag:
                # Find "<!-- [A] -->" or "<!--[A]-->" and extract the tag "A".
                tag = detected_tag.group(1)
                looks_good = self._push(tag, line_num + 1)  # The line number starts from 1.
                if not looks_good:
                    self._status = HealthStatus.UNHEALTHY
            # ToC tags
            elif REGEX_PATTERN["auto_toc"].search(line):
                try:
                    parse_toc_options(line)
                except BadConfigError as e:
                    self._error.append((line_num, e))
                    self._status = HealthStatus.UNHEALTHY

    def _push(self, tag: str, line_num: int) -> bool:
        """Push a tag to check the balance.

        Args:
            tag (str): The tag to push.
            line_num (int): The line number of the tag.

        Returns:
            bool: True if the tag is balanced. False otherwise.
        """
        if tag in self._cfg.lang_tags:
            self._balance_count[tag] += 1
            self._tag_count[tag] += 1

            _is_unbalanced = any([x > 1 for x in self._balance_count.values()])
            _all_appeared_once = all([x == 1 for x in self._balance_count.values()])

            # Unbalanced if any tag appears again before all tags appear once.
            if _is_unbalanced:
                self._warning.append((line_num, f"'{tag}' appeared again before all tags appeared once."))
                self._balance_count[tag] -= 1
            # Reset the balance count if all tags appeared once.
            if _all_appeared_once:
                self._balance_count = dict.fromkeys(self._balance_count, 0)
            return False if _is_unbalanced else True
        elif tag == "common":
            _any_appeared = any([x > 0 for x in self._balance_count.values()])
            # The `common` area should appear after all tags appeared once. (balanced)
            self._balance_count = dict.fromkeys(self._balance_count, 0)
            if _any_appeared:
                self._warning.append((line_num, f"'{tag}' appeared before all tags appeared once."))
            return False if _any_appeared else True
        elif tag == "ignore":
            return True
        else:
            self._tag_count["<Unknown>"] += 1
            self._error.append((line_num, f"Unknown tag '{tag}' detected."))
            return False
