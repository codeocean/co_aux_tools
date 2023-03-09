#!/usr/bin/env python
import sys

from src.co_tools import co_utils


def main():
    print(co_utils.get_cpu_limit())
    return 0


if __name__ == "__main__":
    sys.exit(main())
