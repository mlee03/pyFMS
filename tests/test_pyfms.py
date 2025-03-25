import os

from mpi4py import MPI

from pyfms import pyFMS


cfms_path = os.path.dirname(__file__) + "/../cFMS/cLIBFMS/lib/libcFMS.so"


def test_pyfms_init():

    assert os.path.exists(cfms_path)

    fcomm = MPI.COMM_WORLD.py2f()

    pyfmsobj = pyFMS(
        localcomm=fcomm,
        cFMS_path=cfms_path,
    )

    assert isinstance(pyfmsobj, pyFMS)

    pyfmsobj.pyfms_end()
