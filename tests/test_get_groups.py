import pytest

from src.co_tools.co_utils import get_groups


# Tests for get_groups
@pytest.mark.usefixtures("mocker_samplesheet")
def test_get_groups(mocker_samplesheet):
    groups = "case1,case2,control1,control2"
    assert get_groups("fakefile") == groups


@pytest.mark.usefixtures("mocker_samplesheet")
def test_get_groups_fail(mocker_samplesheet):
    groups = "notcase1,notcase2,notcontrol1,notcontrol2"
    assert not get_groups("fakefile") == groups
