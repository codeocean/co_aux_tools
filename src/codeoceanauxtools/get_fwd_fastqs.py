#!/usr/bin/env python
import sys

from get_logger import LOGGER
import co_aux_utils


def main(argv=None):
    if len(argv) > 1:
        LOGGER.info(f"Searching in {argv[1]} dir for files")
        return co_aux_utils.get_fwd_fastqs(argv[1])
    return co_aux_utils.get_fwd_fastqs()


if __name__ == "__main__":
    LOGGER.debug(f"args: {sys.argv}")
    print(main(sys.argv))
