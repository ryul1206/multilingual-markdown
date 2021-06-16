#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import click
from mmgcli import cli


if __name__ == "__main__":
    assert sys.version_info[0] == 3
    try:
        cli.main()
    except Exception as e:
        click.echo(e)
