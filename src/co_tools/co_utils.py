import os
from glob import glob
from multiprocessing import cpu_count
from pathlib import Path

if os.environ.get("CO_LOG", "false").lower() == "true":
    from .get_logger import LOGGER

    log = LOGGER
else:
    import logging

    log = logging.getLogger(__name__)

co_cpus = os.environ.get("CO_CPUS")
aws_batch_job_id = os.environ.get("AWS_BATCH_JOB_ID")


def get_cpu_limit(co_cpus=co_cpus, aws_batch_job_id=aws_batch_job_id):
    """This function returns an integer corresponding to the number of cores

    Args:
        co_cpus (int, optional): _description_. Defaults to co_cpus.
        aws_batch_job_id (int, optional): _description_. Defaults to aws_batch_job_id.

    Returns:
        int: number of cores available for compute
    """
    log.debug(f"co_cpus: {co_cpus} aws_batch_job_id: {aws_batch_job_id}")
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
    log.debug(f"container_cpus: {container_cpus} cpu_count(): {cpu_count()}")
    return cpu_count() if container_cpus < 1 else container_cpus


def get_dir_contents(dir: str = "../data"):
    """This function finds all the files and folders in a dir

    Args:
        dir (str, optional): The folder you want to search in. Defaults to "../data".

    Returns:
        str: newline separated string of files and folders in the search dir.
    """
    if dir_contents := glob(str(f"{dir}/**/*"), recursive=True):
        log.debug(f"Found the following files in {dir} {dir_contents}")
        return "\n".join(dir_contents)
    log.warning(f"There are no files or folders in the {dir} folder.")
    return 0


def get_groups(filename: str = "../data/sample_sheet.csv", dir: str = ""):
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
        log.error(f"Improper filename given for sample_sheet. filename={filename}")
        return 1
    elif Path(filename).is_file():
        log.debug(f"{filename} is a file.")
        sample_sheet = filename
    else:
        log.debug(
            f"{filename} is not a file. Will search for file. Type: {type(filename)}"
        )
        if "/" in filename:
            filename = filename.split("/")[-1]
            log.debug(f"filename: {filename}")
        if files_found := glob(
            str(f"{Path(dir).resolve()}/{filename}"), recursive=True
        ):
            if len(files_found) > 1:
                log.warning(f"Found multiple sample_sheets. Will use {files_found[0]}")
            log.debug(f"Found the following sample sheet(s): {files_found}")
            sample_sheet = files_found[0]
        else:
            log.warning(f"No sample sheet found for '{filename}'")
            sample_sheet = filename
    groups_set = set()
    try:
        with open(f"{sample_sheet}", "r") as infile:
            lines = infile.readlines()
            log.debug(f"lines: {lines}")
            for line in lines:
                line = line.strip()
                line_group = line.split(",")[0]
                groups_set.add(line_group)
            groups = sorted(list(groups_set))
            log.debug(f"Returning the following groups from sample sheet: {groups}")
            return ",".join(groups)
    except Exception as e:
        log.error(f"Could not open {sample_sheet} due to error {e}.")
        return 0


def is_pipeline():
    """This function lets confirms if code is executing in a pipeline

    Returns:
        int: Returns 1 if in a pipeline, 0 otherwise.
    """
    return 1 if bool(os.environ.get("AWS_BATCH_JOB_ID")) else 0


def print_log_msg(msg=None, level="WARNING"):
    level = level.upper()
    if level == "DEBUG":
        return log.debug(msg)
    elif level == "INFO":
        return log.info(msg)
    elif level == "WARNING":
        return log.warning(msg)
    elif level == "ERROR":
        return log.error(msg)
    elif level == "CRITICAL":
        return log.critical(msg)
    else:
        raise Exception(
            "logging level is not one of [DEBUG, INFO, WARNING, ERROR, CRITICAL]"
        )
