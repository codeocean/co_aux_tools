#!/usr/bin/env python
import sys

import utils.util


def main():
    if len(sys.argv) > 1:
        return utils.util.get_groups(sys.argv[1])
    return utils.util.get_groups()


if __name__ == "__main__":
    print(main())
