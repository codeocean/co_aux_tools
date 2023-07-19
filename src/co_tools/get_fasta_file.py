import os
import sys
from typing import Optional

import typer
from typing_extensions import Annotated

from .co_fasta import find_fasta_file

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
    ] = "../data"
):
    """Return the path to a fasta file. Will randomly return a fasta file if
    more than 1 found in the search directory.

    Args:
        dir : The directory to search for fasta files in.
    """
    log.debug(f"args: {sys.argv}")
    typer.echo(find_fasta_file(input_path=dir))
