import os
import numpy as np
from mpi4py import MPI
import pyfms

input_nml = open("input.nml", "w")
input_nml.close()

cfms = pyfms.cFMS.lib
cfms_do = pyfms.data_override.lib

cfms_path = pyfms.cFMS.libpath
cfms_path_do = pyfms.data_override.libpath

assert(id(cfms)==id(cfms_do))
assert(cfms_path == cfms_path_do)

#fake_path = "I/dont/exist"
#pyfms.cFMS.cfms_path = fake_path
#assert(pyfms.cFMS.lib()[0] is not fake_path)

#pyfms.pyFMS.init(alt_input_nml_path=None,
#                 localcomm=MPI.COMM_WORLD.Get_rank(),
#                 ndomain=1,
#                 nnest_domain=1,
#                 calendar_type=None)

#pyfms.data_override.init()

os.remove("input.nml")
