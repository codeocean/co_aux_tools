import os
from glob import glob
from multiprocessing import cpu_count
from pathlib import Path

# local imports
from .get_logger import LOGGER

co_cpus = os.getenv("CO_CPUS")
aws_batch_job_id = os.getenv("AWS_BATCH_JOB_ID")


def get_cpu_limit(co_cpus=co_cpus, aws_batch_job_id=aws_batch_job_id):
    """This function returns an integer corresponding to the number of cores

    Args:
        co_cpus (int, optional): _description_. Defaults to co_cpus.
        aws_batch_job_id (int, optional): _description_. Defaults to aws_batch_job_id.

    Returns:
        int: number of cores available for compute
    """
    LOGGER.debug(f"co_cpus: {co_cpus}\naws_batch_job_id: {aws_batch_job_id}")
    if co_cpus:
        return co_cpus
    if aws_batch_job_id:
        return 1
    with open("/sys/fs/cgroup/cpu/cpu.cfs_quota_us") as fp:
        cfs_quota_us = int(fp.read())
    with open("/sys/fs/cgroup/cpu/cpu.cfs_period_us") as fp:
        cfs_period_us = int(fp.read())
    container_cpus = cfs_quota_us // cfs_period_us
    # For physical machine, the `cfs_quota_us` could be '-1'
    LOGGER.debug(f"container_cpus: {container_cpus}\ncpu_count(): {cpu_count()}")
    return cpu_count() if container_cpus < 1 else container_cpus


def get_dir_contents(dir: str = "../data"):
    """This function finds all the files and folders in a dir

    Args:
        dir (str, optional): The folder you want to search in. Defaults to "../data".

    Returns:
        str: newline separated string of files and folders in the search dir.
    """
    if dir_contents := glob(str(f"{dir}/**/*"), recursive=True):
        joined_contents = "\n".join(dir_contents)
        LOGGER.info(
            f"The following files and folders are in the {dir} folder:\n{joined_contents}"
        )
        return joined_contents
    LOGGER.warning(f"There are no files or folders in the {dir} folder.")
    return 0


def get_groups(filename: None):
    """This function returns all the groups in a .csv

    Args:
        filename (None): Path to a sample sheet. Will default to
        ../data/sample_sheet.csv if no path supplied. If a filename is supplied,
        this function will attempt to find the path to the file in the
        ../data folder

    Returns:
        str: comma-separated string of groups in ascending alphabetical order.
    """
    if not filename:
        sample_sheet = "../data/sample_sheet.csv"
    elif Path(filename).is_file():
        LOGGER.debug(f"{filename} is a file.")
        sample_sheet = filename
    else:
        LOGGER.debug(f"type for {filename}: {type(filename)}")
        if files_found := glob(str(f"../data/{filename}"), recursive=True):
            if len(files_found) > 1:
                LOGGER.warning(f"Found multiple sample_sheets. Will use {files_found[0]}")
            LOGGER.debug(f"Searching found the following sample sheet(s):\n{files_found}")
            sample_sheet = files_found[0]
        else:
            LOGGER.error(f"No sample sheet found for '{filename}'")
            return 0
    groups_set = set()
    try:
        with open(f"{sample_sheet}", "r") as infile:
            lines = infile.readlines()
            for line in lines:
                line = line.strip()
                line_group = line.split(",")[0]
                groups_set.add(line_group)
            groups = sorted(list(groups_set))
            LOGGER.debug(f"Returning the following groups from sample sheet: {groups}")
            return ",".join(groups)
    except Exception as e:
        LOGGER.error(f"Could not open {sample_sheet} due to error {e}.")
        return 0


def is_pipeline():
    """This function lets confirms if code is executing in a pipeline

    Returns:
        int: Returns 1 if in a pipeline, 0 otherwise.
    """
    return 1 if bool(os.getenv("AWS_BATCH_JOB_ID")) else 0


def print_log_msg(msg=None, level="WARNING"):
    level = level.upper()
    if level == "DEBUG":
        return LOGGER.debug(msg)
    elif level == "INFO":
        return LOGGER.info(msg)
    elif level == "WARNING":
        return LOGGER.warning(msg)
    elif level == "ERROR":
        return LOGGER.error(msg)
    elif level == "CRITICAL":
        return LOGGER.critical(msg)
    else:
        raise Exception(
            "logging level is not one of [DEBUG, INFO, WARNING, ERROR, CRITICAL]"
        )
