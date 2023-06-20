#!/usr/bin/env python
import os
import sys

from .co_fastq import get_fastq_pair

if os.environ.get("CO_LOG", "false").lower() == "true":
    from .get_logger import LOGGER

    log = LOGGER
else:
    import logging

    log = logging.getLogger(__name__)


def main(argv=sys.argv):
    log.debug(f"args: {sys.argv}")
    if len(argv) > 1:
        print(get_fastq_pair(argv[1]))
        return 0
    print(get_fastq_pair())
    return 0


if __name__ == "__main__":
    log.debug(f"args: {sys.argv}")
    sys.exit(main(sys.argv))
