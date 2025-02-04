import ctypes as ct
import os

from mpi4py import MPI

from pyfms import pyFMS


def test_pyfms_init():
    assert os.path.exists("./cFMS/libcFMS/.libs/libcFMS.so")

    fcomm = MPI.COMM_WORLD.py2f()

    pyfmsobj = pyFMS(
        localcomm=fcomm,
        clibFMS_path="./cFMS/libcFMS/.libs/libcFMS.so",
    )

    assert isinstance(pyfmsobj, pyFMS)

    pyfmsobj.set_pelist_npes(2)

    npes = ct.c_int.in_dll(pyfmsobj.clibFMS, "cFMS_pelist_npes")

    assert npes.value == 2

    pyfmsobj.pyfms_end()
