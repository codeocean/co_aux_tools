#!/usr/bin/env python
import sys

import utils.util


def main():
    if len(sys.argv) > 1:
        return (
            f"*** These are the current files in the {sys.argv[1]} directory\n"
            + f"{utils.util.get_dir_contents(sys.argv[1])}"
        )
    return (
        "*** These are the current files in the ../data directory\n"
        + f"{utils.util.get_dir_contents()}"
    )


if __name__ == "__main__":
    print(main())
