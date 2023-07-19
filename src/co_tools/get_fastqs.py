import os
import sys
from typing import Optional

import typer
from typing_extensions import Annotated

from .co_fastq import get_fastqs

if os.environ.get("CO_LOG", "false").lower() == "true":
    from .get_logger import LOGGER

    log = LOGGER
else:
    import logging

    log = logging.getLogger(__name__)


app = typer.Typer()


@app.command()
def main(
    dir: Annotated[
        Optional[str],
        typer.Option(help="The directory to search for fastq files in"),
    ] = "../data",
    fwd: Annotated[
        Optional[bool],
        typer.Option(help="Use this flag to return only the forward reads files"),
    ] = False,
):
    """Find all fastq.gz files in a folder.

    Args:

        dir (str, optional): The directory to search for fastq files in.
        Defaults '../data'

        fwd (bool, optional): Used to return only forward reads files.
        Defaults to --fwd

    Returns:
        newline separated list of absolute paths to fastq.gz files
    """
    log.debug(f"args: {sys.argv}")
    log.debug(f"fwd={fwd}, dir={dir}")
    typer.echo(get_fastqs(fwd=fwd, dir=dir))
