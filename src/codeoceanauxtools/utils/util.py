import logging
import os
import re
import subprocess
from multiprocessing import cpu_count
from pathlib import Path

log = logging.getLogger(__name__)
co_cpus = os.getenv("CO_CPUS")
aws_batch_job_id = os.getenv("AWS_BATCH_JOB_ID")


def get_cpu_limit(co_cpus=co_cpus, aws_batch_job_id=aws_batch_job_id):
    log.debug(f"co_cpus: {co_cpus}\naws_batch_job_id: {aws_batch_job_id}")
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
    log.debug(f"container_cpus: {container_cpus}\ncpu_count(): {cpu_count()}")
    return cpu_count() if container_cpus < 1 else container_cpus


def get_dir_contents(dir: str = "../data"):
    cmd = ["find", "-L", dir]
    return subprocess.check_output(cmd).decode("utf-8").strip()


def get_groups(filename: str = "sample_sheet.csv"):
    filepath = (
        subprocess.check_output(["find", "../data", "-name", filename])
        .decode("utf-8")
        .strip()
    )
    log.debug(f"Found sample_sheet at {filepath}")
    groups_set = set()
    with open(f"{filepath}") as infile:
        lines = infile.readlines()
        for line in lines:
            line = line.strip()
            line_group = line.split(",")[0]
            groups_set.add(line_group)
        return ",".join(sorted(list(groups_set)))


def is_pipeline():
    return 1 if bool(os.getenv("AWS_BATCH_JOB_ID")) else 0


def get_read_direction(filepath: str):
    filename = filepath.split("/")[-1]
    log.debug(f"filename: {filename}")
    if "_" not in filename:
        return 0
    return "1" if "1" in filename.split("_")[-1].split(".")[0] else "2"


def get_read_pattern(filename: str, direction: str = "1"):
    if "_" not in filename and "/" in filename:
        return filename.split("/")[-1]
    direction_complement = "2" if direction == "1" else "1"
    pattern = filename.split("_")[-1]
    log.debug(f"pattern: {pattern}")
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

    match = re.search(r"(.*?)_S\d+_.*R\d_001.fastq.gz", filename)

    if match:
        log.debug(f"match: {match}\ngroup 1 (prefix): {match.group(1)}")
        return match.group(1)

    if "_" in filename and int(split_position):
        prefix_list = filename.split("_")[: int(split_position)]
        log.debug(f"prefix_list: {prefix_list}")
        return "_".join(prefix_list)

    return filename.split(".")[0]


def get_rev_file(fwd_file: str):
    log.debug(f"fwd_file: {fwd_file}\nWill replace {get_read_pattern(fwd_file, '1')} with {get_read_pattern(fwd_file, '2')}")
    return fwd_file.replace(
        get_read_pattern(fwd_file, "1"),
        get_read_pattern(fwd_file, "2"),
    )
