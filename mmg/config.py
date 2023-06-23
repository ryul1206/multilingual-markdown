from dataclasses import dataclass, field
from typing import List, Optional, Final, Dict
import re
from mmg.exceptions import MmgException


RESERVED_KEYWORDS: Final[List] = ["common", "ignore", "<Unknown>"]


REGEX_PATTERN: Final[Dict[str, re.Pattern]] = {
    "comment": re.compile(r"<!--.*-->"),
    "tag": re.compile(r"<!--\s*\[\s*([\w-]+)\s*\]\s*-->"),
    "lang_tags": re.compile(r"(<!-- multilingual suffix:)\s*([\w\s,-]+)(?=\s--)"),
    "no_suffix": re.compile(r"<!-- no suffix:\s*([\w-]+)"),
}


@dataclass
class Config:
    """
    Configuration class to control the behavior of MMG.

    Args:
        lang_tags (List[str]): A List of language tags to be used. Language tags are also used as suffixes.
        no_suffix (str, optional): Prevents the suffix from being appended to the file name when creating the file.
            For example, setting `no_suffix` to 'en' will generate `FileName.md` instead of `FileName.en.md`.
            This option is useful for a README file on GitHub.

    """

    lang_tags: List[str] = field(default_factory=list)
    no_suffix: Optional[str] = None


class ConfigExtractor:
    @classmethod
    def extract(cls, base_md: str) -> Config:
        """
        Extract configuration from the base markdown string.

        Args:
            base_md (str): A base markdown string.

        Returns:
            Config: A configuration extracted from the base markdown file.
        """
        cfg = Config()
        for line_num, line in enumerate(base_md.splitlines()):
            if REGEX_PATTERN["comment"].match(line):
                cfg = cls._try_update_lang_tags(line, cfg, line_num)
                cfg = cls._try_update_no_suffix(line, cfg, line_num)
        return cfg

    @classmethod
    def _try_update_lang_tags(cls, line: str, cfg: Config, line_num: int) -> Config:
        m = REGEX_PATTERN["lang_tags"].search(line)
        if m:
            cls._check_duplicate_config_value(cfg.lang_tags, "lang_tags", line_num)
            lang_tags = m.group(2).replace(" ", "").split(",")
            cfg.lang_tags = lang_tags
        return cfg

    @classmethod
    def _try_update_no_suffix(cls, line: str, cfg: Config, line_num: int) -> Config:
        m = REGEX_PATTERN["no_suffix"].search(line)
        if m:
            cls._check_duplicate_config_value(cfg.no_suffix, "no_suffix", line_num)
            no_suffix = m.group(1)
        return cfg

    @staticmethod
    def _check_duplicate_config_value(value: any, config_name: str, line_num: int):
        if value:
            raise MmgException(f"The configuration '{config_name}' is already defined. [line: {line_num + 1}]")
