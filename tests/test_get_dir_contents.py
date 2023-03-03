import subprocess

from src.codeoceanauxtools.get_dir_contents import get_dir_contents


# Tests for get_dir_contents
def test_get_dir_contents():
    cmd = ["find", "-L", "../data"]
    dir_contents = subprocess.check_output(cmd).decode("utf-8").strip()
    assert get_dir_contents() == dir_contents


def test_get_dir_contents_results():
    cmd = ["find", "-L", "../results"]
    dir_contents = subprocess.check_output(cmd).decode("utf-8").strip()
    assert get_dir_contents("../results") == dir_contents
