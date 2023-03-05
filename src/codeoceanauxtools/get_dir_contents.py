#!/usr/bin/env python
import logging
import sys

import utils.util

log = logging.getLogger(__name__)


def main():
    if len(sys.argv) > 1:
        log.debug(f"args: {sys.argv}")
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
