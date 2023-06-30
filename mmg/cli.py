from typing import List, Dict, Tuple, Callable
import sys
import os
import json
import click
import mmg
from mmg.config import Config, ConfigExtractor, extract_config_from_jupyter
from mmg.health import HealthChecker
from mmg.api import convert_base_doc, convert_base_jupyter
from mmg.base_item import FileItem, collect_base_files
from mmg import output


def _print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(f"Version {mmg.__version__}")
    ctx.exit()


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
            cfg: Config = ConfigExtractor.extract(base_doc)
            return (item, base_doc, cfg)
        elif item.extension == "ipynb":
            base_jn: Dict = json.load(f)
            cfg: Config = extract_config_from_jupyter(base_jn)
            return (item, base_jn, cfg)


def _health_check_on_backlogs(backlogs: Tuple, extension: str, emoji: str, skip_validation: bool, verbose: int) -> bool:
    all_healthy = True
    for item, base, cfg in backlogs:
        if skip_validation:
            click.echo(f" {emoji} {repr(item)}")
        else:
            # Health check
            hc = HealthChecker()
            hc.health_check(base, cfg=cfg, extension=extension)
            if not hc.is_healthy:
                all_healthy = False
            # Print log
            log = hc.cli_log(file_name=repr(item), verbosity=verbose)
            click.echo("\n".join(log))
    return all_healthy


def _convert_backlogs(backlogs: List, convert_func: Callable, output_format: str, css: str):
    for base_item, base, cfg in backlogs:
        # Convert
        target_docs = convert_func(base, skip_health_check=True)
        click.secho(f" {repr(base_item)}", fg="cyan")
        # Save with log
        for lang, content in target_docs.items():
            """
            lang: str (e.g. "en-US")
            content: List[str] (for markdown) or Dict (for jupyter notebook)
            """
            # target
            suffix = f".{lang}." if lang != cfg.no_suffix else "."
            # save
            if output_format == "as-is":
                target_item = output.handle_as_is(base_item, suffix, content)
            else:
                target_item = output.handle_html_or_pdf(base_item, suffix, output_format, css, content)
            # log
            click.echo(f"\t{lang}: {repr(target_item)}")


def perform_exit(message: str, fg: str, code: int):
    click.secho(message, fg=fg)
    sys.exit(code)


@click.command()
# Designate files ############################################################
@click.argument("file_names", nargs=-1, type=click.Path(exists=True))
@click.option(
    "-r", "--recursive", is_flag=True, default=False, help="This will search all subfolders based on current directory."
)
# Output format ##############################################################
@click.option(
    "-o",
    "--output-format",
    type=click.Choice(["as-is", "html", "pdf"]),
    default="as-is",
    help="Output format. (Default: as-is)",
)
@click.option(
    "--css",
    type=str,
    default="github-light",
    help="CSS file path or preset ('github-light'/'github-dark'). Only for Markdown to HTML/PDF. (Default: github-light)",
)
# CLI options #################################################################
@click.option(
    "-y", "--yes", is_flag=True, default=False, help="This will confirm the conversion without asking. (Default: False)"
)
@click.option("-s", "--skip-validation", is_flag=True, default=False, help="Skip the health check. (Default: False)")
@click.option("--validation-only", is_flag=True, default=False, help="Only check the health. (Default: False)")
@click.option("-v", "--verbose", count=True, help="Verbosity level from 0 to 2. --verbose:1, -v:1, -vv:2 (Default: 0)")
# Others ######################################################################
@click.option(
    "--version", is_flag=True, callback=_print_version, expose_value=False, is_eager=True, help="Show the current version."
)
def mmgcli(
    file_names: List[str],
    recursive: bool,
    output_format: str,
    css: str,
    yes: bool,
    skip_validation: bool,
    validation_only: bool,
    verbose: int,
):
    # Check arguments
    # ^^^^^^^^^^^^^^^
    if not file_names and not recursive:
        raise click.UsageError("You have not entered anything. Try `mmg Foo.base.md` or `mmg --recursive`.")

    # Get base files
    # ^^^^^^^^^^^^^^
    base_items = collect_base_files(file_names, recursive)
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
    click.echo("----------------------")
    md_healthy = _health_check_on_backlogs(md_backlogs, "md", "📄", skip_validation, verbose)
    jn_healthy = _health_check_on_backlogs(jn_backlogs, "ipynb", "📒", skip_validation, verbose)
    click.echo("----------------------")
    _msg = "markdowns were" if is_plural else "markdown was"
    click.echo(f" => {base_count} base {_msg} found.")

    # Ask for confirmation
    # ^^^^^^^^^^^^^^^^^^^^
    if validation_only:
        if skip_validation:
            perform_exit(" => No health check was performed.", fg="yellow", code=0)
        elif (md_healthy and jn_healthy):
            perform_exit(" => All files are healthy.", fg="green", code=0)
        else:
            perform_exit(" => Some files are unhealthy.", fg="red", code=1)
    if not yes:
        if not query_yes_no("    Do you want to convert these files?"):
            sys.exit(0)

    # Convert
    # ^^^^^^^
    click.secho("----------------------", fg="cyan")
    _convert_backlogs(md_backlogs, convert_base_doc, output_format, css)
    _convert_backlogs(jn_backlogs, convert_base_jupyter, output_format, css)
    click.secho("----------------------", fg="cyan")
    _msg = "files have" if is_plural else "file has"
    click.secho(f" => {base_count} base {_msg} been converted.\n", fg="cyan")
    return


def main():
    assert sys.version_info[0] == 3
    try:
        mmgcli()
    except Exception as e:
        click.echo(e)
