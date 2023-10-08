from typing import Dict
import mmg.api as mmg

base_md: str = """
<!-- [A] -->
# Sample Document A

Hello, A!
<!-- [B] -->
# Sample Document B

Hello, B!
<!-- [C] -->
# Sample Document C

Hello, C!
<!-- [common] -->
Thank you for using mmg!
"""


def main():
    cfg = mmg.Config(lang_tags=["A", "B", "C"])
    print(f"Config: {cfg}")

    converted_mds: Dict[str, str] = mmg.convert(base_md, cfg=cfg)
    for tag, txt in converted_mds.items():
        print(f"\n>> Tag: {tag}")
        print(txt)


if __name__ == "__main__":
    main()
