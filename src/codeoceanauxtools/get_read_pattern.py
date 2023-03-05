#!/usr/bin/env python
import logging
import sys

import utils.util

log = logging.getLogger(__name__)


def main():
    log.debug(f"args: {sys.argv}")
    if len(sys.argv) == 1:
        sys.exit("You failed to provide a filename and direction")
    elif len(sys.argv) == 2:
        return utils.util.get_read_pattern(sys.argv[1])
    return utils.util.get_read_pattern(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    print(main())
