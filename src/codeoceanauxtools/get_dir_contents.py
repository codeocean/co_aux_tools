#!/usr/bin/env python
import sys

import utils.util

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(
            f"*** These are the current files in the {sys.argv[1]} directory\n"
            + f"{utils.util.get_dir_contents(sys.argv[1])}"
        )
    else:
        print(
            "*** These are the current files in the ../data directory\n"
            + f"{utils.util.get_dir_contents()}"
        )
