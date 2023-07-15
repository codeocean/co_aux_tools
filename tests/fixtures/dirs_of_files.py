from pathlib import Path

import pytest


@pytest.fixture()
def fastq_dir(tmp_path):
    fastq_files = [
        "gsm123_R1.fastq.gz",
        "gsm123_R2.fastq.gz",
        "gsm124_R1.fastq.gz",
        "gsm124_R2.fastq.gz",
    ]
    d = tmp_path / "fastqdir"
    d.mkdir()
    for fastq in fastq_files:
        Path(f"{d}/{fastq}").touch()
    assert Path(d).is_dir()
    return d


@pytest.fixture()
def results_dir(tmp_path):
    fastq_files = [
        "gsm123_trimmed_R1.fastq.gz",
        "gsm123_trimmed_R2.fastq.gz",
        "gsm_counts_matrix.tsv"
        "gsm123_qc_report.html"
        "gsm123_qc_report.json"
        "gsm124_R1.fastq.gz",
        "gsm124_R2.fastq.gz",
    ]
    d = tmp_path / "fastqdir"
    d.mkdir()
    for fastq in fastq_files:
        Path(f"{d}/{fastq}").touch()
    assert Path(d).is_dir()
    return d
