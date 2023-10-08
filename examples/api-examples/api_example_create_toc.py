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
            print(f">> Toc (no-emoji: {toc_options[2]}):\n{toc}\n")


if __name__ == "__main__":
    main()
