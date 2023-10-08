from mmg.health import HealthChecker, HealthStatus

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


def main():
    hc = HealthChecker()
    status: HealthStatus = hc.health_check(base_md.splitlines())

    print(f" - Health check: {status.name}")
    print(" - Health messages:")
    for msg in hc.warning_messages:
        print(f"\t[WARN] {msg}")
    for msg in hc.error_messages:
        print(f"\t[ERR ] {msg}")
    print(f" - Tag list: {hc.tag_count}")


if __name__ == "__main__":
    main()
