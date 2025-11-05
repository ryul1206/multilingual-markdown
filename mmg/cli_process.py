from typing import List, Dict, Tuple, Callable, Set
import sys
import os
import time
import json
import click
import yaml
from mmg.api import convert_base_doc, convert_base_jupyter
from mmg.config import Config, extract_config_from_md, extract_config_from_jupyter
from mmg.health import HealthChecker
from mmg.base_item import FileItem, collect_bases_from_dir, collect_bases_from_files
from mmg.cli_log import log_info, log_warn, log_error, set_log_dir
from mmg.exceptions import BadConfigError
from mmg import output


def query_yes_no(question):
    """Ask a yes/no question via raw_input() and return their answer.
    https://stackoverflow.com/questions/3041986/apt-command-line-interface-like-yes-no-input

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    default = "no"
    prompt = " [y/N] "

    resp = None
    while resp is None:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if choice == "":
            resp = valid[default]
        elif choice in valid:
            resp = valid[choice]
    return resp


def _process_file(item: FileItem) -> Tuple[FileItem, any, Config]:
    # Check if file exists
    if not os.path.isfile(item.norm_path):
        raise click.FileError(item.abs_path, hint="File not found.")
    # Open file
    with open(item.norm_path, "r", encoding="utf-8") as f:
        if item.extension == "md":
            base_md: str = f.read()
            base_doc: List[str] = base_md.splitlines()
            try:
                cfg: Config = extract_config_from_md(base_doc)
            except BadConfigError as e:
                log_error(f" => {repr(item)}: {e}")
                sys.exit(1)
            return (item, base_doc, cfg)
        elif item.extension == "ipynb":
            base_jn: Dict = json.load(f)
            cfg: Config = extract_config_from_jupyter(base_jn)
            return (item, base_jn, cfg)


def _health_check_on_backlogs(
    backlogs: Tuple,
    extension: str,
    emoji: str,
    skip_validation: bool,
    verbose: int,
) -> bool:
    all_healthy = True
    for item, base, cfg in backlogs:
        if skip_validation:
            log_info(f" {emoji} {repr(item)}")
        else:
            # Health check
            hc = HealthChecker()
            hc.health_check(base, cfg=cfg, extension=extension)
            if not hc.is_healthy:
                all_healthy = False
            # Print log
            log = hc.cli_log(file_name=repr(item), verbosity=verbose)
            log_info("\n".join(log))
    return all_healthy


def insert_preamble(file_name: str, content: any, preamble_text: str) -> any:
    """Insert the preamble text into the base document.

    Args:
        file_name (str): The file name to show in the preamble.
        content (any): The content to insert the preamble into.
            - List[str] (for markdown)
            - Dict (for jupyter notebook)
        preamble_text (str): The preamble text to insert.

    Returns:
        any: The content with the preamble inserted.
    """
    preamble_text = preamble_text.replace("<FILE_NAME>", file_name)
    # Markdown
    if isinstance(content, list):
        preamble_text = f"<!-- {preamble_text} -->"
        return [preamble_text] + content
    # Jupyter notebook
    elif isinstance(content, dict):
        preamble_cell = {
            "attachments": {},
            "cell_type": "markdown",
            "metadata": {},
            "source": [preamble_text],
        }
        return {**content, "cells": [preamble_cell] + content["cells"]}
    else:
        raise ValueError(f"Invalid content type: {type(content)} (Should be List[str] or Dict.)")


def _convert_backlogs(
    backlogs: List,
    convert_func: Callable,
    output_format: str,
    css: str,
    preamble: bool,
    preamble_text: str,
    source_dir: str = ".",
    output_dir: str = ".",
    tag_as: str = "suffix",
):
    # Check output format
    if output_format not in ["as-is", "html", "pdf"]:
        raise ValueError(f"Invalid output format: {output_format} (Should be 'as-is', 'html' or 'pdf'.)")

    # Markdown backlogs: List of (item: FileItem, base_doc: List[str], cfg: Config)
    # Jupyter notebook backlogs: List of (item: FileItem, base_jn: Dict, cfg: Config)
    for base_item, base, cfg in backlogs:
        no_suffix: str = cfg.no_suffix
        # When `tag_as`` is "suffix", `no_suffix` will remove the suffix from the file name.
        #   e.g. If no_suffix = "en-US" then
        #       ${source_dir}/file.en-US.md => ${output_dir}/file.md
        #       ${source_dir}/file.fr-FR.md => ${output_dir}/file.fr-FR.md
        #
        # When `tag_as` is "folder", `no_suffix` will omit the folder from the file path.
        #   e.g. If no_suffix = "en-US" then
        #       ${source_dir}/file.en-US.md => ${output_dir}/file.md
        #       ${source_dir}/file.fr-FR.md => ${output_dir}/fr-FR/file.md

        target_docs = convert_func(base, skip_health_check=True)
        # taget_docs: Dict of (key: lang, value: content)
        #   lang: str (e.g. "en-US")
        #   content: List[str] (for markdown) or Dict (for jupyter notebook)

        log_info(f" {repr(base_item)}", fg="cyan")

        # Get the relative path of the base file from the source directory.
        #   e.g. ${source_dir}/file.en-US.md => file.en-US.md
        rel_path = os.path.relpath(base_item.norm_path, source_dir)

        for lang, content in target_docs.items():
            # Add preamble
            if preamble:
                content = insert_preamble(base_item.file_name, content, preamble_text)

            # Get the target directory
            if tag_as == "suffix":
                target_dir = output_dir
                target_name = rel_path.replace(".base.", f".{lang}." if lang != no_suffix else ".")
            elif tag_as == "folder":
                target_dir = os.path.join(output_dir, lang if lang != no_suffix else ".")
                target_name = rel_path.replace(".base.", ".")

            # Get current cmd directory
            cmd_dir = os.getcwd()

            # Make save_path shorter
            save_path = os.path.normpath(os.path.join(target_dir, target_name))
            save_path = os.path.relpath(save_path, cmd_dir)

            # Make sure the directory exists
            save_dir = os.path.dirname(os.path.abspath(save_path))
            os.makedirs(save_dir, exist_ok=True)

            # Save
            if output_format == "as-is":
                target_item = FileItem(save_path, base_item.extension)
                output.handle_as_is(target_item, content)
            else:
                # Change only the last extension
                save_path = f"{os.path.splitext(save_path)[0]}.{output_format}"
                target_item = FileItem(save_path, output_format)
                output.handle_html_or_pdf(target_item, base_item.extension, css, content)

            log_info(f"\t{lang}: {repr(target_item)}")


def convert_cli_args(
    file_names: List[str],
    recursive: bool,
    output_format: str,
    css: str,
    yes: bool,
    skip_validation: bool,
    validation_only: bool,
    verbose: int,
    preamble: bool,
    preamble_text: str,
):
    # Get base files
    base_items = collect_bases_from_files(file_names)
    if recursive:
        base_items.update(collect_bases_from_dir(".", True))
    # Convert
    _convert_items(base_items, output_format, css, yes, skip_validation, validation_only, verbose, preamble, preamble_text)


def convert_batch(batch: str, preamble: bool, preamble_text: str, yes: bool):
    """Convert batch files.

    Args:
        batch (str): The path to the batch file.
        preamble (bool): Whether to add a preamble to the output files.
        preamble_text (str): The text to add to the output files.
        yes (bool): Whether to confirm the conversion without asking.
            If True, overrides the `convert_without_ask` setting in the batch file.
    """
    # Load batch file (yaml)
    if not os.path.isfile(batch):
        raise click.FileError(batch, hint="File not found.")
    with open(batch, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    # Configurations
    yes_override = True if yes else cfg.get("convert_without_ask", False)
    verbose = cfg.get("verbose", 0)
    log_dir = cfg.get("log_dir", None)
    set_log_dir(log_dir)
    # Do jobs
    if "jobs" not in cfg:
        raise click.UsageError("No jobs found in batch file. Please check your file.")
    for job in cfg["jobs"]:
        _convert_job(job, yes_override, verbose, preamble, preamble_text)


def _convert_job(job: Dict, yes: bool, verbose: int, preamble: bool, preamble_text: str):
    # The following options cannot be customized in batch file. (not implemented)
    output_format = "as-is"
    css = ""
    skip_validation = False
    validation_only = False

    # Configurations
    # ^^^^^^^^^^^^^^
    required_keys = ["source", "output_dir", "tag_as"]
    for key in required_keys:
        if key not in job:
            raise click.UsageError(f"No {key} found in job. Please check your file.")

    jname: str = job.get("name", "Unnamed Job")
    source: str = job["source"]
    output_dir: str = job["output_dir"]
    tag_as: str = job["tag_as"]

    # Check
    if not os.path.isdir(output_dir):
        raise click.FileError(output_dir, hint="Directory not found.")
    if tag_as not in ("folder", "suffix"):
        raise click.UsageError("tag_as must be either 'folder' or 'suffix'.")

    # Job start
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log_info(f"\n[{time_str}] Job: {jname}", fg="cyan")

    # Determine source type: file or directory
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    if os.path.isfile(source):
        base_items = collect_bases_from_files([source])
        source_dir = os.path.dirname(source)
    elif os.path.isdir(source):
        recursive = job.get("recursive", True)
        base_items = collect_bases_from_dir(source, recursive)
        source_dir = source
    else:
        raise click.FileError(source, hint="File or directory not found.")

    # Convert items
    # ^^^^^^^^^^^^^
    _convert_items(
        base_items,
        output_format,
        css,
        yes,
        skip_validation,
        validation_only,
        verbose,
        preamble,
        preamble_text,
        source_dir=source_dir,
        output_dir=output_dir,
        tag_as=tag_as,
    )


def _convert_items(
    base_items: Set[FileItem],
    output_format: str,
    css: str,
    yes: bool,
    skip_validation: bool,
    validation_only: bool,
    verbose: int,
    preamble: bool,
    preamble_text: str,
    source_dir: str = ".",
    output_dir: str = ".",
    tag_as: str = "suffix",
):
    if not base_items:
        raise click.UsageError("No base files found.")
    base_count = len(base_items)
    is_plural = base_count > 1

    # Sort and List up
    # ^^^^^^^^^^^^^^^^
    md_backlogs = []  # (item: FileItem, base_doc: List[str], cfg: Config)
    jn_backlogs = []  # (item: FileItem, base_jn: Dict, cfg: Config)
    for item in sorted(base_items, key=lambda x: x.abs_path):
        backlog = _process_file(item)
        if item.extension == "md":
            md_backlogs.append(backlog)
        elif item.extension == "ipynb":
            jn_backlogs.append(backlog)

    # Health Check and Print Log
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^
    log_info("----------------------")
    md_healthy = _health_check_on_backlogs(md_backlogs, "md", "📄", skip_validation, verbose)
    jn_healthy = _health_check_on_backlogs(jn_backlogs, "ipynb", "📒", skip_validation, verbose)
    log_info("----------------------")
    _msg = "s were" if is_plural else " was"
    log_info(f" => {base_count} base file{_msg} found.")

    # Ask for confirmation
    # ^^^^^^^^^^^^^^^^^^^^
    if validation_only:
        if skip_validation:
            log_warn(" => No health check was performed.")
            sys.exit(0)
        elif md_healthy and jn_healthy:
            log_info(" => All files are healthy.", fg="green")
            sys.exit(0)
        else:
            log_error(" => Some files are unhealthy.")
            sys.exit(1)
    if not yes:
        if not query_yes_no("    Do you want to convert these files?"):
            sys.exit(0)

    # Convert
    # ^^^^^^^
    log_info("----------------------", fg="cyan")
    for _backlogs, _convert_func in zip([md_backlogs, jn_backlogs], [convert_base_doc, convert_base_jupyter]):
        _convert_backlogs(
            _backlogs,
            _convert_func,
            output_format,
            css,
            preamble,
            preamble_text,
            source_dir=source_dir,
            output_dir=output_dir,
            tag_as=tag_as,
        )
    log_info("----------------------", fg="cyan")
    _msg = "files have" if is_plural else "file has"
    log_info(f" => {base_count} base {_msg} been converted.\n", fg="cyan")
