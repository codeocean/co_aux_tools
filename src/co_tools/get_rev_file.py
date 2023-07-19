import os
import sys
from typing import Optional

import typer
from typing_extensions import Annotated

from .co_fastq import get_rev_file

if os.environ.get("CO_LOG", "false").lower() == "true":
    from .get_logger import LOGGER

    log = LOGGER
else:
    import logging

    log = logging.getLogger(__name__)


app = typer.Typer()


@app.command()
def main(
    fwd_file: Annotated[
        str,
        typer.Argument(
            help="The filename or path to a file to determine the reverse "
            + "filename from."
        ),
    ],
    name_only: Annotated[
        Optional[bool],
        typer.Option(help="Use this flag to return the filename only"),
    ] = False,
    pattern_fwd: Annotated[
        Optional[str],
        typer.Option(help="The forward pattern to replace."),
    ] = None,
    pattern_rev: Annotated[
        Optional[str],
        typer.Option(help="The reverse pattern that will replace the forward pattern."),
    ] = None,
):
    """Returns the reverse paired-end reads file of an input forward reads file

    Args:

        fwd_file : The filename or path to a file to determine the reverse filename from.

        name_only : Use this flag to return the filename only
        Defaults to False

        pattern_fwd : The forward pattern to replace.
        Defaults to None

        pattern_rev : The reverse pattern that will replace the forward pattern.
        Defaults to None
    """
    log.debug(f"args: {sys.argv}")
    if (pattern_fwd and not pattern_rev) or (not pattern_fwd and pattern_rev):
        raise typer.Exit(
            "You cannot use only one of the --pattern-fwd or --pattern-rev "
            + "flage. You must use both the --pattern-fwd and --pattern-rev "
            + "flags or use neither."
        )
    typer.echo(
        get_rev_file(
            fwd_file=fwd_file,
            name_only=name_only,
            pattern_fwd=pattern_fwd,
            pattern_rev=pattern_rev,
        )
    )
