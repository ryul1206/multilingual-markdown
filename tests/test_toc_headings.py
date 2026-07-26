"""Tests for how `create_toc` reads a heading line.

Two long-standing defects lived in that parsing step:

- the heading level was derived from the whole `^#+\\s+` match, so the blanks after the
  marks were counted as levels and `#  Title` was indented as an h2;
- the marks were removed with `str.replace`, which also deleted any later occurrence of
  the same text, so `# A # B` was displayed as `A B`.
"""

import pytest
from mmg.toc import TocOptions, create_toc


level_cases = [
    # doc, expected indentation of the single entry
    (["# Title"], ""),
    (["#  Title"], ""),  # two blanks after the mark, still an h1
    (["#\tTitle"], ""),  # a tab after the mark, still an h1
    (["# Parent", "## Child"], "    "),  # the h2 is one level deep
]


@pytest.mark.parametrize("doc, expected_indent", level_cases)
def test_heading_level_counts_the_marks_only(doc, expected_indent):
    entry = create_toc(TocOptions(1, 6, False), doc)[-1]
    indent = entry[: len(entry) - len(entry.lstrip())]
    assert indent == expected_indent, entry


def test_only_the_leading_marks_are_removed():
    """`# A # B` is a heading whose text is `A # B`, not `A B`.

    The anchor keeps both dashes because dropping the `#` leaves two blanks behind,
    which is what `github-slugger` does too.
    """
    assert create_toc(TocOptions(1, 6, False), ["# A # B"]) == ["1. [A # B](#a--b)"]


def test_a_heading_that_is_only_marks_is_not_a_heading():
    """`^#+\\s+` needs a blank after the marks, so `#hashtag` stays plain text."""
    assert create_toc(TocOptions(1, 6, False), ["#hashtag"]) == []


if __name__ == "__main__":
    pytest.main()
