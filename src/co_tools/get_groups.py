#!/usr/bin/env python
import os
import sys
from typing import Optional

import typer
from typing_extensions import Annotated

from .co_utils import get_groups

if os.environ.get("CO_LOG", "false").lower() == "true":
    from .get_logger import LOGGER

    log = LOGGER
else:
    import logging

    log = logging.getLogger(__name__)


app = typer.Typer()


@app.command()
def main(
    filename: Annotated[
        Optional[str],
        typer.Option(
            help="The name of the sample sheet file to search for. "
            + "If this flag is a path to a file that exists, then that "
            + "file will be used"
        ),
    ] = "../data/sample_sheet.csv",
    dir: Annotated[
        Optional[str],
        typer.Option(help="The directory to search in for the sample sheet file"),
    ] = "../data",
):
    """Return all the groups from a sample_sheet.csv file as a comma separated
    string in alphabetical order.

    Args:

        filename : The name of the sample sheet file to search for. If this
        flag is a path to a file that exists, then that file will be used
        Defaults to "../data/sample_sheet.csv"

        dir : The directory to search in for the sample sheet file
        Defaults to "../data"
    """
    log.debug(f"args: {sys.argv}")
    typer.echo(get_groups(filename=filename, dir=dir))
