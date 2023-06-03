from typing import Dict
import mmg.api as mmg


def main():
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
    for tag, txt in converted_mds.items():
        print(f"\n>> Tag: {tag}")
        print(txt)


if __name__ == "__main__":
    main()
