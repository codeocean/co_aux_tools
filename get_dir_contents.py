#!/usr/bin/env python
import subprocess
import sys


def get_dir_contents(dir="../data"):
    cmd = ["find", "-L", dir]
    return subprocess.check_output(cmd).decode("utf-8").strip()


if len(sys.argv) > 1:
    print(
        f"*** These are the current files in the {sys.argv[1]} directory\n" +
        f"{get_dir_contents(sys.argv[1])}"
    )
else:
    print(
        f"*** These are the current files in the ../data directory\n" +
        f"{get_dir_contents()}"
    )
