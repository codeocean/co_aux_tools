#!/usr/bin/env python
import sys

import co_tools.co_utils as co_utils


def main():
    print(co_utils.is_pipeline())
    return 0


if __name__ == "__main__":
    sys.exit(main())
