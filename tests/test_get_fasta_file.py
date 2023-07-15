from pathlib import Path

from src.co_tools.co_fasta import find_extension


# Tests for find_extension
def test_generic_fasta():
    input_file = "/data/test.fa"
    assert str(find_extension(input_file)) == "/data/test.fa"


def test_generic_gzip():
    input_file = "/data/test.fa.gz"
    assert str(find_extension(input_file)) == "/data/test.fa.gz"


def test_faindex():
    input_file = "/data/test.fa.gz.fai"
    assert not str(find_extension(input_file))


def test_nucleic_acid_fasta():
    input_file = "/data/test.fna"
    assert str(find_extension(input_file)) == "/data/test.fna"


def test_amino_acid_fasta():
    input_file = "/data/test.faa.gz"
    assert str(find_extension(input_file)) == "/data/test.faa.gz"


def test_period_in_fasta():
    input_file = "/data/ENSG0001.1.fa.gz"
    assert str(find_extension(input_file)) == "/data/ENSG0001.1.fa.gz"


# Path
def test_generic_fasta_Path():
    input_file = Path("/data/test.fa")
    assert not str(find_extension(input_file)) == "/data/test.fa"


def test_generic_gzip_Path():
    input_file = Path("/data/test.fa.gz")
    assert not str(find_extension(input_file)) == "/data/test.fa.gz"


def test_faindex_Path():
    input_file = Path("/data/test.fa.gz.fai")
    assert not str(find_extension(input_file))


def test_nucleic_acid_fasta_Path():
    input_file = Path("/data/test.fna")
    assert not str(find_extension(input_file)) == "/data/test.fna"


def test_amino_acid_fasta_Path():
    input_file = Path("/data/test.faa.gz")
    assert not str(find_extension(input_file)) == "/data/test.faa.gz"


def test_period_in_fasta_Path():
    input_file = Path("/data/ENSG0001.1.fa.gz")
    assert not str(find_extension(input_file)) == "/data/ENSG0001.1.fa.gz"


# TODO
# Tests for find_fasta_file
