import os
import sys
from typing import Optional

import typer
from typing_extensions import Annotated

from .co_utils import get_dir_contents

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
