"""Regression tests for the issue #35.

A Jupyter cell `source` is not guaranteed to be a list of single lines: the `nbformat`
spec also allows a bare string, and it allows a list element to hold several lines.
MMG parses documents line by line, so the conversion result must depend only on the
*text* of a cell, never on how that text happens to be serialized on disk.

Before the fix, a cell stored as one multi-line chunk was treated as a single line:
the leading `<!-- [xx] -->` matched the comment pattern, the whole chunk was consumed
as a tag line, and every line of the cell silently disappeared from the output.
"""

import pytest
from mmg.api import convert_base_jupyter
from mmg.config import extract_config_from_jupyter
from mmg.health import HealthChecker, HealthStatus
from mmg.utils import normalize_source_lines


HEADER_TEXT = "<!-- multilingual suffix: en, fr -->"
BODY_TEXT = "<!-- [fr] -->\nEn français\n<!--[en]-->\nIn english"


def serializations(text):
    """Every on-disk shape a cell holding `text` may legally take."""
    lines = text.splitlines(keepends=True)
    return {
        # The standard nbformat shape: one line per element.
        "line-per-element": lines,
        # A single chunk holding every line. This is what broke the issue #35 reporter.
        "one-multiline-element": [text],
        # A bare string instead of a list. Iterating it used to walk character by character.
        "bare-string": text,
        # A list whose elements straddle line boundaries.
        "mixed-chunks": ["".join(lines[:2]), *lines[2:]],
    }


def notebook(header_source, body_source):
    return {
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": header_source},
            {"cell_type": "markdown", "metadata": {}, "source": body_source},
        ],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def markdown_sources(notebook_out):
    return [cell["source"] for cell in notebook_out["cells"] if cell["cell_type"] == "markdown"]


# --------------------------------------------------------------------------------------
# The conversion result must not depend on the serialization of the body cell.
# --------------------------------------------------------------------------------------


@pytest.mark.parametrize("shape", sorted(serializations(BODY_TEXT)))
def test_body_cell_is_split_by_language_for_every_serialization(shape):
    body = serializations(BODY_TEXT)[shape]
    header = serializations(HEADER_TEXT)["line-per-element"]

    target_docs = convert_base_jupyter(notebook(header, body))

    assert sorted(target_docs) == ["en", "fr"], f"[{shape}] Both languages must be generated."
    assert markdown_sources(target_docs["fr"]) == [["En français\n"]], f"[{shape}] The French text vanished."
    assert markdown_sources(target_docs["en"]) == [["In english"]], f"[{shape}] The English text vanished."


@pytest.mark.parametrize("shape", sorted(serializations(HEADER_TEXT)))
def test_config_is_extracted_for_every_serialization_of_the_header_cell(shape):
    header = serializations(HEADER_TEXT)[shape]
    body = serializations(BODY_TEXT)["line-per-element"]

    cfg = extract_config_from_jupyter(notebook(header, body))

    assert cfg.lang_tags == ["en", "fr"], f"[{shape}] The config of the header cell was not found."


@pytest.mark.parametrize("shape", sorted(serializations(BODY_TEXT)))
def test_health_check_sees_every_tag_for_every_serialization(shape):
    body = serializations(BODY_TEXT)[shape]
    header = serializations(HEADER_TEXT)["line-per-element"]

    hc = HealthChecker()
    status = hc.health_check(notebook(header, body), extension="ipynb")

    assert status == HealthStatus.HEALTHY, f"[{shape}] {hc.error_messages}"
    assert hc.tag_count == {"en": 1, "fr": 1}, f"[{shape}] The tags were miscounted."


def test_single_language_cell_is_not_dropped():
    """A cell holding one language only. Structures #4 and #5 of the issue #35 matrix."""
    text = "<!-- [fr] -->\nEn français"
    header = serializations(HEADER_TEXT)["line-per-element"]

    for shape, body in serializations(text).items():
        target_docs = convert_base_jupyter(notebook(header, body))
        assert markdown_sources(target_docs["fr"]) == [["En français"]], f"[{shape}] The French text vanished."
        assert markdown_sources(target_docs["en"]) == [], f"[{shape}] English has no content in this notebook."


# --------------------------------------------------------------------------------------
# The normalization itself.
# --------------------------------------------------------------------------------------


round_trip_cases = [
    [],
    [""],
    "",
    "\n",
    ["\n\n"],
    ["a"],
    ["a\n"],
    ["a\nb", "c"],
    ["a\nb\n", "", "c\n"],
    "one\ntwo\nthree",
    ["# Title\n", "\n", "body\n"],
]


@pytest.mark.parametrize("source", round_trip_cases)
def test_normalize_source_lines_preserves_the_content(source):
    """Normalization may change the structure of `source`, never its text."""
    original = source if isinstance(source, str) else "".join(source)
    assert "".join(normalize_source_lines(source)) == original


@pytest.mark.parametrize("source", round_trip_cases)
def test_normalize_source_lines_yields_one_line_per_element(source):
    for element in normalize_source_lines(source):
        assert len(element.splitlines()) <= 1, f"{element!r} holds more than one line."


if __name__ == "__main__":
    pytest.main()
