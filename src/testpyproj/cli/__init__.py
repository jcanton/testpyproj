# SPDX-FileCopyrightText: 2025-present Jacopo <jacopo.canton@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from testpyproj.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="testpyproj")
def testpyproj():
    click.echo("Hello world!")
