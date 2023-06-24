import pytest
from mmg.toc import parse_toc_options


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
]


@pytest.mark.parametrize("i, test_case", enumerate(test_cases))
def test_parse_toc_options(i, test_case):
    truth, toc_line = test_case
    anwser = parse_toc_options(toc_line)
    assert anwser == truth, f"Test case {i} failed: Expected {truth}, but got {anwser}."


if __name__ == "__main__":
    pytest.main()
