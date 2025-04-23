import numpy as np
import os
import pyfms

def test_constants():

    inputnml = open("input.nml", "w")
    inputnml.close()
    
    lib = pyfms.pyFMS().cFMS
    constants_obj = pyfms.constants(cFMS=lib)

    assert(constants_obj.PI>np.double(3.14))

    os.remove("input.nml")
