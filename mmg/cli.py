from typing import List
import sys
import click
import mmg
from mmg.cli_process import convert_cli_args, convert_batch
from mmg.cli_log import log_error, log_info


def _print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    log_info(f"Version {mmg.__version__}")
    ctx.exit()


@click.command()
# Designate files ############################################################
@click.argument("file_names", nargs=-1, type=click.Path(exists=True, dir_okay=False))
@click.option(
    "-r",
    "--recursive",
    is_flag=True,
    default=False,
    help="This will search all subfolders based on current directory.",
)
@click.option(
    "-b",
    "--batch",
    type=click.Path(exists=True, dir_okay=False),
    default=None,
    help="YAML file path for batch conversion. (Default: None)",
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
    help="CSS file path or preset('github-light'/'github-dark'). Only for the HTML/PDF output. (Default: github-light)",
)
# CLI options #################################################################
@click.option(
    "-y",
    "--yes",
    is_flag=True,
    default=False,
    help="This will confirm the conversion without asking. (Default: False)",
)
@click.option(
    "-s",
    "--skip-validation",
    is_flag=True,
    default=False,
    help="Skip the health check. (Default: False)",
)
@click.option(
    "--validation-only",
    is_flag=True,
    default=False,
    help="Only check the health. (Default: False)",
)
@click.option(
    "-v",
    "--verbose",
    count=True,
    help="Verbosity level from 0 to 2. --verbose:1, -v:1, -vv:2 (Default: 0)",
)
# Others ######################################################################
@click.option(
    "--version",
    is_flag=True,
    callback=_print_version,
    expose_value=False,
    is_eager=True,
    help="Show the current version.",
)
def mmgcli(
    file_names: List[str],
    recursive: bool,
    batch: str,
    output_format: str,
    css: str,
    yes: bool,
    skip_validation: bool,
    validation_only: bool,
    verbose: int,
):
    """
    FILE_NAMES: Base file names to convert. `*.base.md` or `*.base.ipynb` are available.

    Here are some examples:

        mmg *.base.md

        mmg *.base.ipynb

        mmg *.base.md *.base.ipynb -o pdf --css github-dark

        mmg --recursive

        mmg --recursive --validation-only

        mmg --batch mmg.yml
    """
    if file_names or recursive:
        convert_cli_args(
            file_names,
            recursive,
            output_format,
            css,
            yes,
            skip_validation,
            validation_only,
            verbose,
        )
    elif batch:
        convert_batch(batch)
    else:
        raise click.UsageError(
            "No arguments found. Try one of the following:\n\
            \n\tmmg *.base.md\
            \n\tmmg *.base.ipynb\
            \n\tmmg -r\
            \n\tmmg -b batch.yml\
            \n\tmmg --help\n"
        )
    return


def main():
    assert sys.version_info[0] == 3
    try:
        mmgcli()
    except Exception as e:
        log_error(e)
