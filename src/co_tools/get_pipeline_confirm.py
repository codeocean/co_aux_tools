#!/usr/bin/env python
import sys

# import co_tools.co_utils as co_utils
from .co_utils import is_pipeline


def main():
    print(is_pipeline())
    return 0


if __name__ == "__main__":
    sys.exit(main())
