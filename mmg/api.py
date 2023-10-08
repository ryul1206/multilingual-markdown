from typing import List, Dict
from mmg.config import Config, extract_config_from_md, extract_config_from_jupyter
from mmg.health import HealthChecker, HealthStatus
from mmg.exceptions import BadConfigError
from mmg.classifier import MarkdownClassifier, JupyterClassifier


def convert(
    base_md: str,
    cfg: Config = None,
    skip_health_check: bool = False,
    force_convert: bool = False,
    print_log: bool = False,
    file_name: str = None,
    verbosity: int = 0,
) -> Dict[str, str]:
    """Split the base markdown string into multiple markdowns based on the config.

    Args:
        base_md (str): The base markdown string to convert.
        cfg (Config, optional): The config to convert.
            If not given, the config will be extracted from the base_md. Defaults to None.
        skip_health_check (bool, optional): If True, skip the health check. Defaults to False.
        force_convert (bool, optional): If True, ignore the health check result and force to convert.
            This option is not working when `skip_health_check` is True. Defaults to False.
        print_log (bool, optional): If True, print the log.
            This option is not working when `skip_health_check` is True. Defaults to False.
        file_name (str, optional): The file name to show in the log.
            This option is not working when `print_log` is False. Defaults to None.
        verbosity (int, optional): The verbosity level from 0 to 2.
            This option is not working when `print_log` is False. Defaults to 0.

    Returns:
        Dict[str, str]: A dictionary of converted markdowns. The key is the language tag, a.k.a. suffix.
    """
    base_doc: List[str] = base_md.splitlines()
    target_docs: Dict[str, List[str]] = convert_base_doc(
        base_doc, cfg, skip_health_check, force_convert, print_log, file_name, verbosity
    )
    return {lang: "\n".join(doc) for lang, doc in target_docs.items()}


def convert_base_doc(
    base_doc: List[str],
    cfg: Config = None,
    skip_health_check: bool = False,
    force_convert: bool = False,
    print_log: bool = False,
    file_name: str = None,
    verbosity: int = 0,
) -> Dict[str, List[str]]:
    """Split the base_doc into multiple markdowns based on the config.

    Args:
        base_doc (List[str]): The base markdown string to convert.
        cfg (Config, optional): The config to convert.
            If not given, the config will be extracted from the base_doc. Defaults to None.
        skip_health_check (bool, optional): If True, skip the health check. Defaults to False.
        force_convert (bool, optional): If True, ignore the health check result and force to convert.
            This option is not working when `skip_health_check` is True. Defaults to False.
        print_log (bool, optional): If True, print the log.
            This option is not working when `skip_health_check` is True. Defaults to False.
        file_name (str, optional): The file name to show in the log.
            This option is not working when `print_log` is False. Defaults to None.
        verbosity (int, optional): The verbosity level from 0 to 2.
            This option is not working when `print_log` is False. Defaults to 0.

    Raises:
        BadConfigError: If the health check failed.

    Returns:
        Dict[str, List[str]]: A dictionary of converted markdowns. The key is the language tag, a.k.a. suffix.
    """
    # Extract config (using HealthChecker)
    # > If `cfg` is not given, extract it from the base_md.
    # > If `cfg` is provided, settings in base_md will be ignored.
    cfg: Config = cfg if cfg else extract_config_from_md(base_doc)

    # Health check
    _health_check(
        base_doc,
        cfg,
        extension="md",
        skip_health_check=skip_health_check,
        force_convert=force_convert,
        print_log=print_log,
        file_name=file_name,
        verbosity=verbosity,
    )

    # Classify lines
    target_docs = MarkdownClassifier(cfg.lang_tags)
    target_docs.classify(base_doc)

    # Generate TOC
    target_docs.insert_toc()

    # Return
    return target_docs.docs


def convert_base_jupyter(
    base_jn: Dict,
    cfg: Config = None,
    skip_health_check: bool = False,
    force_convert: bool = False,
    print_log: bool = False,
    file_name: str = None,
    verbosity: int = 0,
) -> Dict[str, Dict]:
    """Split the base jupyter notebook into multiple markdowns based on the config.

    Args:
        base_jn (Dict): The base jupyter notebook to convert.
        cfg (Config, optional): The config to convert.
            If not given, the config will be extracted from the base_jn. Defaults to None.
        skip_health_check (bool, optional): If True, skip the health check. Defaults to False.
        force_convert (bool, optional): If True, ignore the health check result and force to convert.
            This option is not working when `skip_health_check` is True. Defaults to False.
        print_log (bool, optional): If True, print the log.
            This option is not working when `skip_health_check` is True. Defaults to False.
        file_name (str, optional): The file name to show in the log.
            This option is not working when `print_log` is False. Defaults to None.
        verbosity (int, optional): The verbosity level from 0 to 2.
            This option is not working when `print_log` is False. Defaults to 0.

    Raises:
        BadConfigError: If the health check failed.

    Returns:
        Dict[str, Dict]: A dictionary of converted jupyter notebooks. The key is the language tag, a.k.a. suffix.
    """
    # Extract config (using HealthChecker)
    # > If `cfg` is not given, extract it from the base_md.
    # > If `cfg` is provided, settings in base_md will be ignored.
    cfg: Config = cfg if cfg else extract_config_from_jupyter(base_jn)

    # Health check
    _health_check(
        base_jn,
        cfg,
        extension="ipynb",
        skip_health_check=skip_health_check,
        force_convert=force_convert,
        print_log=print_log,
        file_name=file_name,
        verbosity=verbosity,
    )

    # Classify cells
    jupyter_docs = JupyterClassifier(cfg.lang_tags)
    jupyter_docs.init_targets(base_jn)
    for cell in base_jn["cells"]:
        jupyter_docs.push(cell)

    # Generate TOC
    jupyter_docs.insert_toc()

    # Return
    return jupyter_docs.docs


def _health_check(
    base: any,
    cfg: Config,
    extension: str,
    skip_health_check: bool,
    force_convert: bool,
    print_log: bool,
    file_name: str,
    verbosity: int,
):
    if not skip_health_check:
        hc = HealthChecker()
        status: HealthStatus = hc.health_check(base, cfg=cfg, extension=extension)
        if print_log:
            log = hc.cli_log(file_name=file_name, verbosity=verbosity)
            print("\n".join(log))
        if (not force_convert) and (status != HealthStatus.HEALTHY):
            error_messages = "\n".join(hc.error_messages)
            raise BadConfigError(f"Health check failed.\n - Status: {status.name}\n - Error:\n{error_messages}")
