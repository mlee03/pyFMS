import os


def test_shared_object_exists():
    assert os.path.exists("./cFMS/cLIBFMS/lib/libcFMS.so")
