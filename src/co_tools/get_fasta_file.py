#!/usr/bin/env python
import argparse
import sys
from pathlib import Path

# local import
from .co_fasta import find_fasta_file
from .get_logger import LOGGER


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Find fasta files recursively from input directory"
    )
    parser.add_argument(
        "--input_dir", help="Input path to search", default="../data", type=Path
    )

    if argv:
        args = parser.parse_args(argv)
    else:
        parser.print_usage()
        return 0
    input_dir = args.input_dir.absolute()
    LOGGER.info(f"Input dir to search for fasta files {args.input_dir}")
    fasta_file = find_fasta_file(args.input_dir)
    if fasta_file:
        print(fasta_file)
    else:
        LOGGER.error("Unable to find fasta file!")
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
