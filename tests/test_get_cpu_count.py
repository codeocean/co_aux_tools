from multiprocessing import cpu_count

from src.co_tools.co_utils import get_cpu_limit


# Tests for get_cpu_count
def test_v210_capsule():
    co_cpus = 3
    aws_batch_job_id = None
    assert get_cpu_limit(co_cpus, aws_batch_job_id) == 3


def test_v210_pipeline():
    co_cpus = 3
    aws_batch_job_id = "123456"
    assert get_cpu_limit(co_cpus, aws_batch_job_id) == 3


def test_v29_capsule():
    co_cpus = None
    aws_batch_job_id = None
    assert get_cpu_limit(co_cpus, aws_batch_job_id) == cpu_count()


def test_v29_pipeline():
    co_cpus = None
    aws_batch_job_id = "123456"
    assert get_cpu_limit(co_cpus, aws_batch_job_id) == 1
