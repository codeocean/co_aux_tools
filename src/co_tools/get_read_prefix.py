#!/usr/bin/env python
import sys

# local imports
from co_tools.co_logger.get_logger import LOGGER
from co_tools.co_fastq import get_prefix


def main(argv=sys.argv):
    LOGGER.debug(f"args: {sys.argv}")
    if len(argv) == 1:
        LOGGER.error("You failed to provide a filename")
        sys.exit("You failed to provide a filename")
    elif len(argv) == 2:
        print(get_prefix(argv[1]))
        return 0
    print(get_prefix(argv[1], argv[2]))
    return 0


if __name__ == "__main__":
    LOGGER.debug(f"args: {sys.argv}")
    sys.exit(main(sys.argv))
