import pytest
from six import PY2


@pytest.fixture
def mocker_samplesheet(mocker):
    # Read a mocked file
    mocked_sample_sheet = mocker.mock_open(
        read_data="case1,SRR10388935_R1.fastq.gz,SRR10388935_R2.fastq.gz"
        + "\ncase1,SRR10388936_R1.fastq.gz,SRR10388936_R2.fastq.gz\ncase2,"
        + "SRR10388937_R1.fastq.gz,SRR10388937_R2.fastq.gz\ncase2,"
        + "SRR10388938_R1.fastq.gz,SRR10388938_R2.fastq.gz\ncontrol1,"
        + "SRR10388939_R1.fastq.gz,SRR10388939_R2.fastq.gz\ncontrol1,"
        + "SRR10388940_R1.fastq.gz,SRR10388940_R2.fastq.gz\ncontrol2,"
        + "SRR10388941_R1.fastq.gz,SRR10388941_R2.fastq.gz"
    )
    builtin_open = "__builtin__.open" if PY2 else "builtins.open"
    mocker.patch(builtin_open, mocked_sample_sheet)
