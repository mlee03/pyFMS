import os

import pytest

import pyfms


def test_write_module():
    myfile = open("module1.py", "w")
    myfile.write(
        """
import pyfms
class Module1Class():
    module1_lib_id = id(pyfms.cfms.lib())
        """
    )
    myfile.close()


def test_share_same_library():

    """
    Test to ensure pyfms modules use the same
    ctypes CDLL library object
    """

    assert id(pyfms.cfms._lib) == id(pyfms.mpp_domains._lib)


def test_load_library_same_object():

    """
    Test to ensure the ctypes CDLL Library object
    is instantiated only once
    """

    import module1

    myclass = module1.Module1Class()
    assert id(pyfms.cfms.lib()) == myclass.module1_lib_id


@pytest.mark.xfail
def test_library_load_fail():

    """
    Partial test to ensure the changelib function
    works
    """

    pyfms.cfms.changelib(libpath="do_not_exist")


def test_remove_module():
    os.remove("module1.py")


if __name__ == "__main__":
    test_write_module()
