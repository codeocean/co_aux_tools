#!/usr/bin/env python
import sys

import utils.util

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(utils.util.get_groups(sys.argv[1]))
    else:
        print(utils.util.get_groups())
