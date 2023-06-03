from mmg.api import Config


def main():
    cfg1 = Config()
    cfg1.lang_tags = ["en", "fr", "kr", "jp"]  # Language tags are also used as suffixes.
    cfg1.no_suffix_tag = "en"
    print(f"cfg1: {cfg1}")

    cfg2 = Config(
        lang_tags=["en", "fr", "kr", "jp"],
        no_suffix_tag="en",
    )
    print(f"cfg2: {cfg2}")


if __name__ == "__main__":
    main()
