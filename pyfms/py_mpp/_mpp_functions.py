from ctypes import c_bool, c_char_p, c_double, c_float, c_int, POINTER
import numpy as np

ndptr = np.ctypeslib.ndpointer
C = "C_CONTIGUOUS"

def define(lib):

    #cFMS_set_pelist_npes
    lib.cFMS_set_pelist_npes.restype = None
    lib.cFMS_set_pelist_npes.argtypes = [POINTER(c_int)] #npes

    #cFMS_declare_pelist
    lib.cFMS_declare_pelist.restype = None
    lib.cFMS_declare_pelist.argtypes = [ndptr(dtype=np.int32, ndim=(1), flags=C), #pelist
                                        c_char_p #name
     ]

    #cFMS_error
    lib.cFMS_error.restype = None
    lib.cFMS_error.argtypes = [POINTER(c_int), #errortype
                               c_char_p        #errormsg
    ]

    #cFMS_get_current_pelist
    lib.cFMS_get_current_pelist.restype = None
    lib.cFMS_get_current_pelist.argtypes = [ndptr(dtype=np.int32, ndim=(1), flags=C), #pelist
                                            c_char_p,      #name
                                            POINTER(c_int) #commID
    ]

    #cFMS_npes
    lib.cFMS_npes.restype = c_int
    lib.cFMS_npes.argtypes = None

    #cFMS_pe
    lib.cFMS_pe.restype = c_int
    lib.cFMS_pe.argtypes = None

    #cFMS_set_current_pelist
    lib.cFMS_set_current_pelist.restype = None
    lib.cFMS_set_current_pelist.argtypes = [ndptr(dtype=np.int32, ndim=(1), flags=C), #pelist
                                            POINTER(c_bool) #no_sync
    ]

    
