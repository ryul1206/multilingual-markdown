from dataclasses import dataclass, field
from typing import List, Optional
import re
from mmg.exceptions import MmgException


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
    REGEX_TAG = re.compile(r"<!--[\w ]*-->")
    REGEX_LANG_TAGS = re.compile(r"<!-- multilingual suffix:[ ]*([\w]+)(, [\w]+)*")
    REGEX_NO_SUFFIX = re.compile(r"<!-- no suffix:[ ]*([\w]+)")

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
            if cls.REGEX_TAG.match(line):
                cfg = cls._try_update_lang_tags(line, cfg, line_num)
                cfg = cls._try_update_no_suffix(line, cfg, line_num)
        return cfg

    @classmethod
    def _try_update_lang_tags(cls, line: str, cfg: Config, line_num: int) -> Config:
        m = cls.REGEX_LANG_TAGS.search(line)
        lang_tags = m.group(1).split(", ")
        cfg.lang_tags = cls._update_config_value(cfg.lang_tags, lang_tags, "lan_tags", line_num)
        return cfg

    @classmethod
    def _try_update_no_suffix(cls, line: str, cfg: Config, line_num: int) -> Config:
        m = cls.REGEX_NO_SUFFIX.search(line)
        no_suffix = m.group(1)
        cfg.no_suffix = cls._update_config_value(cfg.no_suffix, no_suffix, "no_suffix", line_num)
        return cfg

    @staticmethod
    def _update_config_value(old_value: any, new_value: any, config_name: str, line_num: int) -> any:
        if new_value and old_value:
            raise MmgException(f"The configuration '{config_name}' is already defined. [line: {line_num + 1}]")
        return new_value if new_value else old_value
