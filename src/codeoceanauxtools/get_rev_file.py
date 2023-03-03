#!/usr/bin/env python
import sys

from .get_read_pattern import get_read_pattern


def get_rev_file(fwd_file):
    return fwd_file.replace(
        get_read_pattern(fwd_file, "1"), get_read_pattern(fwd_file, "2")
    )


if __name__ == "__main__":
    print(get_rev_file(sys.argv[1]))
