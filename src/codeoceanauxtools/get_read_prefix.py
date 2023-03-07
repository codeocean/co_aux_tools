#!/usr/bin/env python
import logging
import re
import sys
from pathlib import Path

import utils.util

log = logging.getLogger(__name__)


def main(argv=None):
    if len(argv) == 1:
        log.error("You failed to provide a filename")
        sys.exit("You failed to provide a filename")
    elif len(argv) == 2:
        return utils.util.get_prefix(argv[1])
    return utils.util.get_prefix(argv[1], argv[2])


if __name__ == "__main__":
    log.debug(f"args: {sys.argv}")
    print(main(sys.argv))
