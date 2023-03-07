#!/usr/bin/env python
import sys

from get_logger import LOGGER
import co_aux_utils


def main(argv=None):
    if len(argv) > 1:
        return co_aux_utils.get_groups(argv[1])
    return co_aux_utils.get_groups()


if __name__ == "__main__":
    LOGGER.debug(f"args: {sys.argv}")
    print(main(sys.argv))
