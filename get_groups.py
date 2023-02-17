#!/usr/bin/env python
import subprocess
import sys

def get_groups(filename="sample_sheet.csv"):
    filepath = subprocess.check_output(["find", "../data", "-name", filename]).decode("utf-8").strip()
    groups_set = set()
    with open(f"{filepath}") as infile:
        lines = infile.readlines()
        for line in lines:
            line = line.strip()
            line_group = line.split(",")[0]
            groups_set.add(line_group)
        return ",".join(list(groups_set))

if len(sys.argv) > 1:
    print(get_groups(sys.argv[1]))
else:
    print(get_groups())
