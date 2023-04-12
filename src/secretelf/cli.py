# SPDX-FileCopyrightText: 2023-present Sylvain Bellemare <sbellem@gmail.com>
#
# SPDX-License-Identifier: MIT

# Based on https://github.com/ofek/hatch-showcase/blob/master/src/hatch_showcase/cli/__init__.py

import click

from secretelf import iaskeys as _iaskeys
from secretelf._version import version


@click.version_option(version=version, prog_name="secretelf")
@click.group()
def secretelf():
    pass


@click.argument("binary", type=str)
@secretelf.command()
def iaskeys(binary: str):
    api_key, spid = _iaskeys.extract(binary)
    click.echo(f"API KEY: \t{api_key.decode()}")
    click.echo(f"SPID: \t\t{spid.decode()}")
