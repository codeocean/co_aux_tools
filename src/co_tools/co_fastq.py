import os
import re
from glob import glob
from pathlib import Path

if os.environ.get("CO_LOG", "false").lower() == "true":
    from .get_logger import LOGGER

    log = LOGGER
else:
    import logging

    log = logging.getLogger(__name__)


def get_fastq_pair(dir_path: str = "../data"):
    """This function returns a pair of paired-end reads files

    Args:
        dir (str, optional): The folder where all the reads files are.
        Defaults to "../data".

    Returns:
        str: comma-separated pair of reads files as path to files
    """
    total_dirs = 0
    for base, dirs, files in os.walk(dir_path):
        log.debug(f"Found the following directories {dirs}")
        for dir in dirs:
            log.debug(f"Path to dir {Path(dir).resolve()}")
            total_dirs += 1
    if total_dirs != 2:
        log.error(
            f"The fastq files in {dir_path} are not properly configured"
            + " to use this function. There should be only 2 folders"
            + f" inside the {dir_path} folder."
        )
        return 0
    prefix_dict, this_prefix = {}, None
    fwd, rev = None, None
    for path in glob(str(f"{Path(dir_path).resolve()}/**/*.fastq.gz"), recursive=True):
        log.debug(f"Will attempt to determine prefix for {path}")
        if prefix := get_prefix(path):
            if prefix in prefix_dict:
                prefix_dict[prefix].append(path)
                if len(prefix_dict[prefix]) == 3:
                    log.info(f"prefix {prefix} occurs 3 times in the {dir_path} folder")
                    this_prefix = prefix
                    break
            else:
                prefix_dict[prefix] = [path]
        else:
            log.warning(f"No prefix determined for {path}")
    if not prefix_dict:
        log.warning(f"No files found in {dir_path}")
        return 0
    if not this_prefix:
        log.warning(f"fastq files in {dir_path} not properly organized")
        return 0
    for path in prefix_dict[this_prefix]:
        if get_read_direction(path) == "1":
            fwd = path
        elif get_read_direction(path) == "2":
            rev = path
    if fwd and rev:
        log.info(f"returning {fwd},{rev}")
        return f"{fwd},{rev}"
    else:
        log.warning(f"Could not find complementary pair of fastq files in {dir_path}")
        return 0


def get_fastqs(fwd: bool = False, dir: str = "../data"):
    """Returns all the reads files in ascending alphabetical order

    Args:
        dir (str, optional): The folder where all the reads file are.
        Defaults to "../data".

    Returns:
        str: newline-separated string of reads files
    """
    if not dir:
        dir = "../data"
    if fastq_files := glob(str(f"{dir}/**/*.fastq.gz"), recursive=True):
        log.debug(
            f"Found the following fastq files in the {dir} folder:\n{fastq_files}"
        )
        if fwd:
            log.debug(f"fwd={fwd}")
            pattern = get_read_pattern(fastq_files[0])
            fastq_files = glob(str(f"{dir}/**/*{pattern}"), recursive=True)
        fastq_files.sort()
        fastqs = "\n".join(fastq_files)
        log.debug(f"Returning the following fastq files\n{fastqs}")
        return fastqs
    else:
        log.error(f"There are no fastq.gz files in the {dir} directory")
        return 0


def get_read_direction(filepath: str):
    """This function returns the direction of a single paired-end reads file

    Args:
        filepath (str): The path to the reads file you need the direction of

    Returns:
        str: Returns 1 if file is detected as forward, 2 otherwise
    """
    filename = Path(filepath).name
    log.debug(f"filename: {filename}")
    if "_" not in filename:
        log.warning(
            "You might be trying to use a single end reads file as a paired"
            + f" end reads file. Current input: {filepath}"
        )
        return 0
    return "1" if "1" in filename.split("_")[-1].split(".")[0] else "2"


def get_read_pattern(filename: str, direction: str = "1"):
    """This function returns the pattern shared for half the paired-end reads files

    Args:
        filename (str): Name of file to determine pattern from
        direction (str, optional): The direction you need the pattern for.
        Defaults to "1". Accepts "1" for forward or "2" for reverse

    Returns:
        str: The pattern for all the forward or reverse paired-end reads file
        corresponding to the direction you specified in 'direction'
    """
    if "_" not in filename and "/" in filename:
        log.warning(
            f"{filename} might be a single end reads file. The pattern being returned"
            + " is the entire filename"
        )
        return Path(filename).name
    direction_complement = "2" if direction == "1" else "1"
    pattern = filename.split("_")[-1]
    log.debug(f"pattern: {pattern}")
    return (
        pattern
        if direction in pattern
        else pattern.replace(direction_complement, direction)
    )


def get_prefix(filename: str, split_position: str = "-1"):
    """This function returns the prefix that is unique to (1) pair of paired-end files

    Args:
        filename (str): The name of the file to determine prefix from
        split_position (str, optional): If underscores are in the filename and user
        just needs to trim the filename after a certain underscore, then
        this arg specifies where to trim e.g.
        get_prefix("GSM1234_sample12_exp.fastq.gz", -1) returns "GSM1234_sample12").
        Defaults to "-1".

    Returns:
        str: Returns the prefix that is unique to a single pair of paired-end
        reads files.
    """
    filename = Path(filename).name
    # illumina read files use a specific format, and sometimes allow underscores in the prefix
    # SampleName_S1_L001_R1_001.fastq.gz for lane 1
    # SampleName_S1_R1_001.fastq.gz for merged lanes.

    if match := re.search(r"(.*?)_S\d+_.*R\d_001.fastq.gz", filename):
        log.debug(f"match: {match}\ngroup 1 (prefix): {match.group(1)}")
        return match.group(1)

    if "_" in filename and int(split_position):
        prefix_list = filename.split("_")[: int(split_position)]
        log.debug(f"prefix_list: {prefix_list}")
        return "_".join(prefix_list)

    log.warning(f"A prefix was not able to be determined for {filename}")
    return 0


def get_rev_file(
    fwd_file: str,
    name_only: bool = False,
    pattern_fwd: str = None,
    pattern_rev: str = None,
):
    """_summary_

    Args:
        fwd_file (str): The forward file you want to find the reverse
        file for.
        name_only (bool, optional): Set to True if you want this function to
        return only the filename. Defaults to False.
        pattern_fwd (str, optional): Specify the pattern to replace.
        Defaults to None.
        pattern_rev (str, optional): Specify the replacement pattern.
        Defaults to None.

    Returns:
        str: The reverse reads file
    """
    # if name_only:
    #     name_only = True if "true" in str(name_only).lower() else False
    if not pattern_fwd:
        pattern_fwd = get_read_pattern(fwd_file, "1")
        log.debug(f"Autodetected forward pattern: {pattern_fwd}")
    if not pattern_rev:
        pattern_rev = get_read_pattern(fwd_file, "2")
        log.debug(f"Autodetected reverse pattern: {pattern_rev}")
    log.info(f"fwd_file={fwd_file}. Will replace {pattern_fwd} with {pattern_rev}")
    return (
        Path(
            fwd_file.replace(
                pattern_fwd,
                pattern_rev,
            )
        ).name
        if name_only
        else fwd_file.replace(
            pattern_fwd,
            pattern_rev,
        )
    )
