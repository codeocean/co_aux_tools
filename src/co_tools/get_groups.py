#!/usr/bin/env python
import sys

# local imports
from .get_logger import LOGGER
from .co_utils import get_groups


def main(argv=sys.argv):
    LOGGER.debug(f"args: {sys.argv}")
    if len(argv) > 1:
        print(get_groups(argv[1]))
        return 0
    print(get_groups())
    return 0


if __name__ == "__main__":
    LOGGER.debug(f"args: {sys.argv}")
    sys.exit(main(sys.argv))
