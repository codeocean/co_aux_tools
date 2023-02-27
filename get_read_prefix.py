#!/usr/bin/env python
from pathlib import Path
import re
import sys


def get_prefix(filename: str, split_position=-1):
    filename = Path(filename).name
    # illumina read files use a specific format, and sometimes allow underscores in the prefix
    # SampleName_S1_L001_R1_001.fastq.gz for lane 1
    # SampleName_S1_R1_001.fastq.gz for merged lanes.

    match = re.search(r"(.*?)_S\d+_.*R\d_001.fastq.gz", filename)

    if match:
        return match.group(1)

    if "_" in filename and int(split_position):
        prefix_list = filename.split("_")[: int(split_position)]
        return "_".join(prefix_list)
    else:
        return filename.split(".")[0]


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print(get_prefix(sys.argv[1], sys.argv[2]))
    else:
        print(get_prefix(sys.argv[1]))

