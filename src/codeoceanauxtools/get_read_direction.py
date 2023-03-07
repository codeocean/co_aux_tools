#!/usr/bin/env python
import logging
import sys

import utils.util

log = logging.getLogger(__name__)


def main(argv=None):
    if len(argv) == 1:
        sys.exit("You failed to provide a file name")
    return utils.util.get_read_direction(argv[1])


if __name__ == "__main__":
    log.debug(f"args: {sys.argv}")
    print(main(sys.argv))
