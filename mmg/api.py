from typing import Final, List, Dict
from mmg.config import Config, ConfigExtractor
from mmg.health import HealthChecker, HealthStatus


def convert(
    base_md: str,
    cfg: Config = None,
    skip_health_check: bool = False,
    print_log: bool = False,
    verbosity: int = 0,
) -> Dict[str, str]:
    # Extract config (using HealthChecker)
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # If `cfg` is not given, extract it from the base_md.
    # If `cfg` is provided, settings in base_md will be ignored.
    cfg: Config = cfg if cfg else ConfigExtractor.extract(base_md)

    # Health check
    # ^^^^^^^^^^^^
    if not skip_health_check:
        hc = HealthChecker()
        status: HealthStatus = hc.health_check(base_md, cfg=cfg)
        assert status == HealthStatus.HEALTHY, f"Health check failed: {status.name}"
        # if print_log:
        #     print(hc.cli_log(verbosity=verbosity))
    #
    raise NotImplementedError
