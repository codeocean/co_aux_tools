#!/usr/bin/env python
from multiprocessing import cpu_count
import os

co_cpus = os.getenv("CO_CPUS")
aws_batch_job_id = os.getenv("AWS_BATCH_JOB_ID")


def get_cpu_limit(co_cpus = co_cpus, aws_batch_job_id = aws_batch_job_id):
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
    return cpu_count() if container_cpus < 1 else container_cpus


if __name__ == "__main__":
    print(get_cpu_limit())
