import re
import subprocess
from pathlib import Path

# local imports
from .co_logger.get_logger import LOGGER


def get_fwd_fastqs(dir: str = "../data"):
    some_fastq = (
        subprocess.check_output(["find", "-L", dir, "-name", "*.fastq.gz"])
        .decode("utf-8")
        .strip()
    )
    if not some_fastq:
        LOGGER.error(f"There are no fastq.gz files in the {dir} directory")
        return 0
    if "\n" in some_fastq:
        some_fastq = some_fastq.split("\n")[0]
    pattern = get_read_pattern(some_fastq)
    LOGGER.debug(f"some_fastq: {some_fastq}")
    LOGGER.debug(f"pattern: {pattern}")
    files = (
        subprocess.check_output(["find", "-L", dir, "-name", f"*{pattern}"])
        .decode("utf-8")
        .strip()
    )
    LOGGER.debug(f"type for files is: {type(files)}")
    LOGGER.debug(f"files: {files}")
    return files


def get_read_direction(filepath: str):
    filename = filepath.split("/")[-1]
    LOGGER.debug(f"filename: {filename}")
    if "_" not in filename:
        LOGGER.warning(
            f"You might be trying to use a single end reads file as a paired end reads"
            + " file. Check your input"
        )
        return 0
    return "1" if "1" in filename.split("_")[-1].split(".")[0] else "2"


def get_read_pattern(filename: str, direction: str = "1"):
    if "_" not in filename and "/" in filename:
        LOGGER.warning(
            f"{filename} might be a single end reads file. The pattern being returned"
            + " is the entire filename"
        )
        return filename.split("/")[-1]
    direction_complement = "2" if direction == "1" else "1"
    pattern = filename.split("_")[-1]
    LOGGER.debug(f"pattern: {pattern}")
    return (
        pattern
        if direction in pattern
        else pattern.replace(direction_complement, direction)
    )


def get_prefix(filename: str, split_position: str = "-1"):
    filename = Path(filename).name
    # illumina read files use a specific format, and sometimes allow underscores in the prefix
    # SampleName_S1_L001_R1_001.fastq.gz for lane 1
    # SampleName_S1_R1_001.fastq.gz for merged lanes.

    if (match := re.search(r"(.*?)_S\d+_.*R\d_001.fastq.gz", filename)):
        LOGGER.debug(f"match: {match}\ngroup 1 (prefix): {match.group(1)}")
        return match.group(1)

    if "_" in filename and int(split_position):
        prefix_list = filename.split("_")[: int(split_position)]
        LOGGER.debug(f"prefix_list: {prefix_list}")
        return "_".join(prefix_list)

    return filename.split(".")[0]


def get_rev_file(fwd_file: str):
    LOGGER.debug(
        f"fwd_file: {fwd_file}\nWill replace {get_read_pattern(fwd_file, '1')}"
        + f" with {get_read_pattern(fwd_file, '2')}"
    )
    return fwd_file.replace(
        get_read_pattern(fwd_file, "1"),
        get_read_pattern(fwd_file, "2"),
    )
