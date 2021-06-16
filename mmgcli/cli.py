#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
import os
import re
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


@click.command()
@click.argument("filenames", nargs=-1, type=click.Path(exists=True))
@click.option(
    "-r",
    "--recursive",
    is_flag=True,
    help='This recursive option searches all subfolders based on current directory'
         ' and converts all base files.',
)
def main(filenames, recursive):
    if recursive or filenames:
        base_count = 0
        click.secho("----------------------", fg="cyan")
        if recursive:
            for path, filename in search("."):
                MultilingualDoc(path, filename)
                base_count += 1
        if filenames:
            for filename in filtered_base_list(filenames):
                MultilingualDoc(".", filename)
                base_count += 1
        click.secho("----------------------", fg="cyan")
        is_plural = base_count > 1
        message = "markdowns were" if is_plural else "markdown was"
        click.secho(f" => {base_count} base {message} converted.\n", fg="cyan")
    else:
        raise click.UsageError(
            "You have not entered anything. Do 'mmg Foo.base.md' or 'mmg --recursive'."
        )
