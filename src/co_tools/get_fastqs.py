import os
import sys
from typing import Optional

import typer
from typing_extensions import Annotated

from co_tools.co_fastq import get_fastqs
from co_tools.co_utils import LOG_LEVELS

if os.environ.get("CO_LOG_LEVEL", "false").lower() in LOG_LEVELS:
    from co_tools.get_logger import LOGGER as log
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
