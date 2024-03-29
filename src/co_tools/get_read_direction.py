#!/usr/bin/env python
import os
import sys

import typer
from typing_extensions import Annotated

from co_tools.co_fastq import get_read_direction
from co_tools.co_utils import LOG_LEVELS

if os.environ.get("CO_LOG_LEVEL", "false").lower() in LOG_LEVELS:
    from co_tools.get_logger import LOGGER as log
else:
    import logging

    log = logging.getLogger(__name__)


app = typer.Typer()


@app.command()
def main(file: Annotated[str, typer.Argument()]):
    """Returns '1' if the file is detected as a forward reads file.
    Returns '2' otherwise.

    Args:
        file: The name of the file to determine the read direction of.
        This can be a path to a file.
    """
    log.debug(f"args: {sys.argv}")
    typer.echo(get_read_direction(filepath=file))
