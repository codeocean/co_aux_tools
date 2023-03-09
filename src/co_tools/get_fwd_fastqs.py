#!/usr/bin/env python
import sys

from src.co_tools.get_logger import LOGGER
from src.co_tools import co_fastq
# import co_tools.co_fastq as co_fastq


def main(argv=sys.argv):
    LOGGER.debug(f"args: {sys.argv}")
    if len(argv) > 1:
        LOGGER.info(f"Searching in {argv[1]} dir for files")
        print(co_fastq.get_fwd_fastqs(argv[1]))
        return 0
    print(co_fastq.get_fwd_fastqs())
    return 0


if __name__ == "__main__":
    LOGGER.debug(f"args: {sys.argv}")
    sys.exit(main(sys.argv))
