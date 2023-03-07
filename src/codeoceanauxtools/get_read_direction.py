#!/usr/bin/env python
import sys

from get_logger import LOGGER
import util


def main(argv=None):
    if len(argv) == 1:
        sys.exit("You failed to provide a file name")
    return util.get_read_direction(argv[1])


if __name__ == "__main__":
    LOGGER.debug(f"args: {sys.argv}")
    print(main(sys.argv))