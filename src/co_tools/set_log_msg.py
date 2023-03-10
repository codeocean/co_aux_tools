#!/usr/bin/env python
import sys

# local imports
from co_tools.co_utils import print_log_msg
from co_tools.get_logger import LOGGER


def main(argv=sys.argv):
    if len(argv) == 1:
        LOGGER.error("You failed to provide a log message")
        sys.exit("You failed to provide a log message")
    elif len(argv) == 2:
        return print_log_msg(argv[1])
    return print_log_msg(argv[1], argv[2])


if __name__ == "__main__":
    LOGGER.debug(f"args: {sys.argv}")
    sys.exit(main(sys.argv))
