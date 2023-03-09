import pytest

from src.co-tools.co_utils import get_groups


@pytest.fixture
def mocker_samplesheet(mocker):
    # Read a mocked file
    mocked_sample_sheet = mocker.mock_open(
        read_data="case1,SRR10388935_R1.fastq.gz,SRR10388935_R2.fastq.gz\ncase1,SRR10388936_R1.fastq.gz,"
        + "SRR10388936_R2.fastq.gz\ncase2,SRR10388937_R1.fastq.gz,SRR10388937_R2.fastq.gz\ncase2,"
        + "SRR10388938_R1.fastq.gz,SRR10388938_R2.fastq.gz\ncontrol1,SRR10388939_R1.fastq.gz,"
        + "SRR10388939_R2.fastq.gz\ncontrol1,SRR10388940_R1.fastq.gz,SRR10388940_R2.fastq.gz\n"
        + "control2,SRR10388941_R1.fastq.gz,SRR10388941_R2.fastq.gz"
    )
    mocker.patch("builtins.open", mocked_sample_sheet)


# Tests for get_groups
def test_get_groups(mocker_samplesheet):
    groups = "case1,case2,control1,control2"
    assert get_groups("fakefile") == groups


def test_get_groups_fail(mocker_samplesheet):
    groups = "notcase1,notcase2,notcontrol1,notcontrol2"
    assert not get_groups("fakefile") == groups
