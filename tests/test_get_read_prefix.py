from src.co_tools.co_fastq import get_prefix


# Tests for get_prefix
def test_get_prefix_illumina1():
    filename = "test_bad_prefix_S1_L001_R1_001.fastq.gz"
    assert get_prefix(filename) == "test_bad_prefix"


def test_get_prefix_illumina2():
    filename = "test_bad_prefix_S1_R1_001.fastq.gz"
    assert get_prefix(filename) == "test_bad_prefix"


def test_get_prefix_illumina1_path():
    filepath = "/some/path/to/test_bad_prefix_S1_L001_R1_001.fastq.gz"
    assert get_prefix(filepath) == "test_bad_prefix"


def test_get_prefix_illumina2_path():
    filepath = "/some/path/to/test_bad_prefix_S1_R1_001.fastq.gz"
    assert get_prefix(filepath) == "test_bad_prefix"


def test_get_prefix_R1():
    filename = "GSM1234_sample12_R1.fastq.gz"
    assert get_prefix(filename) == "GSM1234_sample12"


def test_get_prefix_R2():
    filename = "GSM1234_sample12_R2.fastq.gz"
    assert get_prefix(filename) == "GSM1234_sample12"


def test_get_prefix_single_end1():
    filename = "GSM1234_sample12_exp.fastq.gz"
    assert get_prefix(filename, 0) == "GSM1234_sample12_exp"


def test_get_prefix_single_end2():
    filename = "GSM1234_sample12_exp.fastq.gz"
    assert get_prefix(filename, -1) == "GSM1234_sample12"


def test_get_prefix_single_end3():
    filename = "GSM1234_sample12_exp.fastq.gz"
    assert get_prefix(filename, -2) == "GSM1234"
