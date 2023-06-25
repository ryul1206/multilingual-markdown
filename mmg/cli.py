from typing import List, Iterator, Dict
from dataclasses import dataclass
import sys
import os
import re
import click
import mmg
from mmg.config import Config, ConfigExtractor
from mmg.health import HealthChecker
from mmg.api import convert


@dataclass
class _BaseFileItem:
    norm_path: str

    @property
    def abs_path(self) -> str:
        return os.path.abspath(self.norm_path)

    def __repr__(self):
        return shorten_path(self.norm_path)

    def __hash__(self) -> int:
        return hash(self.abs_path)


def _print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(f"Version {mmg.__version__}")
    ctx.exit()


def is_base_md(file_name: str) -> bool:
    base = re.compile(r"[.]base[.]md")
    return base.search(file_name) is not None


def filter_base_md(file_names: List[str]) -> Iterator[_BaseFileItem]:
    for file_name in file_names:
        if is_base_md(file_name):
            # Resolve a PowerShell bug related to file paths with specific names
            # `mmg` will throw an error when the file_name starts with ".\" or "./".
            if file_name.startswith(".\\") or file_name.startswith("./"):
                file_name = file_name[2:]
            file_path = os.path.join(".", file_name)
            norm_path = os.path.normpath(file_path)
            yield _BaseFileItem(norm_path)


def walk_base_md(path: str) -> Iterator[_BaseFileItem]:
    for path, _, files in os.walk(path):
        for file_name in files:
            if is_base_md(file_name):
                file_path = os.path.join(path, file_name)
                norm_path = os.path.normpath(file_path)
                yield _BaseFileItem(norm_path)


def shorten_path(path: str, max_length: int = 50) -> str:
    """Shorten the path to a given length.
    https://stackoverflow.com/questions/74300488/pretty-printing-of-paths-in-python

    Args:
        path (str): The path to shorten.
        max_length (int, optional): The maximum length of the path. Defaults to 20.

    Returns:
        str: The shortened path.
    """
    if len(path) < max_length:
        return path  # no need to shorten

    shortened_path = "..."  # add middle item
    paths_to_choose_from = path.split(os.sep)  # split by your custom OS separator. "/" for linux, "\" for windows.
    add_last_path = True
    while len(shortened_path) < max_length:
        if len(paths_to_choose_from) == 0:
            return shortened_path
        if add_last_path:
            shortened_path = shortened_path.replace("...", f"...{os.sep}{paths_to_choose_from[-1]}")
            del paths_to_choose_from[-1]  # delete elem used
            add_last_path = False
        else:
            shortened_path = shortened_path.replace("...", f"{paths_to_choose_from[0]}{os.sep}...")
            del paths_to_choose_from[0]  # delete elem used
            add_last_path = True
    return shortened_path


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


@click.command()
@click.argument("file_names", nargs=-1, type=click.Path(exists=True))
@click.option(
    "-r", "--recursive", is_flag=True, default=False, help="This will search all subfolders based on current directory."
)
@click.option(
    "-y", "--yes", is_flag=True, default=False, help="This will confirm the conversion without asking. (Default: False)"
)
@click.option("-s", "--skip-validation", is_flag=True, default=False, help="Skip the health check. (Default: False)")
@click.option("--validation-only", is_flag=True, default=False, help="Only check the health. (Default: False)")
@click.option("-v", "--verbose", count=True, help="Verbosity level from 0 to 2. --verbose:1, -v:1, -vv:2 (Default: 0)")
@click.option(
    "--version", is_flag=True, callback=_print_version, expose_value=False, is_eager=True, help="Show the current version."
)
def mmgcli(file_names: List[str], recursive: bool, yes: bool, skip_validation: bool, validation_only: bool, verbose: int):
    # Check arguments
    # ^^^^^^^^^^^^^^^
    if not file_names and not recursive:
        raise click.UsageError("You have not entered anything. Try `mmg Foo.base.md` or `mmg --recursive`.")

    # Get base files
    # ^^^^^^^^^^^^^^
    # Collect base files
    base_items: set[_BaseFileItem] = set()  # use set to avoid duplicates
    if file_names:
        for item in filter_base_md(file_names):
            base_items.add(item)
    if recursive:
        for item in walk_base_md("."):
            base_items.add(item)
    if not base_items:
        raise click.UsageError("No base files found.")
    # Count base files
    base_count = len(base_items)
    is_plural = base_count > 1
    # Sort and List up
    backlogs = []
    for item in sorted(base_items, key=lambda x: x.abs_path):
        if not os.path.isfile(item.norm_path):
            raise click.UsageError(f"File not found: {item.abs_path}")
        # Read the base file
        with open(item.norm_path, "r", encoding="utf-8") as f:
            base_md: str = f.read()
        base_doc: List[str] = base_md.splitlines()
        # Extract config
        cfg: Config = ConfigExtractor.extract(base_doc)
        # Add to backlogs
        backlogs.append((item, base_md, base_doc, cfg))

    # Health Check and Print Log
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^
    all_healthy = True
    click.echo("----------------------")
    for item, _, base_doc, cfg in backlogs:
        if skip_validation:
            click.echo(f" 📄 {repr(item)}")
        else:
            # Health check
            hc = HealthChecker()
            hc.health_check(base_doc, cfg=cfg)
            if not hc.is_healthy:
                all_healthy = False
            # Print log
            log = hc.cli_log(file_name=repr(item), verbosity=verbose)
            click.echo(log)
    click.echo("----------------------")
    _msg = "markdowns were" if is_plural else "markdown was"
    click.echo(f" => {base_count} base {_msg} found.")

    # Ask for confirmation
    # ^^^^^^^^^^^^^^^^^^^^
    if validation_only:
        if skip_validation:
            click.secho(" => No health check was performed.", fg="yellow")
            sys.exit(0)
        if all_healthy:
            click.secho(" => All files are healthy.", fg="green")
            sys.exit(0)
        else:
            click.secho(" => Some files are unhealthy.", fg="red")
            sys.exit(1)
    if not yes:
        if not query_yes_no("    Do you want to convert these files?"):
            sys.exit(0)

    # Convert
    # ^^^^^^^
    click.secho("----------------------", fg="cyan")
    for item, base_md, _, cfg in backlogs:
        # Convert
        target_docs: Dict[str, List[str]] = convert(base_md, skip_health_check=True)
        click.secho(f" {repr(item)}", fg="cyan")
        # Save with log
        for lang, md in target_docs.items():
            # target
            suffix = f".{lang}." if lang != cfg.no_suffix else "."
            target_item = _BaseFileItem(item.norm_path.replace(".base.", suffix))
            # save
            with open(target_item.norm_path, "w", encoding="utf-8") as f:
                f.write("\n".join(md))
            # log
            click.echo(f"\t{lang}: {repr(target_item)}")
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
