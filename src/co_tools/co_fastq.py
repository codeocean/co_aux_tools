import os
import re
from glob import glob
from pathlib import Path

# local imports
from .get_logger import LOGGER


def get_fastq_pair(dir_path: str = "../data"):
    """This function returns a pair of paired-end reads files

    Args:
        dir_path (str, optional): The folder where all the reads files are. 
        Defaults to "../data".

    Returns:
        str: comma-separated pair of reads files as path to files
    """
    total_dirs = 0
    for base, dirs, files in os.walk(dir_path):
        for dir in dirs:
            total_dirs += 1
    if total_dirs != 2:
        LOGGER.error(
            f"The fastq files in {dir_path} are not properly configured"
            + " to use this function. There should be only 2 folders"
            + " inside the data folder."
        )
        return 0
    prefix_dict, this_prefix = {}, None
    fwd, rev = None, None
    for path in glob(str(f"{dir_path}/**/*.fastq.gz"), recursive=True):
        if prefix := get_prefix(path):
            if prefix in prefix_dict:
                prefix_dict[prefix].append(path)
                if len(prefix_dict[prefix]) == 3:
                    LOGGER.info(
                        f"prefix {prefix} occurs 3 times in the {dir_path} folder"
                    )
                    this_prefix = prefix
                    break
            else:
                prefix_dict[prefix] = [path]
        else:
            LOGGER.warning(f"No prefix determined for {path}")
    if not prefix_dict:
        LOGGER.error(f"No files found in {dir_path}")
        return 0
    if not this_prefix:
        LOGGER.error(f"fastq files in {dir_path} not properly organized")
        return 0
    for path in prefix_dict[this_prefix]:
        if get_read_direction(path) == "1":
            fwd = path
        elif get_read_direction(path) == "2":
            rev = path
    if fwd and rev:
        LOGGER.info(f"returning {fwd},{rev}")
        return f"{fwd},{rev}"
    else:
        LOGGER.error(
            f"Could not find complementary pair of fastq files in {dir_path}"
        )
        return 0


def get_fwd_fastqs(dir: str = "../data"):
    """Returns all the forward reads files in ascending alphabetical order

    Args:
        dir (str, optional): The folder where all the reads file are.
        Defaults to "../data".

    Returns:
        str: newline-separated string of forward reads files
    """
    if fastq_files := glob(str(f"{dir}/**/*.fastq.gz"), recursive=True):
        LOGGER.debug(f"Found the following fastq files in the {dir} folder:\n{fastq_files}")
        pattern = get_read_pattern(fastq_files[0])
        fwd_fastqs_list = glob(str(f"{dir}/**/*{pattern}"), recursive=True)
        fwd_fastqs_list.sort()
        fwd_fastqs = "\n".join(fwd_fastqs_list)
        LOGGER.debug(f"Returning the following fwd fastq files\n{fwd_fastqs}")
        return fwd_fastqs
    else:
        LOGGER.error(f"There are no fastq.gz files in the {dir} directory")
        return 0


def get_read_direction(filepath: str):
    """This function returns the direction of a single paired-end reads file

    Args:
        filepath (str): The path to the reads file you need the direction of

    Returns:
        str: Returns 1 if file is detected as forward, 2 otherwise
    """
    filename = filepath.split("/")[-1]
    LOGGER.debug(f"filename: {filename}")
    if "_" not in filename:
        LOGGER.warning(
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
        LOGGER.debug(f"match: {match}\ngroup 1 (prefix): {match.group(1)}")
        return match.group(1)

    if "_" in filename and int(split_position):
        prefix_list = filename.split("_")[: int(split_position)]
        LOGGER.debug(f"prefix_list: {prefix_list}")
        return "_".join(prefix_list)

    return filename.split(".")[0]


def get_rev_file(fwd_file: str, name_only=False):
    """This function returns the reverse reads file

    Args:
        fwd_file (str): The forward file you want to find the
        reverse file for.
        name_only (bool, optional): Set to True if you want this function to
        return only the filename. Defaults to False.

    Returns:
        _type_: _description_
    """
    if name_only:
        name_only = True if "true" in name_only.lower() else False
    LOGGER.debug(
        f"fwd_file: {fwd_file}\nWill replace {get_read_pattern(fwd_file, '1')}"
        + f" with {get_read_pattern(fwd_file, '2')}"
    )
    return (
        fwd_file.replace(
            get_read_pattern(fwd_file, "1"),
            get_read_pattern(fwd_file, "2"),
        ).split("/")[-1]
        if name_only
        else fwd_file.replace(
            get_read_pattern(fwd_file, "1"),
            get_read_pattern(fwd_file, "2"),
        )
    )
