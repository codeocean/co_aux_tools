#!/usr/bin/env python
import sys

import utils.util


def main():
    if len(sys.argv) == 1:
        sys.exit("You failed to provide a filename")
    return utils.util.get_rev_file(sys.argv[1])


if __name__ == "__main__":
    print(main())
