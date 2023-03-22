#!/usr/bin/env python
import sys

from .co_fastq import get_fastq_pair
# local imports
from .get_logger import LOGGER


def main(argv=sys.argv):
    LOGGER.debug(f"args: {sys.argv}")
    if len(argv) > 1:
        print(get_fastq_pair(argv[1]))
        return 0
    print(get_fastq_pair())
    return 0


if __name__ == "__main__":
    LOGGER.debug(f"args: {sys.argv}")
    sys.exit(main(sys.argv))
