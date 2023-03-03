#!/usr/bin/env python
import os
import sys


def is_pipeline():
    return "1" if bool(os.getenv("AWS_BATCH_JOB_ID")) else "0"


if __name__ == "__main__":
    # print(is_pipeline())
    sys.exit(is_pipeline())
