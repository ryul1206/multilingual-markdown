import pytest
from mmg.exceptions import BadConfigError
from mmg.toc import TocOptions, parse_toc_options


# Each expectation is spelled as a plain tuple and widened with `TocOptions(*truth)`
# in the test, so a 3-tuple case also asserts that `anchor` defaults to "github".
test_cases = [
    # Min, Max, No emoji
    ((2, 3, True), "<!-- [[ multilingual toc: level=2~3, no-emoji ]] -->"),
    ((2, 3, True), "<!-- [[ multilingual toc: level=2~ 3, no-emoji ]] -->"),
    ((2, 3, True), "<!-- [[ multilingual toc: level=2 ~3, no-emoji ]] -->"),
    ((2, 3, True), "<!-- [[ multilingual toc: level=2 ~ 3, no-emoji ]] -->"),
    ((2, 3, True), "<!-- [[ multilingual toc: level= 2~3, no-emoji ]] -->"),
    ((2, 3, True), "<!-- [[ multilingual toc: level =2~3, no-emoji ]] -->"),
    ((2, 3, True), "<!-- [[ multilingual toc: level = 2~3, no-emoji ]] -->"),
    ((2, 3, True), "<!-- [[ multilingual toc: level = 2~ 3, no-emoji ]] -->"),
    # Max, No emoji
    ((1, 3, True), "<!-- [[ multilingual toc: level=~3, no-emoji ]] -->"),
    ((1, 3, True), "<!-- [[ multilingual toc: level=~ 3, no-emoji ]] -->"),
    ((1, 3, True), "<!-- [[ multilingual toc: level= ~ 3, no-emoji ]] -->"),
    ((1, 3, True), "<!-- [[ multilingual toc: level = ~3, no-emoji ]] -->"),
    ((1, 3, True), "<!-- [[ multilingual toc: level = ~ 3, no-emoji ]] -->"),
    # Min, No emoji
    ((1, 9, True), "<!-- [[ multilingual toc: level=1~, no-emoji ]] -->"),
    ((1, 9, True), "<!-- [[ multilingual toc: level = 1~, no-emoji ]] -->"),
    ((1, 9, True), "<!-- [[ multilingual toc: level = 1 ~ , no-emoji ]] -->"),
    # Single, No emoji
    ((2, 2, True), "<!-- [[ multilingual toc: level=2, no-emoji ]] -->"),
    ((2, 2, True), "<!-- [[ multilingual toc: level = 2, no-emoji ]] -->"),
    ((2, 2, True), "<!-- [[ multilingual toc: level = 2 , no-emoji ]] -->"),
    # Min, Max
    ((2, 3, False), "<!-- [[ multilingual toc: level=2~3 ]] -->"),
    ((2, 3, False), "<!-- [[ multilingual toc: level=2~ 3 ]] -->"),
    ((2, 3, False), "<!-- [[ multilingual toc: level=2 ~3 ]] -->"),
    ((2, 3, False), "<!-- [[ multilingual toc: level=2 ~ 3 ]] -->"),
    ((2, 3, False), "<!-- [[ multilingual toc: level= 2~3 ]] -->"),
    ((2, 3, False), "<!-- [[ multilingual toc: level =2~3 ]] -->"),
    ((2, 3, False), "<!-- [[ multilingual toc: level = 2~3 ]] -->"),
    ((2, 3, False), "<!-- [[ multilingual toc: level = 2~ 3 ]] -->"),
    # Max
    ((1, 3, False), "<!-- [[ multilingual toc: level=~3 ]] -->"),
    ((1, 3, False), "<!-- [[ multilingual toc: level=~ 3 ]] -->"),
    ((1, 3, False), "<!-- [[ multilingual toc: level= ~ 3 ]] -->"),
    ((1, 3, False), "<!-- [[ multilingual toc: level = ~3 ]] -->"),
    ((1, 3, False), "<!-- [[ multilingual toc: level = ~ 3 ]] -->"),
    # Min
    ((1, 9, False), "<!-- [[ multilingual toc: level=1~ ]] -->"),
    ((1, 9, False), "<!-- [[ multilingual toc: level = 1~ ]] -->"),
    ((1, 9, False), "<!-- [[ multilingual toc: level = 1 ~  ]] -->"),
    # Single
    ((2, 2, False), "<!-- [[ multilingual toc: level=2 ]] -->"),
    ((2, 2, False), "<!-- [[ multilingual toc: level = 2 ]] -->"),
    ((2, 2, False), "<!-- [[ multilingual toc: level = 2  ]] -->"),
    # Anchor style (issue #36)
    ((2, 3, False, "github"), "<!-- [[ multilingual toc: level=2~3, anchor=github ]] -->"),
    ((2, 3, False, "jupyter"), "<!-- [[ multilingual toc: level=2~3, anchor=jupyter ]] -->"),
    ((2, 3, False, "jupyter"), "<!-- [[ multilingual toc: level=2~3, anchor = jupyter ]] -->"),
    ((2, 3, False, "jupyter"), "<!-- [[ multilingual toc: level=2~3, anchor= jupyter ]] -->"),
    # Anchor style, combined with the other options in either order
    ((2, 3, True, "jupyter"), "<!-- [[ multilingual toc: level=2~3, no-emoji, anchor=jupyter ]] -->"),
    ((2, 3, True, "jupyter"), "<!-- [[ multilingual toc: level=2~3, anchor=jupyter, no-emoji ]] -->"),
    ((1, 9, True, "jupyter"), "<!-- [[ multilingual toc: anchor=jupyter, no-emoji, level=1~ ]] -->"),
]


@pytest.mark.parametrize("i, test_case", enumerate(test_cases))
def test_parse_toc_options(i, test_case):
    truth, toc_line = test_case
    truth = TocOptions(*truth)  # A 3-tuple case asserts the default anchor style.
    anwser = parse_toc_options(toc_line)
    assert anwser == truth, f"Test case {i} failed: Expected {truth}, but got {anwser}."


bad_anchor_cases = [
    "<!-- [[ multilingual toc: level=2~3, anchor=colab ]] -->",
    "<!-- [[ multilingual toc: level=2~3, anchor=GitHub ]] -->",
    "<!-- [[ multilingual toc: level=2~3, anchor= ]] -->",
]


@pytest.mark.parametrize("toc_line", bad_anchor_cases)
def test_parse_toc_options_rejects_unknown_anchor(toc_line):
    """An unknown anchor style must be reported instead of silently falling back."""
    with pytest.raises(BadConfigError):
        parse_toc_options(toc_line)


if __name__ == "__main__":
    pytest.main()
