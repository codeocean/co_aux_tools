from pathlib import Path

import pytest

from src.co_tools.co_fastq import get_fastqs


@pytest.mark.usefixtures("fastq_dir")
def test_get_fwd_true_fastqs(fastq_dir):
    fastq_files = ["gsm123_R1.fastq.gz", "gsm124_R1.fastq.gz"]
    if returned_files := get_fastqs(fwd="true", dir=fastq_dir):
        for i, x in enumerate(returned_files.split("\n")):
            fastq = Path(x).name
            assert fastq == fastq_files[i]


@pytest.mark.usefixtures("fastq_dir")
def test_get_fwd_fwd_fastqs(fastq_dir):
    fastq_files = ["gsm123_R1.fastq.gz", "gsm124_R1.fastq.gz"]
    if returned_files := get_fastqs(fwd="fwd", dir=fastq_dir):
        for i, x in enumerate(returned_files.split("\n")):
            fastq = Path(x).name
            assert fastq == fastq_files[i]


@pytest.mark.usefixtures("fastq_dir")
def test_get_all_fastqs(fastq_dir):
    fastq_files = [
        "gsm123_R1.fastq.gz",
        "gsm123_R2.fastq.gz",
        "gsm124_R1.fastq.gz",
        "gsm124_R2.fastq.gz",
    ]
    if returned_files := get_fastqs("", fastq_dir):
        for i, x in enumerate(returned_files.split("\n")):
            fastq = Path(x).name
            assert fastq == fastq_files[i]
