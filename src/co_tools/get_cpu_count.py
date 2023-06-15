#!/usr/bin/env python
import sys

# local imports
from .co_utils import get_cpu_limit


def main():
    print(get_cpu_limit())
    return 0


if __name__ == "__main__":
    sys.exit(main())
