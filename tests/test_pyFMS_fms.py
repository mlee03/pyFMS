import os

from mpi4py import MPI

from pyfms import pyFMS


# @pytest.fixture(scope="session")
# def temp_file(tmpdir_factory):
#     file_path = tmpdir_factory.mktemp("data").join("input.nml")
#     yield file_path
#     os.remove(file_path)


def test_pyfms_init():
    assert os.path.exists("./cFMS/libcFMS/.libs/libcFMS.so")

    fcomm = MPI.COMM_WORLD.py2f()

    pyfmsobj = pyFMS(
        localcomm=fcomm,
        clibFMS_path="./cFMS/libcFMS/.libs/libcFMS.so",
    )

    # assert isinstance(pyfmsobj, pyFMS)

    pyfmsobj.pyfms_end()
