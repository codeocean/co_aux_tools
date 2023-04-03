#!/usr/bin/env python
import sys

# local imports
from .co_fastq import get_fwd_fastqs
from .get_logger import LOGGER


def main(argv=sys.argv):
    LOGGER.debug(f"args: {sys.argv}")
    if len(argv) > 1:
        LOGGER.info(f"Searching in {argv[1]} dir for files")
        print(get_fwd_fastqs(argv[1]))
        return 0
    print(get_fwd_fastqs())
    return 0


if __name__ == "__main__":
    LOGGER.debug(f"args: {sys.argv}")
    sys.exit(main(sys.argv))
