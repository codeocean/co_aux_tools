#!/usr/bin/env python
import sys

# local imports
import co_utils
from codeoceanauxtools.get_logger import LOGGER


def main(argv=None):
    if len(argv) == 1:
        sys.exit("You failed to provide a log message")
    elif len(argv) == 2:
        return co_utils.print_log_msg(argv[1])
    return co_utils.print_log_msg(argv[1], argv[2])


if __name__ == "__main__":
    LOGGER.debug(f"args: {sys.argv}")
    print(main(sys.argv))
