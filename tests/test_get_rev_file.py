from src.codeoceanauxtools.utils.util import get_rev_file


# Tests for get_rev_file
def test_get_rev_file_1_path():
    filepath = "/path/to/reads/gsm123_rep1_1.fastq.gz"
    assert get_rev_file(filepath) == "/path/to/reads/gsm123_rep1_2.fastq.gz"


def test_get_rev_file_2_path():
    filepath = "/path/to/reads/gsm123_rep1_2.fastq.gz"
    assert get_rev_file(filepath) == "/path/to/reads/gsm123_rep1_2.fastq.gz"


def test_get_rev_file_R1_path():
    filepath = "/path/to/reads/gsm123_rep1_R1.fastq.gz"
    assert get_rev_file(filepath) == "/path/to/reads/gsm123_rep1_R2.fastq.gz"


def test_get_rev_file_R2_path():
    filepath = "/path/to/reads/gsm123_rep1_R2.fastq.gz"
    assert get_rev_file(filepath) == "/path/to/reads/gsm123_rep1_R2.fastq.gz"


def test_get_rev_file_1():
    filepath = "gsm123_rep1_1.fastq.gz"
    assert get_rev_file(filepath) == "gsm123_rep1_2.fastq.gz"


def test_get_rev_file_2():
    filepath = "gsm123_rep1_2.fastq.gz"
    assert get_rev_file(filepath) == "gsm123_rep1_2.fastq.gz"


def test_get_rev_file_R1():
    filepath = "gsm123_rep1_R1.fastq.gz"
    assert get_rev_file(filepath) == "gsm123_rep1_R2.fastq.gz"


def test_get_rev_file_R2():
    filepath = "gsm123_rep1_R2.fastq.gz"
    assert get_rev_file(filepath) == "gsm123_rep1_R2.fastq.gz"


# def test_get_rev_file_single_end_path():
#     filepath = "/path/to/reads/gsm123rep1.fastq.gz"
#     assert get_rev_file(filepath) == "/path/to/reads/gsm123rep1.fastq.gz"
