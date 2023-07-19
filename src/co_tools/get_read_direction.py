#!/usr/bin/env python
import os
import sys

import typer
from typing_extensions import Annotated

from .co_fastq import get_read_direction

if os.environ.get("CO_LOG", "false").lower() == "true":
    from .get_logger import LOGGER

    log = LOGGER
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
