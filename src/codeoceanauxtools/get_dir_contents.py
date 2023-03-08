#!/usr/bin/env python
import sys

# from get_logger import LOGGER
from codeoceanauxtools.get_logger import LOGGER
import co_utils


def main(argv=None):
    if len(argv) > 1:
        return (
            f"*** These are the current files in the {argv[1]} directory\n"
            + f"{co_utils.get_dir_contents(argv[1])}"
        )
    return (
        "*** These are the current files in the ../data directory\n"
        + f"{co_utils.get_dir_contents()}"
    )


if __name__ == "__main__":
    LOGGER.debug(f"args: {sys.argv}")
    print(main(sys.argv))
