import os
import sys
from typing import Optional

import typer
from typing_extensions import Annotated

from co_tools.co_fastq import get_read_pattern
from co_tools.co_utils import LOG_LEVELS

if os.environ.get("CO_LOG_LEVEL", "false").lower() in LOG_LEVELS:
    from co_tools.get_logger import LOGGER as log
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
    fwd: Annotated[
        Optional[bool],
        typer.Option(
            "--fwd/--rev",
            help="Use this flag to return the forward or reverse reads files",
        ),
    ] = True,
):
    """Returns the pattern in the filename that is shared with all sequencing
    files for a given direction based on the --fwd or --rev flags.
    e.g. 'gsm123_456_R1.fastq.gz' will return 'R1.fastq.gz'

    Args:

        file : The filename or path to a file to determine the pattern from

        --fwd : Use this flag to return the forward reads file pattern

        --rev : Use this flag to return the reverse reads file pattern
    """
    log.debug(f"args: {sys.argv}")
    direction = "1" if fwd else "2"
    typer.echo(get_read_pattern(filename=file, direction=direction))
