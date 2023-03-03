import os

from src.codeoceanauxtools.utils.util import is_pipeline


# Tests for is_pipeline
def test_is_pipeline_pipeline():
    os.environ["AWS_BATCH_JOB_ID"] = "123"
    assert is_pipeline()


def test_is_pipeline_capsule():
    del os.environ["AWS_BATCH_JOB_ID"]
    assert not is_pipeline()
