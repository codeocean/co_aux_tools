#!/usr/bin/env python
import re
import sys
from pathlib import Path

import utils.util

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print(utils.util.get_prefix(sys.argv[1], sys.argv[2]))
    else:
        print(utils.util.get_prefix(sys.argv[1]))
