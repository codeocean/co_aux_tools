#!/usr/bin/env python
import sys

# local imports
from co_tools.get_logger import LOGGER
from co_tools.co_fastq import get_fastq_pair


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
