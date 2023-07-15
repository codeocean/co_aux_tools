#!/usr/bin/env python
import os
import sys

from .co_fastq import get_fastqs

if os.environ.get("CO_LOG", "false").lower() == "true":
    from .get_logger import LOGGER

    log = LOGGER
else:
    import logging

    log = logging.getLogger(__name__)


def main(argv=sys.argv):
    log.debug(f"args: {sys.argv}")
    if len(argv) > 2:
        log.info(f"Searching in {argv[2]} dir for files. fwd={argv[1]}")
        print(get_fastqs(argv[1], argv[2]))
        return 0
    elif len(argv) > 1:
        log.info(f"Searching in default dir for files. fwd={argv[1]}")
        print(get_fastqs(argv[1]))
        return 0
    else:
        log.info("Searching in default dir for complementary files")
        print(get_fastqs())
        return 0


if __name__ == "__main__":
    log.debug(f"args: {sys.argv}")
    sys.exit(main(sys.argv))
