#!/usr/bin/env python
import sys


def get_read_pattern(filename, direction="1"):
    if "_" not in filename and "/" in filename:
        return filename.split("/")[-1]
    direction_complement = "2" if direction == "1" else "1"
    pattern = filename.split("_")[-1]
    return (
        pattern
        if direction in pattern
        else pattern.replace(direction_complement, direction)
    )


if __name__ == "__main__":
    print(get_read_pattern(sys.argv[1], sys.argv[2]))
