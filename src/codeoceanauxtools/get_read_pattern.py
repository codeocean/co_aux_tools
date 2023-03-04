#!/usr/bin/env python
import sys

import utils.util


def main():
    if len(sys.argv) == 1:
        sys.exit("You failed to provide a filename and direction")
    elif len(sys.argv) == 2:
        return utils.util.get_read_pattern(sys.argv[1])
    return utils.util.get_read_pattern(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    print(main())
