from typing import List, Dict
from enum import Enum, auto
from mmg.utils import flag_code_block_lines, REGEX_PATTERN
from mmg.config import Config, ConfigExtractor, RESERVED_KEYWORDS


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
    def warning_messages(self) -> List[str]:
        return self._warning

    @property
    def error_messages(self) -> List[str]:
        return self._error

    @property
    def tag_count(self) -> Dict[str, int]:
        return self._tag_count

    def cli_log(self, file_name: str = None, verbosity: int = 0) -> str:
        """Return the log string of the CLI style.

        Args:
            file_name (str, optional): The file name to show in the log. Defaults to None.
            verbosity (int, optional): The verbosity level from 0 to 2. Defaults to 0.

        Returns:
            str: The log string.
        """
        tag_count_max = max(self._tag_count.values())
        num_incomplete = sum(1 if x != tag_count_max else 0 for x in self._tag_count.values())
        icon = "❌" if num_incomplete else "✅"
        file_name = file_name if file_name else "Anonymous file"
        # Messages
        messages = "----------------------\n"
        messages += f" {icon} {file_name}\n"
        if verbosity > 0:
            messages += f"    {num_incomplete} language(s) not translated.\n" if num_incomplete else ""
            messages += f"    Tag count: {str(self._tag_count)}\n"
        if verbosity > 1:
            messages += "\n".join(self._error)
            messages += "\n".join(self._warning)
        messages += "----------------------\n"
        return messages

    def health_check(self, base_doc: List[str], cfg: Config = None) -> HealthStatus:
        """Check the health based on the current config.

        Args:
            base_md (str): The base markdown string to check.
            cfg (Config, optional): The config to check. If not given, the config will be extracted from the base_md.

        Returns:
            HealthStatus: The health status. (HEALTHY, UNHEALTHY, NOT_CHECKED)
        """
        # Reset for the current config
        self._reset()

        # Check the config
        cfg: Config = cfg if cfg else ConfigExtractor.extract(base_doc)
        self._check_config(cfg)

        # Parse the base_md to ignore command tags in code blocks.
        codeblock_flag = flag_code_block_lines(base_doc)
        self._check_doc(cfg, base_doc, codeblock_flag)

        # If no error detected, the health is healthy.
        if self._status == HealthStatus.NOT_CHECKED:
            self._status = HealthStatus.HEALTHY
        return self._status

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

    def _check_doc(self, cfg: Config, doc: List[str], codeblock_flag: List[bool]):
        # self._tag_count = dict.fromkeys(cfg.lang_tags, 0)
        balance_checker = _TagBalanceChecker(cfg)
        # Check the tag line by line.
        for line_num, line in enumerate(doc):
            is_codeblock = codeblock_flag[line_num]
            detected_tag = REGEX_PATTERN["tag"].search(line)
            if (not is_codeblock) and detected_tag:
                # Find "<!-- [A] -->" or "<!--[A]-->" and extract the tag "A".
                tag = detected_tag.group(1)
                looks_good = balance_checker.push(tag, line_num)
                if not looks_good:
                    self._status = HealthStatus.UNHEALTHY
        # Get the tag count, warning, and error messages.
        self._tag_count = balance_checker.tag_count
        self._warning.extend(balance_checker.warning_messages)
        self._error.extend(balance_checker.error_messages)


class _TagBalanceChecker:
    def __init__(self, cfg: Config):
        self._cfg: Config = cfg
        self._balance_count: Dict[str, int] = dict.fromkeys(cfg.lang_tags, 0)
        self._tag_count: Dict[str, int] = dict.fromkeys(cfg.lang_tags, 0)
        self._tag_count["<Unknown>"] = 0

        self._warning: List[str] = []
        self._error: List[str] = []

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

    def push(self, tag: str, line_num: int) -> bool:
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
                self._warning.append(f"Line {line_num}: '{tag}' appeared again before all tags appeared once.")
                self._balance_count[tag] -= 1
            # Reset the balance count if all tags appeared once.
            if _all_appeared_once:
                self._balance_count = dict.fromkeys(self._balance_count, 0)
            return False if _is_unbalanced else True
        elif tag == "common":
            _any_appeared = any([x > 0 for x in self._balance_count.values()])
            # The `common` area should appear after all tags appeared once. (balanced)
            if _any_appeared:
                self._warning.append(f"Line {line_num}: '{tag}' appeared before all tags appeared once.")
            return False if _any_appeared else True
        elif tag == "ignore":
            return True
        else:
            self._tag_count["<Unknown>"] += 1
            self._error.append(f"Line {line_num}: Unknown tag '{tag}' detected.")
            return False
