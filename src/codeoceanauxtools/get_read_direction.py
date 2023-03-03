#!/usr/bin/env python
import sys


def get_read_direction(filepath):
    filename = filepath.split("/")[-1]
    if "_" not in filename:
        return 0
    return "1" if "1" in filename.split("_")[-1].split(".")[0] else "2"


if __name__ == "__main__":
    print(get_read_direction(sys.argv[1]))
