import pytest
from src.co_tools.co_fastq import get_rev_file



# def test_create_file(tmp_path):
#     d = tmp_path / "sub"
#     d.mkdir()
#     p = d / "hello.txt"
#     p.write_text(CONTENT)
#     assert p.read_text() == CONTENT
#     assert len(list(tmp_path.iterdir())) == 1
#     assert 0



@pytest.fixture(scope="session")
def fastq_file(tmp_path_factory):
    # img = compute_expensive_image()
    fastq = "gsm123_R1.fastq.gz"
    fn = tmp_path_factory.mktemp("data") / "gsm123_R1.fastq.gz"
    # fastq.save(fn)
    return fn.name



def test_get_rev_file_with_fixture(fastq_file):
    assert get_rev_file(fastq_file) == "gsm123_R2.fastq.gz"



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
