#!/usr/bin/env python
import sys

def get_read_direction(filepath):
    if "_" not in filepath:
        return ""
    filename = filepath.split("/")[-1]
    return "1" if "1" in filename.split("_")[-1].split(".")[0] else "2"

print(get_read_direction(sys.argv[1]))
