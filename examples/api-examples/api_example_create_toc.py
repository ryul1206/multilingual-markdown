from typing import List
from mmg.utils import REGEX_PATTERN
from mmg.toc import create_toc, parse_toc_options

base_md: str = """
# 🔎 Header 1

Here are some examples of the table of contents.

**Table of Contents with Emoji**

<!-- [[ multilingual toc: level=2~3 ]] -->

**Table of Contents without Emoji**

<!-- [[ multilingual toc: level=2~3 no-emoji ]] -->

**Table of Contents with Jupyter anchors**

<!-- [[ multilingual toc: level=2~3, anchor=jupyter ]] -->

## 📝 Header 2

Foo

### 🌈 Header 3

Bar
"""


def main():
    doc = base_md.splitlines()
    for line in doc:
        if REGEX_PATTERN["auto_toc"].match(line):
            toc_options = parse_toc_options(line)
            toc: List[str] = create_toc(toc_options, doc)
            toc: str = "\n".join(toc)
            # `parse_toc_options` returns a `TocOptions` named tuple, so the options
            # can be read by name instead of by position.
            print(f">> Toc (no-emoji: {toc_options.no_emoji}, anchor: {toc_options.anchor}):\n{toc}\n")


if __name__ == "__main__":
    main()
