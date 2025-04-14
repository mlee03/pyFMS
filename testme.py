import os
import numpy as np
from mpi4py import MPI
import pyfms

input_nml = open("input.nml", "w")
input_nml.close()

cfms = pyfms.cFMS.lib
print(cfms)

cfms_do = pyfms.data_override.lib
print(cfms_do)

cfms_fms = pyfms.fms.lib
print(cfms_fms)

cfms_diag_manager = pyfms.diag_manager.lib
print(cfms_diag_manager)

cfms_horiz_interp = pyfms.horiz_interp.lib
print(cfms_horiz_interp)

cfms_grid_utils = pyfms.grid_utils.lib
print(cfms_horiz_interp)

cfms_mpp = pyfms.mpp.lib
print(cfms_mpp)

cfms_mpp_domains = pyfms.mpp_domains.lib
print(cfms_mpp_domains)

pyfms.fms.init(alt_input_nml_path=None,
                 localcomm=MPI.COMM_WORLD.Get_rank(),
                 ndomain=1,
                 nnest_domain=1,
                 calendar_type=None)

#pyfms.diag_manager.init()
#cfms_path = pyfms.cFMS.libpath
#cfms_path_do = pyfms.data_override.libpath


#assert(id(cfms)==id(cfms_do))
#assert(cfms_path == cfms_path_do)

#fake_path = "I/dont/exist"
#pyfms.cFMS.cfms_path = fake_path
#assert(pyfms.cFMS.lib()[0] is not fake_path)

#pyfms.pyFMS.init(

#pyfms.data_override.init()

os.remove("input.nml")
