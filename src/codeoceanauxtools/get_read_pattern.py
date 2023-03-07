#!/usr/bin/env python
import sys

from get_logger import LOGGER
import utils.util


def main(argv=None):
    if len(argv) == 1:
        LOGGER.error("You failed to provide a filename and direction")
        sys.exit("You failed to provide a filename and direction")
    elif len(argv) == 2:
        return utils.util.get_read_pattern(argv[1])
    return utils.util.get_read_pattern(argv[1], argv[2])


if __name__ == "__main__":
    LOGGER.debug(f"args: {sys.argv}")
    print(main(sys.argv))
