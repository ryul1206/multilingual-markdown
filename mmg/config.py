from dataclasses import dataclass, field
from typing import List, Optional, Final, Dict
from mmg.exceptions import BadConfigError
from mmg.utils import REGEX_PATTERN, flag_code_block_lines


RESERVED_KEYWORDS: Final[List] = ["common", "ignore", "<Unknown>"]


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


def _try_update_lang_tags(line: str, cfg: Config) -> Config:
    m = REGEX_PATTERN["lang_tags"].search(line)
    if m:
        _check_duplicate_config_value(cfg.lang_tags, "lang_tags")
        lang_tags = m.group(2).replace(" ", "").split(",")
        cfg.lang_tags = lang_tags
    return cfg


def _try_update_no_suffix(line: str, cfg: Config) -> Config:
    m = REGEX_PATTERN["no_suffix"].search(line)
    if m:
        _check_duplicate_config_value(cfg.no_suffix, "no_suffix")
        cfg.no_suffix = m.group(1)
    return cfg


def _check_duplicate_config_value(value: any, config_name: str):
    if value:
        raise BadConfigError(f"The configuration '{config_name}' is already defined.")


def extract_config_from_md(base_doc: List[str]) -> Config:
    """
    Extract configuration from the base markdown string.

    Args:
        base_doc (List[str]): A list of strings extracted from the base markdown file.

    Raises:
        BadConfigError: If the configuration is duplicated.

    Returns:
        Config: A configuration extracted from the base markdown file.
    """
    cfg = Config()

    is_in_code_block = flag_code_block_lines(base_doc)
    for line_num, line in enumerate(base_doc):
        if is_in_code_block[line_num]:
            continue
        if REGEX_PATTERN["comment"].match(line):
            try:
                cfg = _try_update_lang_tags(line, cfg)
                cfg = _try_update_no_suffix(line, cfg)
            except BadConfigError as e:
                raise BadConfigError(f"{e} [Check line: {line_num + 1}]")
    return cfg


def extract_config_from_jupyter(base_jn: Dict) -> Config:
    md_cells: List[str] = [cell["source"] for cell in base_jn["cells"] if cell["cell_type"] == "markdown"]
    md_cells = [line for cell in md_cells for line in cell]  # flatten
    cfg: Config = extract_config_from_md(md_cells)
    return cfg
