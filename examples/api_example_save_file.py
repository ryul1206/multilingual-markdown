from typing import Dict
import mmg.api as mmg


def main(fake: bool = True):
    base_md: str = """
    <!---------------------------->
    <!-- multilingual suffix: A, B, C -->
    <!---------------------------->
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
    converted_mds: Dict[str, str] = mmg.convert(base_md)
    if fake:
        print(f"Fake mode: skip saving file. Detected tags: {converted_mds.keys()}")
        return
    for tag, txt in converted_mds.items():
        with open(f"./{tag}.md", "w", encoding="utf-8") as f:
            f.write(txt)


if __name__ == "__main__":
    main(fake=False)
