from mmg.api import HealthChecker


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

    hc = HealthChecker(base_md)
    print(f" - Health check: {'✅OK' if hc.health_check() else '❌NG'}")
    print(f" - Health message: {hc.health_messages}")
    print(f" - Tag list: {hc.tag_count}")


if __name__ == "__main__":
    main()
