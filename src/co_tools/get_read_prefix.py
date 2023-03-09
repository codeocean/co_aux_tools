#!/usr/bin/env python
import re
import sys
from pathlib import Path

from src.co_tools.get_logger import LOGGER
# import co_tools.co_fastq as co_fastq
from src.co_tools import co_fastq


def main(argv=sys.argv):
    LOGGER.debug(f"args: {sys.argv}")
    if len(argv) == 1:
        LOGGER.error("You failed to provide a filename")
        sys.exit("You failed to provide a filename")
    elif len(argv) == 2:
        print(co_fastq.get_prefix(argv[1]))
        return 0
    print(co_fastq.get_prefix(argv[1], argv[2]))
    return 0


if __name__ == "__main__":
    LOGGER.debug(f"args: {sys.argv}")
    sys.exit(main(sys.argv))
