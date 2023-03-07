#!/usr/bin/env python
import re
import sys
from pathlib import Path

from get_logger import LOGGER
import util


def main(argv=None):
    if len(argv) == 1:
        LOGGER.error("You failed to provide a filename")
        sys.exit("You failed to provide a filename")
    elif len(argv) == 2:
        return util.get_prefix(argv[1])
    return util.get_prefix(argv[1], argv[2])


if __name__ == "__main__":
    LOGGER.debug(f"args: {sys.argv}")
    print(main(sys.argv))
