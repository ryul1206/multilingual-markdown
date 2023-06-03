from typing import Dict
import mmg.api as mmg


def main():
    # Read a markdown file as a string
    base_file: str = "./sample.base.md"
    with open(base_file, "r", encoding="utf-8") as f:
        base_md: str = f.read()

    # Convert markdown string
    converted_mds: Dict[str, str] = mmg.convert(base_md)
    for tag, txt in converted_mds.items():
        print(f"\n>> Tag: {tag}")
        print(txt)


if __name__ == "__main__":
    main()
