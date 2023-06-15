#!/usr/bin/env python
import os
import sys

from .co_utils import print_log_msg

if os.getenv("CO_LOG").lower() == "true":
    from .get_logger import LOGGER

    log = LOGGER
else:
    import logging

    log = logging.getLogger(__name__)


def main(argv=sys.argv):
    if len(argv) == 1:
        sys.exit(log.error("You failed to provide a log message"))
    elif len(argv) == 2:
        return print_log_msg(argv[1])
    return print_log_msg(argv[1], argv[2])


if __name__ == "__main__":
    log.debug(f"args: {sys.argv}")
    sys.exit(main(sys.argv))
