"""Tests for the ToC anchor styles (issue #36) and for ToC output inside a notebook.

Issue #36 is not a bug but a mismatch of conventions: MMG builds GitHub-flavored
anchors (lowercased, punctuation stripped) while Jupyter/nbconvert/Colab keep the case
and the punctuation of the heading. `anchor=jupyter` opts into the latter; `github`
stays the default because most MMG output is a GitHub README.

The notebook tests also cover a separate defect found while working on the issue #35:
a Jupyter cell keeps the line endings inside `source`, so the ToC generator used to
leak a `\\n` into the anchor and to emit entries that collapsed into a single line.
"""

import pytest
from mmg.api import convert, convert_base_jupyter
from mmg.toc import TocOptions, create_toc


HEADING = "# Nombre d'étoiles sur GitHub"

GITHUB_ENTRY = "1. [Nombre d'étoiles sur GitHub](#nombre-détoiles-sur-github)"
JUPYTER_ENTRY = "1. [Nombre d'étoiles sur GitHub](#Nombre-d'%C3%A9toiles-sur-GitHub)"


anchor_cases = [
    ("github", GITHUB_ENTRY),
    ("jupyter", JUPYTER_ENTRY),
]


@pytest.mark.parametrize("anchor, expected", anchor_cases)
def test_create_toc_follows_the_requested_anchor_style(anchor, expected):
    assert create_toc(TocOptions(1, 3, False, anchor), [HEADING]) == [expected]


# Every expectation below was measured by rendering the same heading with
# `jupyter nbconvert --to html` and reading the `id` of the generated `<h1>`.
# The rule is: trim the text, turn each blank into "-", then percent-encode whatever
# `encodeURI()` would escape, plus "#".
nbconvert_slugs = [
    ("# Nombre d'étoiles sur GitHub", "Nombre-d'%C3%A9toiles-sur-GitHub"),
    ("# Hello, World!", "Hello,-World!"),
    ("# a/b?c&d", "a/b?c&d"),
    ("# Heading 💎", "Heading-%F0%9F%92%8E"),
    ("# A  B", "A--B"),
    ("# A # B", "A-%23-B"),
    ("#  Title", "Title"),
    ("# Trailing space ", "Trailing-space"),
    ("# Tab\tafter", "Tab%09after"),
    ("# 한국어 제목", "%ED%95%9C%EA%B5%AD%EC%96%B4-%EC%A0%9C%EB%AA%A9"),
]


@pytest.mark.parametrize("heading, expected_slug", nbconvert_slugs)
def test_jupyter_slug_matches_nbconvert(heading, expected_slug):
    entry = create_toc(TocOptions(1, 6, False, "jupyter"), [heading])[0]
    assert entry.endswith(f"](#{expected_slug})"), entry


# Every expectation below was measured with `github-slugger`, the reference
# implementation of the GitHub rules: lowercase, keep only letters, digits, marks, "_",
# "-" and blanks, then turn each remaining blank into a "-".
github_slugs = [
    ("# Simple", "simple"),
    ("# Two words", "two-words"),
    ("# A  B", "a--b"),  # a blank is never collapsed
    ("# A   C", "a---c"),
    ("# Trailing space ", "trailing-space"),
    ("# Tab\tafter", "tabafter"),  # a control character is dropped, not turned into "-"
    ("# Hello, World!", "hello-world"),
    ("# Nombre d'étoiles sur GitHub", "nombre-détoiles-sur-github"),
    ("# 한국어 제목", "한국어-제목"),
    ("# Heading 💎", "heading-"),
    ("# a/b?c&d", "abcd"),
    ("# snake_case_name", "snake_case_name"),  # "_" is kept, unlike other punctuation
    ("# kebab-case-name", "kebab-case-name"),
    ("# café — dash", "café--dash"),  # an em dash is dropped, leaving both blanks
    ("# e.g. U.S.A.", "eg-usa"),
    ("# MiXeD CaSe", "mixed-case"),
]


@pytest.mark.parametrize("heading, expected_slug", github_slugs)
def test_github_slug_matches_github_slugger(heading, expected_slug):
    entry = create_toc(TocOptions(1, 6, False, "github"), [heading])[0]
    assert entry.endswith(f"](#{expected_slug})"), entry


# --------------------------------------------------------------------------------------
# Repeated headings
# --------------------------------------------------------------------------------------


