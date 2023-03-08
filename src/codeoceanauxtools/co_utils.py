import os
import re
import subprocess
from multiprocessing import cpu_count
from pathlib import Path

from codeoceanauxtools.get_logger import LOGGER

# import get_logger

co_cpus = os.getenv("CO_CPUS")
aws_batch_job_id = os.getenv("AWS_BATCH_JOB_ID")


def get_cpu_limit(co_cpus=co_cpus, aws_batch_job_id=aws_batch_job_id):
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
    cmd = ["find", "-L", dir]
    LOGGER.debug(f"Running subprocess with the following cmd: {cmd}")
    return subprocess.check_output(cmd).decode("utf-8").strip()


def get_groups(filename: str = "sample_sheet.csv"):
    filepath = (
        subprocess.check_output(["find", "../data", "-name", filename])
        .decode("utf-8")
        .strip()
    )
    LOGGER.debug(f"Found sample_sheet at {filepath}")
    groups_set = set()
    with open(f"{filepath}") as infile:
        lines = infile.readlines()
        for line in lines:
            line = line.strip()
            line_group = line.split(",")[0]
            groups_set.add(line_group)
        groups = sorted(list(groups_set))
        LOGGER.debug(f"Returning the following groups from sample sheet: {groups}")
        return ",".join(groups)


def is_pipeline():
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
