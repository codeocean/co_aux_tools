from glob import glob

import pytest

from src.co_tools.co_utils import get_dir_contents


# Tests for get_dir_contents
@pytest.mark.usefixtures("fastq_dir")
def test_get_dir_contents(fastq_dir):
    dir_contents = glob(str(f"{fastq_dir}/**/*"), recursive=True)
    dir_contents_joined = "\n".join(dir_contents)
    assert get_dir_contents(fastq_dir) == dir_contents_joined


@pytest.mark.usefixtures("results_dir")
def test_get_dir_contents_results(results_dir):
    dir_contents = glob(str(f"{results_dir}/**/*"), recursive=True)
    dir_contents_joined = "\n".join(dir_contents)
    assert get_dir_contents(results_dir) == dir_contents_joined
