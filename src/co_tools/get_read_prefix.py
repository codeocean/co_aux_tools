import os
import sys
from typing import Optional

import typer
from typing_extensions import Annotated

from .co_fastq import get_prefix

if os.environ.get("CO_LOG", "false").lower() == "true":
    from .get_logger import LOGGER

    log = LOGGER
else:
    import logging

    log = logging.getLogger(__name__)


app = typer.Typer()


@app.command()
def main(
    file: Annotated[
        str,
        typer.Argument(
            help="The filename or path to a file to determine the pattern from"
        ),
    ],
    split_pos: Annotated[
        Optional[int],
        typer.Option(
            help="The number of trailing text fileds denoted by splitting on "
            + "'_' to remove"
        ),
    ] = 1,
):
    """Returns the pattern in the filenames shared between a pair of
    complementary paired-end reads files.

    Args:

        file : The filename or path to a file to determine the prefix from

        split_pos : The number of trailing text fields denoted by splitting
        on '_' to remove.
        Defaults to 1
    """
    log.debug(f"args: {sys.argv}")
    split_pos = int(split_pos) * -1
    log.debug(f"split_pos={split_pos}")
    typer.echo(get_prefix(filename=file, split_position=str(split_pos)))
