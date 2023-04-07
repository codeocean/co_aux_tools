from src.co_tools.co_fastq import get_read_direction


# Tests for get_read_direction
def test_get_read_direction_filepath_R1():
    filepath = "/capsule/data/some_random_folder/gsm12345_R1.fastq.gz"
    assert get_read_direction(filepath) == "1"


def test_get_read_direction_filepath_R2():
    filepath = "/capsule/data/some_random_folder/gsm12345_R2.fastq.gz"
    assert get_read_direction(filepath) == "2"


def test_get_read_direction_filepath_1():
    filepath = "/capsule/data/some_random_folder/gsm12345_1.fastq.gz"
    assert get_read_direction(filepath) == "1"


def test_get_read_direction_filepath_2():
    filepath = "/capsule/data/some_random_folder/gsm12345_2.fastq.gz"
    assert get_read_direction(filepath) == "2"


def test_get_read_direction_file_R1():
    filename = "gsm12345_R1.fastq.gz"
    assert get_read_direction(filename) == "1"


def test_get_read_direction_file_R2():
    filename = "gsm12345_R2.fastq.gz"
    assert get_read_direction(filename) == "2"


def test_get_read_direction_file_1():
    filename = "gsm12345_1.fastq.gz"
    assert get_read_direction(filename) == "1"


def test_get_read_direction_file_2():
    filename = "gsm12345_2.fastq.gz"
    assert get_read_direction(filename) == "2"


def test_get_read_direction_not_paired_end_filepath():
    filename = "/capsule/data/some_random_folder/gsm12345.fastq.gz"
    assert not get_read_direction(filename)


def test_get_read_direction_not_paired_end_file():
    filename = "gsm12345.fastq.gz"
    assert not get_read_direction(filename)
