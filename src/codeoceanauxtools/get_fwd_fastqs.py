#!/usr/bin/env python
import logging
import sys

import utils.util

log = logging.getLogger(__name__)


def main(argv=None):
    if len(argv) > 1:
        log.info(f"Searching in {argv[1]} dir for files")
        return utils.util.get_fwd_fastqs(argv[1])
    return utils.util.get_fwd_fastqs()


if __name__ == "__main__":
    log.debug(f"args: {sys.argv}")
    print(main(sys.argv))
