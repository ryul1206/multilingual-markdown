from typing import Dict, List
import copy
from mmg.config import Config
from mmg.utils import REGEX_PATTERN, flag_code_block_lines
from mmg.toc import create_toc, parse_toc_options


class MarkdownClassifier:
    def __init__(self, lang_tags: List[str]):
        self.docs: Dict[str, List[str]] = {lang: [] for lang in lang_tags}
        self.freezed = False

    def _write(self, tag, line):
        # Check if the classifier is freezed
        if self.freezed:
            raise RuntimeError("Cannot write to the classifier after freezing.")
        # Write
        if tag == "common":
            for doc in self.docs.values():
                doc.append(line)
        elif tag != "ignore":
            self.docs[tag].append(line)

    def classify(self, base_doc: List[str]):
        # signal (str): Tag for the current line.
        signal = "common"
        codeblock = flag_code_block_lines(base_doc)

        for line_num, line in enumerate(base_doc):
            # DEBUG
            # m = "O" if REGEX_PATTERN["comment"].match(line) else "X"
            # c = "O" if codeblock[line_num] else "X"
            # print(f"{line_num}: match[{m}] code[{c}]: {line}")

            if REGEX_PATTERN["comment"].match(line) and (not codeblock[line_num]):
                # Case 1: Tag
                #   * Switch the signal to the tag.
                detected_tag = REGEX_PATTERN["tag"].search(line)
                if detected_tag:
                    signal = detected_tag.group(1)
                    # If the tag is <Unknown>, ignore it.
                    if (signal not in self.docs.keys()) and (signal != "common"):
                        signal = "ignore"
                # Case 2: Table of Contents
                #   * Mark TOC position. In some cases, the table of contents (TOC) can vary for each tag,
                #     so for now, we will only determine the TOC position and generate the TOC at the end.
                #   * And, the signal will be switched to "common".
                elif REGEX_PATTERN["auto_toc"].match(line):
                    signal = "common"
                    self._write(signal, line)
            else:
                # DEBUG
                # print(f"    write[{signal}]: {line}")
                self._write(signal, line)

    def insert_toc(self):
        # Freeze, no more writing
        self.freezed = True
        # Insert ToC
        for lang, doc in self.docs.items():
            self.docs[lang] = replace_toc(doc, doc)


class JupyterClassifier:
    def __init__(self, lang_tags: List[str]):
        self.docs: Dict[str, Dict] = {lang: {} for lang in lang_tags}
        self.freezed = False

    def init_targets(self, base_jn: Dict):
        """Initialize the target notebooks and copy metadata."""
        for key, value in base_jn.items():
            for doc in self.docs.values():
                doc[key] = copy.deepcopy(value) if key != "cells" else []

    def push(self, cell: Dict):
        """Divide the cell into each language and push to the target notebooks.

        Args:
            cell (Dict): The cell to push.

        Raises:
            RuntimeError: Cannot push to the classifier after freezing.
        """
        # Check if the classifier is freezed
        if self.freezed:
            raise RuntimeError("Cannot push to the classifier after freezing.")
        # Push
        if cell["cell_type"] == "markdown":
            # Split the markdown cell into each language
            doc = cell["source"]
            target_sources = MarkdownClassifier(self.docs.keys())
            target_sources.classify(doc)
            # Push when the source is not empty
            for lang, src in target_sources.docs.items():
                # Skip if the source is empty
                if not src:
                    continue
                # Push
                temp_cell = {k: copy.deepcopy(v) if k != "source" else src for k, v in cell.items()}
                self.docs[lang]["cells"].append(temp_cell)
        else:
            for doc in self.docs.values():
                doc["cells"].append(copy.deepcopy(cell))

    def insert_toc(self):
        # Freeze, no more writing
        self.freezed = True
        # Collect all markdown cells
        for lang, nb in self.docs.items():
            md_cells = [cell for cell in nb["cells"] if cell["cell_type"] == "markdown"]
            md_doc = [line for cell in md_cells for line in cell["source"]]  # flatten
            # Put ToC
            for md_cell in md_cells:
                md_cell["source"] = replace_toc(md_cell["source"], md_doc)


def replace_toc(source: List[str], entire_doc: List[str]) -> List[str]:
    new_source = []  # partial doc
    codeblock = flag_code_block_lines(source)
    for i, line in enumerate(source):
        if REGEX_PATTERN["auto_toc"].match(line) and (not codeblock[i]):
            toc_options = parse_toc_options(line)
            new_source.extend(create_toc(toc_options, entire_doc))
        else:
            new_source.append(line)
    return new_source
