#!/usr/bin/env python
import os
import sys

from .co_fasta import find_fasta_file

if os.getenv("CO_LOG").lower() == "true":
    from .get_logger import LOGGER

    log = LOGGER
else:
    import logging

    log = logging.getLogger(__name__)


def main(argv=sys.argv):
    if len(argv) == 1:
        log.warning(
            "You failed to provide a search directory."
            + " Will continue by searching in ../data"
        )
        print(find_fasta_file("../data"))
        return 0
    else:
        log.info(f"Input dir to search for fasta file: {sys.argv[1]}")
        print(find_fasta_file(sys.argv[1]))
        return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
