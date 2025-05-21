from ctypes import c_bool, c_char_p, c_double, c_float, c_int, POINTER


def define(lib):

    #cFMS_init
    lib.cFMS_init.restype = None
    lib.cFMS_init.argtypes = [POINTER(c_int), #localcomm
                              c_char_p,       #alt_input_nml_path
                              POINTER(c_int), #ndomain
                              POINTER(c_int), #nnest_domain
                              POINTER(c_int)  #calendar_type
    ]

    #cFMS_end
    lib.cFMS_end.restype = None
    lib.cFMS_end.argtypes = None
    
