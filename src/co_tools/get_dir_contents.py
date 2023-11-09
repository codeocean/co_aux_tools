import os
import sys
from typing import Optional

import typer
from typing_extensions import Annotated

from co_tools.co_utils import get_dir_contents
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
        Optional[str], typer.Option(help="The directory to list the contents of")
    ] = "../data"
):
    """List all the files and folders in a a particular directory at a given point in your code

    Args:
        dir : The directory to list the contents of.
    """
    log.debug(f"args: {sys.argv}")
    typer.echo(
        f"*** These are the current files in the {dir} directory\n"
        + f"{get_dir_contents(dir)}"
    )
