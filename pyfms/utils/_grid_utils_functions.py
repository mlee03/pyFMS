from ctypes import c_int, POINTER
import numpy as np

npptr = np.ctypeslib.ndpointer
C = "C_CONTIGUOUS"

def define(lib):

    lib.cFMS_get_grid_area.restype = None
    lib.cFMS_get_grid_area.argtypes = [
        POINTER(c_int),                            #nlon
        POINTER(c_int),                            #nlat
        npptr(dtype=np.float64, ndim=(1), flags=C),#lon
        npptr(dtype=np.float64, ndim=(1), flags=C),#lat
        npptr(dtype=np.float64, ndim=(1), flags=C) #area
    ]
                                       
