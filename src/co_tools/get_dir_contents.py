#!/usr/bin/env python
import sys

from co_tools.get_logger import LOGGER
import co_tools.co_utils as co_utils


def main(argv=sys.argv):
    LOGGER.debug(f"args: {sys.argv}")
    if len(argv) > 1:
        print(
            f"*** These are the current files in the {argv[1]} directory\n"
            + f"{co_utils.get_dir_contents(argv[1])}"
        )
        return 0
    print(
        "*** These are the current files in the ../data directory\n"
        + f"{co_utils.get_dir_contents()}"
    )
    return 0


if __name__ == "__main__":
    LOGGER.debug(f"args: {sys.argv}")
    sys.exit(main(sys.argv))
