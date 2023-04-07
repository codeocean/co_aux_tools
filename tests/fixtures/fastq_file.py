import pytest


@pytest.fixture(scope="session")
def fastq_file_fwd(tmp_path_factory):
    fn = tmp_path_factory.mktemp("data") / "gsm123_R1.fastq.gz"
    return fn


@pytest.fixture(scope="session")
def fastq_file_single_end(tmp_path_factory):
    fn = tmp_path_factory.mktemp("data") / "gsm123.fastq.gz"
    return fn
