import pytest
import subprocess

from src.co_tools.co_utils import get_dir_contents


# Tests for get_dir_contents
@pytest.mark.usefixtures("fastq_dir")
def test_get_dir_contents(fastq_dir):
    cmd = ["find", "-L", fastq_dir]
    dir_contents = subprocess.check_output(cmd).decode("utf-8").strip()
    assert get_dir_contents(fastq_dir) == dir_contents


@pytest.mark.usefixtures("results_dir")
def test_get_dir_contents_results(results_dir):
    # cmd = ["find", "-L", "../results"]
    cmd = ["find", "-L", results_dir]
    dir_contents = subprocess.check_output(cmd).decode("utf-8").strip()
    assert get_dir_contents(results_dir) == dir_contents
