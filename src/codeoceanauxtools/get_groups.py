#!/usr/bin/env python
import sys

from get_logger import LOGGER
import aux_tools_utils.util


def main(argv=None):
    if len(argv) > 1:
        return aux_tools_utils.util.get_groups(argv[1])
    return aux_tools_utils.util.get_groups()


if __name__ == "__main__":
    LOGGER.debug(f"args: {sys.argv}")
    print(main(sys.argv))
