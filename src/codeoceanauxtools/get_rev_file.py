#!/usr/bin/env python
import logging
import sys

import utils.util

log = logging.getLogger(__name__)


def main():
    if len(sys.argv) == 1:
        sys.exit("You failed to provide a filename")
    log.debug(f"args: {sys.argv}")
    return utils.util.get_rev_file(sys.argv[1])


if __name__ == "__main__":
    print(main())
