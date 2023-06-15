#!/usr/bin/env python
import os
import sys

from .co_utils import get_dir_contents

if os.getenv("CO_LOG").lower() == "true":
    from .get_logger import LOGGER

    log = LOGGER
else:
    import logging

    log = logging.getLogger(__name__)


def main(argv=sys.argv):
    log.debug(f"args: {sys.argv}")
    if len(argv) > 1:
        print(
            f"*** These are the current files in the {argv[1]} directory\n"
            + f"{get_dir_contents(argv[1])}"
        )
        return 0
    print(
        "*** These are the current files in the ../data directory\n"
        + f"{get_dir_contents()}"
    )
    return 0


if __name__ == "__main__":
    log.debug(f"args: {sys.argv}")
    sys.exit(main(sys.argv))