def slugs_of(doc, anchor, min_level=1):
    entries = create_toc(TocOptions(min_level, 6, False, anchor), doc)
    return [entry.split("](#", 1)[1][:-1] for entry in entries]


def test_github_disambiguates_repeated_headings():
    """GitHub appends -1, -2 ... to a repeated heading ID."""
    assert slugs_of(["# Setup", "# Setup", "# Setup"], "github") == ["setup", "setup-1", "setup-2"]


def test_github_skips_a_suffix_that_is_already_taken():
    """`# Setup 1` owns `setup-1`, so the second `# Setup` has to move on to `setup-2`."""
    assert slugs_of(["# Setup 1", "# Setup", "# Setup"], "github") == ["setup-1", "setup", "setup-2"]


def test_github_counts_headings_the_toc_leaves_out():
    """A renderer gives an ID to every heading, even one filtered out of this ToC."""
    assert slugs_of(["# Setup", "## Setup"], "github", min_level=2) == ["setup-1"]


def test_github_ignores_headings_inside_a_code_block():
    doc = ["# Setup", "```", "# Setup", "```", "# Setup"]
    assert slugs_of(doc, "github") == ["setup", "setup-1"]


def test_jupyter_repeats_the_same_slug():
    """nbconvert emits the very same ID for each repetition, so MMG must not disambiguate."""
    assert slugs_of(["# Setup", "# Setup", "# Setup"], "jupyter") == ["Setup", "Setup", "Setup"]


def test_github_is_the_default_anchor_style():
    """Changing this default would silently break the ToC of every GitHub README."""
    assert create_toc(TocOptions(1, 3, False), [HEADING]) == [GITHUB_ENTRY]
    assert create_toc((1, 3, False), [HEADING]) == [GITHUB_ENTRY]


# --------------------------------------------------------------------------------------
# Markdown output
# --------------------------------------------------------------------------------------


def base_md(toc_marker):
    return "\n".join(
        [
            "<!-- multilingual suffix: en -->",
            toc_marker,
            "<!-- [en] -->",
            HEADING,
            "## Sub heading",
        ]
    )


markdown_cases = [
    ("<!-- [[ multilingual toc: level=1~3 ]] -->", GITHUB_ENTRY),
    ("<!-- [[ multilingual toc: level=1~3, anchor=github ]] -->", GITHUB_ENTRY),
    ("<!-- [[ multilingual toc: level=1~3, anchor=jupyter ]] -->", JUPYTER_ENTRY),
]


@pytest.mark.parametrize("toc_marker, expected_entry", markdown_cases)
def test_markdown_toc_uses_the_requested_anchor_style(toc_marker, expected_entry):
    out = convert(base_md(toc_marker))["en"]
    assert expected_entry in out.splitlines()


# --------------------------------------------------------------------------------------
# Jupyter output
# --------------------------------------------------------------------------------------


def base_notebook(toc_marker):
    return {
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": ["<!-- multilingual suffix: en -->\n"]},
            {"cell_type": "markdown", "metadata": {}, "source": [toc_marker + "\n"]},
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["<!-- [en] -->\n", HEADING + "\n", "## Sub heading\n"],
            },
        ],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def toc_cell_source(toc_marker):
    out = convert_base_jupyter(base_notebook(toc_marker))["en"]
    return out["cells"][0]["source"]


@pytest.mark.parametrize("toc_marker, expected_entry", markdown_cases)
def test_jupyter_toc_uses_the_requested_anchor_style(toc_marker, expected_entry):
    assert toc_cell_source(toc_marker)[0] == expected_entry + "\n"


def test_jupyter_toc_never_leaks_a_line_ending_into_the_entry():
    """A notebook keeps the line ending inside `source`; it must not reach the anchor."""
    for line in toc_cell_source(markdown_cases[0][0]):
        text, _, anchor = line.partition("](#")
        assert "\n" not in text, f"A line ending leaked into the link text: {line!r}"
        assert "\n" not in anchor.rstrip("\n"), f"A line ending leaked into the anchor: {line!r}"


def test_jupyter_toc_entries_stay_on_separate_lines():
    """Without a line ending per element, a notebook renders the whole ToC as one line."""
    source = toc_cell_source(markdown_cases[0][0])
    assert len(source) == 2, f"Expected one element per ToC entry, got {source!r}"
    assert "".join(source).splitlines() == [GITHUB_ENTRY, "    1. [Sub heading](#sub-heading)"]


if __name__ == "__main__":
    pytest.main()
