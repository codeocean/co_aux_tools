#!/usr/bin/env python
import re
import sys
from pathlib import Path

import utils.util


def main():
    if len(sys.argv) == 1:
        sys.exit("You failed to provide a filename")
    elif len(sys.argv) == 2:
        return utils.util.get_prefix(sys.argv[1])
    return utils.util.get_prefix(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    print(main())
