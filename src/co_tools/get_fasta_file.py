#!/usr/bin/env python
import sys

# local import
from .co_fasta import find_fasta_file
from .get_logger import LOGGER


def main(argv=sys.argv):
    if len(argv) == 1:
        LOGGER.warning(
            "You failed to provide a search directory."
            + " Will continue by searching in ../data"
        )
        print(find_fasta_file("../data"))
        return 0
    else:
        LOGGER.info(f"Input dir to search for fasta file: {sys.argv[1]}")
        print(find_fasta_file(sys.argv[1]))
        return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
