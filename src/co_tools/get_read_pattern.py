#!/usr/bin/env python
import sys

# from get_logger import LOGGER
from src.co_tools.get_logger import LOGGER
# import co_tools.co_fastq as co_fastq
from src.co_tools import co_fastq


def main(argv=sys.argv):
    LOGGER.debug(f"args: {sys.argv}")
    if len(argv) == 1:
        LOGGER.error("You failed to provide a filename and direction")
        sys.exit("You failed to provide a filename and direction")
    elif len(argv) == 2:
        print(co_fastq.get_read_pattern(argv[1]))
        return 0
    print(co_fastq.get_read_pattern(argv[1], argv[2]))
    return 0


if __name__ == "__main__":
    LOGGER.debug(f"args: {sys.argv}")
    sys.exit(main(sys.argv))
