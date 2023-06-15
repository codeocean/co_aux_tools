#!/usr/bin/env python
import os
import sys

from .co_fastq import get_prefix

if os.getenv("CO_LOG").lower() == "true":
    from .get_logger import LOGGER

    log = LOGGER
else:
    import logging

    log = logging.getLogger(__name__)


def main(argv=sys.argv):
    log.debug(f"args: {sys.argv}")
    if len(argv) == 1:
        sys.exit(log.error("You failed to provide a filename"))
    elif len(argv) == 2:
        print(get_prefix(argv[1]))
        return 0
    print(get_prefix(argv[1], argv[2]))
    return 0


if __name__ == "__main__":
    log.debug(f"args: {sys.argv}")
    sys.exit(main(sys.argv))
