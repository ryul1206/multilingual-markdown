from typing import List, Dict
from mmg.config import Config, ConfigExtractor
from mmg.health import HealthChecker, HealthStatus
from mmg.utils import REGEX_PATTERN, flag_code_block_lines
from mmg.toc import create_toc, parse_toc_options
from mmg.exceptions import MmgException


def convert(
    base_md: str,
    cfg: Config = None,
    skip_health_check: bool = False,
    force_convert: bool = False,
    print_log: bool = False,
    verbosity: int = 0,
) -> Dict[str, str]:
    """Split the base_md into multiple markdowns based on the config.

    Args:
        base_md (str): The base markdown string to convert.
        cfg (Config, optional): The config to convert.
            If not given, the config will be extracted from the base_md. Defaults to None.
        skip_health_check (bool, optional): If True, skip the health check. Defaults to False.
        force_convert (bool, optional): If True, ignore the health check result and force to convert. Defaults to False.
        print_log (bool, optional): If True, print the log. Defaults to False.
        verbosity (int, optional): The verbosity level from 0 to 2. Defaults to 0.

    Returns:
        Dict[str, str]: A dictionary of converted markdowns. The key is the language tag, a.k.a. suffix.
    """
    base_doc: List[str] = base_md.splitlines()

    # Extract config (using HealthChecker)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # If `cfg` is not given, extract it from the base_md.
    # If `cfg` is provided, settings in base_md will be ignored.
    cfg: Config = cfg if cfg else ConfigExtractor.extract(base_doc)

    # Health check
    # ^^^^^^^^^^^^
    if not skip_health_check:
        hc = HealthChecker()
        status: HealthStatus = hc.health_check(base_doc, cfg=cfg)
        if print_log:
            print(hc.cli_log(verbosity=verbosity))
        if (not force_convert) and (status != HealthStatus.HEALTHY):
            raise MmgException(f"Health check failed: {status.name}")

    # Classify lines
    # ^^^^^^^^^^^^^^
    # signal (str): Tag for the current line.
    signal = "common"
    codeblock = flag_code_block_lines(base_doc)
    target_docs = _LineClassifier(cfg)

    for line_num, line in enumerate(base_doc):
        if REGEX_PATTERN["comment"].match(line) and (not codeblock[line_num]):
            # Case 1: Tag
            #   * Switch the signal to the tag.
            detected_tag = REGEX_PATTERN["tag"].search(line)
            if detected_tag:
                new_signal = detected_tag.group(1)
                signal = new_signal if new_signal in cfg.lang_tags else "ignore"
            # Case 2: Table of Contents
            #   * Mark TOC position. In some cases, the table of contents (TOC) can vary for each tag,
            #     so for now, we will only determine the TOC position and generate the TOC at the end.
            #   * And, the signal will be switched to "common".
            elif REGEX_PATTERN["auto_toc"].match(line):
                signal = "common"
                target_docs.write(signal, line)
        else:
            target_docs.write(signal, line)

    # Generate TOC
    # ^^^^^^^^^^^^
    target_docs.insert_toc()

    # Return
    # ^^^^^^
    return target_docs.docs


class _LineClassifier:
    def __init__(self, cfg: Config):
        self.docs: Dict[str, List[str]] = dict.fromkeys(cfg.lang_tags, [])

    def write(self, tag, line):
        if tag == "common":
            for doc in self.docs.values():
                doc.append(line)
        elif tag != "ignore":
            self.docs[tag].append(line)

    def insert_toc(self):
        for lang, doc in self.docs.items():
            new_doc = []
            for line in doc:
                if REGEX_PATTERN["auto_toc"].match(line):
                    toc_options = parse_toc_options(line)
                    new_doc.extend(create_toc(toc_options, doc))
                else:
                    new_doc.append(line)
            self.docs[lang] = new_doc
