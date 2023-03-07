#!/usr/bin/env python
import logging
import sys

import utils.util

log = logging.getLogger(__name__)


def main(argv=None):
    if len(argv) > 1:
        return utils.util.get_groups(argv[1])
    return utils.util.get_groups()


if __name__ == "__main__":
    log.debug(f"args: {sys.argv}")
    print(main(sys.argv))
