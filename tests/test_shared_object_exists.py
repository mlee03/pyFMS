import os
import pytest

def test_file_exists():
    file_path = "./cFMS/libcFMS/.libs/libcFMS.so"
    assert os.path.exists(file_path)