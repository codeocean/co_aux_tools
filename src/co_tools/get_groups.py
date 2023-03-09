#!/usr/bin/env python
import sys

# from get_logger import LOGGER
from co_tools.get_logger import LOGGER
import co_tools.co_utils as co_utils


def main(argv=sys.argv):
    LOGGER.debug(f"args: {sys.argv}")
    if len(argv) > 1:
        print(co_utils.get_groups(argv[1]))
        return 0
    print(co_utils.get_groups())
    return 0


if __name__ == "__main__":
    LOGGER.debug(f"args: {sys.argv}")
    sys.exit(main(sys.argv))
