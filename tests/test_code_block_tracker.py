import pytest
from typing import List, Tuple
from mmg.utils import flag_code_block_lines


CB = True
no = False


class Scenario:
    def __init__(self, doc: List[Tuple[bool, str]]):
        self.ans, self.doc = zip(*doc)

    def __len__(self):
        return len(self.doc)

    def __eq__(self, other_ans: List):
        for i in range(len(self)):
            if self.ans[i] != other_ans[i]:
                return False
        return True


scenarios = {
    "Text": Scenario(
        [
            (no, "This is not a code line."),
        ]
    ),
    "Single backtick inline": Scenario(
        [
            (CB, "This is a `code` line."),
        ]
    ),
    "Double backticks inline": Scenario(
        [
            (CB, "This is a ``code`` line."),
        ]
    ),
    "Three backticks inline": Scenario(
        [
            (no, "This is not a code line."),
            (CB, "This is a ```code``` line."),
            (no, "This is not a code line."),
            (CB, "```This is a code line.```"),
        ]
    ),
    "Three backticks block": Scenario(
        [
            (no, "This is not a code line."),
            (CB, "```"),
            (CB, "This is a code line."),
            (CB, "```"),
            (no, "This is not a code line."),
        ]
    ),
    "Single backtick inline (between lines)": Scenario(
        [
            (CB, "This is a `code line."),
            (CB, "This is a code line."),
            (CB, "This is a code` line."),
            (no, "This is not a code line."),
        ]
    ),
    "Double backtick inline (between lines)": Scenario(
        [
            (CB, "This is a ``code line."),
            (CB, "This is a code line."),
            (CB, "This is a code`` line."),
            (no, "This is not a code line."),
        ]
    ),
    "Three backtick inline (between lines)": Scenario(
        [
            (CB, "This is a ```code line."),
            (CB, "This is a code line."),
            (CB, "This is a code``` line."),
            (no, "This is not a code line."),
        ]
    ),
    "Fake single backtick (between lines)": Scenario(
        [
            (no, "This is not a `code line."),
            (no, ""),
            (no, "This is not a `code line."),
        ]
    ),
    "Fake double backtick (between lines)": Scenario(
        [
            (no, "This is not a ``code line."),
            (no, ""),
            (no, "This is not a ``code line."),
        ]
    ),
    "Fake three backtick (between lines)": Scenario(
        [
            (no, "This is not a ```code line."),
            (no, ""),
            (no, "This is not a ```code line."),
        ]
    ),
    "Complex code between lines": Scenario(
        [
            (no, "This is not a code line."),
            (no, "This is not a ```code line."),
            (no, "This is not a code line."),
            (CB, "```"),
            (CB, "This is a code line."),
            (CB, "This is a ```code line."),
            (CB, ""),
            (CB, "This is a code line."),
            (CB, "```"),
            (no, "This is not a code line."),
            (no, "This is not a ```code line."),
            (no, "This is not a code line."),
        ]
    ),
    "Double backtick lines": Scenario(
        [
            (no, "This is not a code line."),
            (no, "This is not a ```code line."),
            (no, "This is not a code line."),
            (CB, "```md"),
            (CB, "This is a code line."),
            (CB, "```md"),
            (CB, "This is a ```code line."),
            (CB, ""),
            (CB, "```"),
            (no, "This is not a code line."),
            (CB, "```"),
            (CB, "This is a code line."),
            (CB, "This is a ```code line."),
            (CB, "This is a code line."),
        ]
    ),
    "Code block in code block": Scenario(
        [
            (no, "This is not a code line."),
            (no, "This is not a ```code line."),
            (no, "This is not a code line."),
            (CB, "````md"),
            (CB, "This is a code line."),
            (CB, "```sh"),
            (CB, "This is a ```code line."),
            (CB, "This is a code line."),
            (CB, "```"),
            (CB, ""),
            (CB, "This is a code line."),
            (CB, "````"),
            (no, "This is not a code line."),
            (no, "This is not a ```code line."),
            (no, "This is not a code line."),
        ]
    ),
    "Open block": Scenario(
        [
            (no, "This is not a code line."),
            (no, "This is not a ```code line."),
            (no, "This is not a code line."),
            (CB, "````md"),
            (CB, "This is a code line."),
            (CB, "```sh"),
            (CB, "This is a ```code line."),
            (CB, "This is a code line."),
            (CB, "```"),
            (CB, ""),
            (CB, "This is a code line."),
        ]
    ),
    "Unbalanced block": Scenario(
        [
            (no, "This is not a code line."),
            (no, "This is not a ```code line."),
            (no, "This is not a code line."),
            (CB, "````md"),
            (CB, "This is a code line."),
            (CB, "```sh"),
            (CB, "This is a ```code line."),
            (CB, "This is a code line."),
            (CB, "``````"),
            (no, ""),
            (no, "This is not a code line."),
        ]
    ),
    "Indented block": Scenario(
        [
            (no, "This is not a code line."),
            (no, "This is not a ```code line."),
            (no, "This is not a code line."),
            (CB, "```md"),
            (CB, "This is a code line."),
            (CB, " ```"),
            (no, " This is not a ```code line."),
            (CB, " ```"),
            (CB, "This is a code line."),
            (CB, "``````"),
            (no, ""),
            (no, "This is not a code line."),
        ]
    ),
    "Indented block 2": Scenario(
        [
            (no, "This is not a code line."),
            (no, "This is not a ```code line."),
            (no, "This is not a code line."),
            (CB, "```md"),
            (CB, "This is a code line."),
            (CB, "    ```"),
            (CB, "    This is a ```code line."),
            (CB, "    ```"),
            (CB, "This is a code line."),
            (CB, "```"),
            (no, ""),
            (no, "This is not a code line."),
        ]
    ),
    "Indented block 3": Scenario(
        [
            (no, "This is not a code line."),
            (no, "This is not a ```code line."),
            (no, "This is not a code line."),
            (CB, "    ```md"),
            (CB, "    This is a code line."),
            (CB, "     ```"),
            (no, "     This is not a ```code line."),
            (CB, "        ```"),
            (no, "    This is not a code line."),
            (CB, "    ```"),
            (no, ""),
            (no, "This is not a code line."),
        ]
    ),
    "Unclosed indented block": Scenario(
        [
            (no, "This is not a code line."),
            (no, "This is not a ```code line."),
            (no, "This is not a code line."),
            (no, ""),
            (CB, "    ```md"),
            (CB, "    This is a code line."),
            (CB, "        ```"),
            (no, ""),
            (no, "This is not a code line."),
            (CB, "```"),
            (CB, ""),
            (CB, "This is a code line."),
        ]
    ),
}


@pytest.mark.parametrize("name, scenario", scenarios.items())
def test_code_block_tracker(name, scenario):
    result = flag_code_block_lines(scenario.doc)
    assert scenario == result, f"Failed: {name}"


if __name__ == "__main__":
    pytest.main()
