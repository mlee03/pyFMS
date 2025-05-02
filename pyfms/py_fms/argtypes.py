import ctypes

fms_init = [ctypes.POINTER(ctypes.c_int), #localcomm
            ctypes.c_char_p,              #alt_input_nml_Path
            ctypes.POINTER(ctypes.c_int), #ndomain
            ctypes.POINTER(ctypes.c_int), #nnest_domain,
            ctypes.POINTER(ctypes.c_int)  #calendar_type
]
