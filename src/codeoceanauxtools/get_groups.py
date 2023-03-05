#!/usr/bin/env python
import logging
import sys

import utils.util

log = logging.getLogger(__name__)


def main():
    if len(sys.argv) > 1:
        log.debug(f"args: {sys.argv}")
        return utils.util.get_groups(sys.argv[1])
    return utils.util.get_groups()


if __name__ == "__main__":
    print(main())
