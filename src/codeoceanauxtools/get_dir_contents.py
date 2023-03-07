#!/usr/bin/env python
import logging
import sys

import utils.util

log = logging.getLogger(__name__)


def main(argv=None):
    if len(argv) > 1:
        return (
            f"*** These are the current files in the {argv[1]} directory\n"
            + f"{utils.util.get_dir_contents(argv[1])}"
        )
    return (
        "*** These are the current files in the ../data directory\n"
        + f"{utils.util.get_dir_contents()}"
    )


if __name__ == "__main__":
    log.debug(f"args: {sys.argv}")
    print(main(sys.argv))
