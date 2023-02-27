from multiprocessing import cpu_count
import pytest
import subprocess

from ..get_cpu_count import get_cpu_limit
from ..get_dir_contents import get_dir_contents
from ..get_groups import get_groups


# @pytest.fixture
# def sample_sheet(tmp_path):
#     # create your file manually here using the tmp_path fixture
#     # or just import a static pre-built mock file
#     # something like :
#     target_output = os.path.join(tmp_path,'mydoc.csv')
#     with open(target_output, 'w+'):
#         # write stuff here
#     return target_output


@pytest.fixture
def mocker_samplesheet(mocker):
    # Read a mocked /etc/release file
    mocked_sample_sheet = mocker.mock_open(
        read_data="case1,SRR10388935_R1.fastq.gz,SRR10388935_R2.fastq.gz\ncase1,SRR10388936_R1.fastq.gz,"
        + "SRR10388936_R2.fastq.gz\ncase2,SRR10388937_R1.fastq.gz,SRR10388937_R2.fastq.gz\ncase2,"
        + "SRR10388938_R1.fastq.gz,SRR10388938_R2.fastq.gz\ncontrol1,SRR10388939_R1.fastq.gz,"
        + "SRR10388939_R2.fastq.gz\ncontrol1,SRR10388940_R1.fastq.gz,SRR10388940_R2.fastq.gz\n"
        + "control2,SRR10388941_R1.fastq.gz,SRR10388941_R2.fastq.gz"
    )
    mocker.patch("builtins.open", mocked_sample_sheet)


# Tests for get_cpu_count
def test_v210_capsule():
    co_cpus = 3
    aws_batch_job_id = None
    assert get_cpu_limit(co_cpus, aws_batch_job_id) == 3


def test_v210_pipeline():
    co_cpus = 3
    aws_batch_job_id = "123456"
    assert get_cpu_limit(co_cpus, aws_batch_job_id) == 3


def test_v29_capsule():
    co_cpus = None
    aws_batch_job_id = None
    assert get_cpu_limit(co_cpus, aws_batch_job_id) == cpu_count()


def test_v29_pipeline():
    co_cpus = None
    aws_batch_job_id = "123456"
    assert get_cpu_limit(co_cpus, aws_batch_job_id) == 1


# Tests for get_dir_contents
def test_get_dir_contents():
    cmd = ["find", "-L", "../data"]
    dir_contents = subprocess.check_output(cmd).decode("utf-8").strip()
    assert get_dir_contents() == dir_contents


def test_get_dir_contents_results():
    cmd = ["find", "-L", "../results"]
    dir_contents = subprocess.check_output(cmd).decode("utf-8").strip()
    assert get_dir_contents("../results") == dir_contents


# TODO
# Tests for get_fasta_file


# Tests for get_groups
def test_get_groups(mocker_samplesheet):
    groups = "case1,case2,control1,control2"
    assert get_groups("fakefile") == groups
    
    
def test_get_groups_fail(mocker_samplesheet):
    groups = "notcase1,notcase2,notcontrol1,notcontrol2"
    assert not get_groups("fakefile") == groups
