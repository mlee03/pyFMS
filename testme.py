import os
import numpy as np
from mpi4py import MPI
import pyfms

input_nml = open("input.nml", "w")
input_nml.close()

cfms_path, cfms = pyfms.cFMS.getlib()
cfms_path_in_do, cfms_in_do = pyfms.pyDataOverride.getlib()

assert(cfms_path == cfms_path_in_do)
assert(id(cfms)==id(cfms_in_do))

fake_path = "I/dont/exist"
pyfms.cFMS.cfms_path = fake_path
assert(pyfms.cFMS.getlib()[0] is not fake_path)

pyfms.pyFMS.init(alt_input_nml_path=None,
                 localcomm=MPI.COMM_WORLD.Get_rank(),
                 ndomain=1,
                 nnest_domain=1,
                 calendar_type=None)

pyfms.pyDataOverride.init()

os.remove("input.nml")
