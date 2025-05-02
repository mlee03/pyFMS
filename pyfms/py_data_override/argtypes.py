import ctypes
import numpy as np

data_override_init = [ctypes.POINTER(ctypes.c_int), #atm_domain_id
                      ctypes.POINTER(ctypes.c_int), #ocn_domain_id
                      ctypes.POINTER(ctypes.c_int), #ice_domain_id
                      ctypes.POINTER(ctypes.c_int), #land_domain_id
                      ctypes.POINTER(ctypes.c_int), #land_domainUG_id
                      ctypes.POINTER(ctypes.c_int)  #mode
]

data_override_set_time = [ctypes.POINTER(ctypes.c_int), #year
                          ctypes.POINTER(ctypes.c_int), #month
                          ctypes.POINTER(ctypes.c_int), #day
                          ctypes.POINTER(ctypes.c_int), #hour
                          ctypes.POINTER(ctypes.c_int), #minute
                          ctypes.POINTER(ctypes.c_int), #second
                          ctypes.POINTER(ctypes.c_int), #tick
                          ctypes.c_char_p
]

data_override_scalar = [ctypes.c_char_p, #gridname
                        ctypes.c_char_p, #fieldname,
                        ctypes.POINTER(ctypes.c_double), #data
                        ctypes.POINTER(ctypes.c_bool), #override
                        ctypes.POINTER(ctypes.c_int) #data_index
]

data_override = [ctypes.c_char_p, #gridname
                 ctypes.c_char_p, #fieldname
                 None,            #data_shape
                 None,            #data
                 ctypes.POINTER(ctypes.c_bool), #override
                 ctypes.POINTER(ctypes.c_int),  #is
                 ctypes.POINTER(ctypes.c_int),  #ie
                 ctypes.POINTER(ctypes.c_int),  #js
                 ctypes.POINTER(ctypes.c_int)   #je
]
