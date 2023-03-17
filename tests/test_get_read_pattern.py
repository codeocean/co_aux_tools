from src.co_tools.co_fastq import get_read_pattern


# Tests for get_read_pattern
def test_get_read_pattern_R1_filename():
    filename = "gsm12345_other_identifiers_R1.fastq.gz"
    assert get_read_pattern(filename, "1") == "R1.fastq.gz"


def test_get_read_pattern_R1_filename_mismatch():
    filename = "gsm12345_other_identifiers_R1.fastq.gz"
    assert not get_read_pattern(filename, "1") == "R2.fastq.gz"


def test_get_read_pattern_R1_opposite_filename():
    filename = "gsm12345_other_identifiers_R1.fastq.gz"
    assert get_read_pattern(filename, "2") == "R2.fastq.gz"


def test_get_read_pattern_R1_opposite_filename_mismatch():
    filename = "gsm12345_other_identifiers_R1.fastq.gz"
    assert not get_read_pattern(filename, "2") == "R1.fastq.gz"


def test_get_read_pattern_R2_filename():
    filename = "gsm12345_other_identifiers_R1.fastq.gz"
    assert get_read_pattern(filename, "2") == "R2.fastq.gz"


def test_get_read_pattern_R2_filename_mismatch():
    filename = "gsm12345_other_identifiers_R1.fastq.gz"
    assert not get_read_pattern(filename, "2") == "R1.fastq.gz"


def test_get_read_pattern_R2_opposite_filename():
    filename = "gsm12345_other_identifiers_R1.fastq.gz"
    assert get_read_pattern(filename, "1") == "R1.fastq.gz"


def test_get_read_pattern_R2_opposite_filename_mismatch():
    filename = "gsm12345_other_identifiers_R1.fastq.gz"
    assert not get_read_pattern(filename, "1") == "R2.fastq.gz"


def test_get_read_pattern_R1_filepath():
    filepath = "/capsule/data/some_random_folder/gsm12345_other_identifiers_R1.fastq.gz"
    assert get_read_pattern(filepath, "1") == "R1.fastq.gz"


def test_get_read_pattern_R1_filepath_mismatch():
    filepath = "/capsule/data/some_random_folder/gsm12345_other_identifiers_R1.fastq.gz"
    assert not get_read_pattern(filepath, "1") == "R2.fastq.gz"


def test_get_read_pattern_R1_opposite_filepath():
    filepath = "/capsule/data/some_random_folder/gsm12345_other_identifiers_R1.fastq.gz"
    assert get_read_pattern(filepath, "2") == "R2.fastq.gz"


def test_get_read_pattern_R1_opposite_filepath_mismatch():
    filepath = "/capsule/data/some_random_folder/gsm12345_other_identifiers_R1.fastq.gz"
    assert not get_read_pattern(filepath, "2") == "R1.fastq.gz"


def test_get_read_pattern_R2_filepath():
    filepath = "/capsule/data/some_random_folder/gsm12345_other_identifiers_R1.fastq.gz"
    assert get_read_pattern(filepath, "2") == "R2.fastq.gz"


def test_get_read_pattern_R2_filepath_mismatch():
    filepath = "/capsule/data/some_random_folder/gsm12345_other_identifiers_R1.fastq.gz"
    assert not get_read_pattern(filepath, "2") == "R1.fastq.gz"


def test_get_read_pattern_R2_opposite_filepath():
    filepath = "/capsule/data/some_random_folder/gsm12345_other_identifiers_R1.fastq.gz"
    assert get_read_pattern(filepath, "1") == "R1.fastq.gz"


def test_get_read_pattern_R2_opposite_filepath_mismatch():
    filepath = "/capsule/data/some_random_folder/gsm12345_other_identifiers_R1.fastq.gz"
    assert not get_read_pattern(filepath, "1") == "R2.fastq.gz"


def test_get_read_pattern_singleend_filename():
    filename = "gsm12345.fastq.gz"
    assert get_read_pattern(filename) == "gsm12345.fastq.gz"


def test_get_read_pattern_singleend_filepath():
    filepath = "gsm12345.fastq.gz"
    assert get_read_pattern(filepath) == "gsm12345.fastq.gz"
