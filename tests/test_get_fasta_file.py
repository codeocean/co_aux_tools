from pathlib import Path

from src.co_tools.co_fasta import find_extension, find_fasta_file

# Tests for find_extension
def test_generic_fasta():
    input_file = Path("/data/test.fa")
    assert str(find_extension(input_file)) == "/data/test.fa"


def test_generic_gzip():
    input_file = Path("/data/test.fa.gz")
    assert str(find_extension(input_file)) == "/data/test.fa.gz"


def test_faindex():
    input_file = Path("/data/test.fa.gz.fai")
    assert str(find_extension(input_file)) == ""


def test_nucleic_acid_fasta():
    input_file = Path("/data/test.fna")
    assert str(find_extension(input_file)) == "/data/test.fna"


def test_amino_acid_fasta():
    input_file = Path("/data/test.faa.gz")
    assert str(find_extension(input_file)) == "/data/test.faa.gz"


# Tests for find_fasta_file
# TODO
