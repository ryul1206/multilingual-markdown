import pytest
from typing import List, Tuple
from mmg.utils import CodeBlockTracker


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
}


@pytest.mark.parametrize("name, scenario", scenarios.items())
def test_code_block_tracker(name, scenario):
    tracker = CodeBlockTracker()
    tracker.parse(scenario.doc)
    assert scenario == tracker.result, f"Failed: {name}"


if __name__ == "__main__":
    pytest.main()
