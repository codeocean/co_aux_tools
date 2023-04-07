import subprocess
from pathlib import Path

import pytest

# from testfixtures import TempDirectory
from src.co_tools.co_fastq import get_fwd_fastqs

# Tests for get_fwd_fastqs

@pytest.mark.usefixtures("fastq_dir")
def test_get_fwd_fastqs(fastq_dir):
    fastq_files = ["gsm123_R1.fastq.gz", "gsm124_R1.fastq.gz"]
    if returned_files := get_fwd_fastqs(fastq_dir):
        for i, x in enumerate(returned_files.split("\n")):
            fastq = Path(x).name
            assert fastq == fastq_files[i]
