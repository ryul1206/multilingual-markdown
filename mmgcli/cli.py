#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import re
import click
import mmgcli
from mmgcli.base_parser import MultilingualDoc


def is_base_md(filename):
    base = re.compile(r"[.]base[.]md")
    return base.search(filename)


def search(dir_name):
    for path, folder, files in os.walk(dir_name):
        for file_name in files:
            if is_base_md(file_name):
                yield (path, file_name)


def filtered_base_list(filelist):
    for filename in filelist:
        if is_base_md(filename):
            yield filename


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(f'Version {mmgcli.__version__}')
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
        # sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")
    return resp


def load_files(filenames, recursive, check, verbosity):
    base_files = []
    if recursive:
        for path, filename in search("."):
            base_files.append(MultilingualDoc(path, filename))
    if filenames:
        for filename in filtered_base_list(filenames):
            base_files.append(MultilingualDoc(".", filename))

    base_count = len(base_files)
    if base_count == 0:
        click.echo("The base file does not exist.")
        exit()

    click.echo("----------------------")
    for base in base_files:
        icon, _msg, color = base.check_log(verbosity=verbosity) if check else ("+", "", "white")
        click.secho(f" {icon} {base.full_name}", fg=color)
        if _msg:
            click.echo(_msg)
    click.echo("----------------------")
    is_plural = base_count > 1
    _msg = "markdowns were" if is_plural else "markdown was"
    click.echo(f" => {base_count} base {_msg} found.")
    if verbosity == 0:
        click.echo("    Your verbosity is 0. Try the `--verbose` option for more details.")
    return base_files


@click.command()
@click.option(
    "--version",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
    help='Show the current version.')
@click.argument("filenames", nargs=-1, type=click.Path(exists=True))
@click.option(
    "--recursive", "-r",
    is_flag=True,
    default=False,
    help='This recursive option searches all subfolders based on current directory'
         ' and converts all base files.',
)
@click.option(
    "--yes", "-y",
    is_flag=True,
    default=False,
    help='Confirm the action without prompting',
)
@click.option(
    "--check/--skip", "-c/-s",
    default=True,
    help='Check the number of language tags of each file (defualt: --check)',
)
@click.option('-v', '--verbose', count=True, help="For example, -v:1, -vv:2")
def main(filenames, recursive, yes, check, verbose):
    if recursive or filenames:
        base_files = load_files(filenames, recursive, check, verbose)
        base_count = len(base_files)
        is_plural = base_count > 1

        _msg = "files have" if is_plural else "file has"
        if not yes:
            if not query_yes_no("Do you want to convert these files?"):
                exit()

        click.secho("----------------------", fg="cyan")
        for base in base_files:
            base.run()
        click.secho("----------------------", fg="cyan")

        click.secho(f" => {base_count} base {_msg} been converted.\n", fg="cyan")
    else:
        raise click.UsageError(
            "You have not entered anything. Do 'mmg Foo.base.md' or 'mmg --recursive'."
        )
