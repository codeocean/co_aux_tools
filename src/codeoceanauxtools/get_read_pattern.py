#!/usr/bin/env python
import sys

import utils.util

if __name__ == "__main__":
    print(utils.util.get_read_pattern(sys.argv[1], sys.argv[2]))
