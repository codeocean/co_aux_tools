#!/usr/bin/env python
import sys

from .co_fastq import get_read_direction
# local imports
from .get_logger import LOGGER


def main(argv=sys.argv):
    LOGGER.debug(f"args: {sys.argv}")
    if len(argv) == 1:
        sys.exit("You failed to provide a file name")
    print(get_read_direction(argv[1]))
    return 0


if __name__ == "__main__":
    LOGGER.debug(f"args: {sys.argv}")
    sys.exit(main(argv=sys.argv))
