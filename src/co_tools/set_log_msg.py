#!/usr/bin/env python
import os
from typing import Optional

import typer
from typing_extensions import Annotated

from .co_utils import print_log_msg

if os.environ.get("CO_LOG", "false").lower() == "true":
    from .get_logger import LOGGER

    log = LOGGER
else:
    import logging

    log = logging.getLogger(__name__)


app = typer.Typer()


@app.command()
def main(
    msg: Annotated[
        str,
        typer.Argument(help="The message to log"),
    ],
    log_level: Annotated[
        Optional[str],
        typer.Option(help="The log level for this log message."),
    ] = "warning",
):
    """Create a log message in the Code Ocean log which will be located in a
    folder called 'co_logs' which is in the results folder. The name of the
    log file will be the computation ID when in a capsule or the AWS Batch
    Job ID when in a pipeline.

    Args:

        msg : The message to log

        log_level : The log level for this log message.
        Defaults to "warning"

    Returns:
        Nothing is returned to the terminal
    """
    typer.echo(print_log_msg(msg=msg, level=log_level))
