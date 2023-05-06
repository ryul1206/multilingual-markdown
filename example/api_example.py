# This is an example of how to use the API.
# Same as the CLI, you can use the API to convert markdown files.


from mmg.base_parser import MultilingualDoc
from typing import Dict


def example1():
    """
    Convert markdown file and save it
    The result is the same as the CLI: `mmg ./example.base.md`
    """
    base_file: str = "./example.base.md"
    base_md: str = open(base_file, "r", encoding="utf-8").read()

    # Convert markdown string
    parsed_md = MultilingualDoc(base_md)
    converted_mds: Dict[str, str] = parsed_md.convert(print_log=True)
    log = parsed_md.log

    # Save the converted markdown file with the tag as the file name.
    for tag, txt in converted_mds.items():
        doc = open(f"./{tag}.md", "w", encoding="utf-8")
        doc.write(txt)
        doc.close()


def example2():
    """
    Convert markdown string and print it
    """
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

    # Convert markdown string
    parsed_md = MultilingualDoc(base_md)
    converted_mds: Dict[str, str] = parsed_md.convert(print_log=False)
    log = parsed_md.log

    # Print the converted markdown string
    for tag, txt in converted_mds.items():
        print(f"\n>> Tag: {tag}")
        print(txt)


if __name__ == "__main__":
    example1()
    example2()
