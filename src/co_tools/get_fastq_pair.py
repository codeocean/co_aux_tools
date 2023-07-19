#!/usr/bin/env python
import os
import sys
from typing import Optional

import typer
from typing_extensions import Annotated

from .co_fastq import get_fastq_pair

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
        typer.Option(
            help="The directory to search in for complementary pair of fastq.gz files"
        ),
    ] = "../data"
):
    """When working with paired-end sequencing files in Code Ocean pipelines
    you need to send the input capsule 1 forward reads file at-a-time and also
    use the 'collect' option on a 2nd mapping to also give the input capsule
    access to every sequencing file. This function will determine the prefix
    of the single forward reads file and then find the complementary pair
    in the folder with all the sequencing files to return this pair as a
    comma separated string.

    Args:
        dir : The directory to search in for complementary pair of fastq.gz files
    """
    log.debug(f"args: {sys.argv}")
    log.debug(f"dir={dir}")
    typer.echo(get_fastq_pair(dir_path=dir))
