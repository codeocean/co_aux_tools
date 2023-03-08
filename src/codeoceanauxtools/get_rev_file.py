#!/usr/bin/env python
import sys

# from get_logger import LOGGER
from codeoceanauxtools.get_logger import LOGGER
import co_fastq


def main(argv=None):
    if len(argv) == 1:
        LOGGER.error("You failed to provide a filename")
        sys.exit("You failed to provide a filename")
    return co_fastq.get_rev_file(argv[1])


if __name__ == "__main__":
    LOGGER.debug(f"args: {sys.argv}")
    print(main(sys.argv))
