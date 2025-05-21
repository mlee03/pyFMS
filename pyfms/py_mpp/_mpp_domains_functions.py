from ctypes import c_bool, c_char_p, c_double, c_float, c_int, POINTER
import numpy as np

ndptr = np.ctypeslib.ndpointer
C = "C_CONTIGUOUS"

def define(lib):

    #cFMS_get_compute/data_domain
    #cFMS_set_comupte/data_domain
    for function in [lib.cFMS_get_compute_domain,
                     lib.cFMS_get_data_domain,
                     lib.cFMS_set_compute_domain,
                     lib.cFMS_set_data_domain,
                     lib.cFMS_set_global_domain]
                     
    function.restype = None
    function.argtypes = [POINTER(c_int),  #domain_id
                         POINTER(c_int),  #xbegin
                         POINTER(c_int),  #xend
                         POINTER(c_int),  #ybegin
                         POINTER(c_int),  #yend
                         POINTER(c_int),  #xsize
                         POINTER(c_int),  #xmax_size
                         POINTER(c_int),  #ysize
                         POINTER(c_int),  #ymax_size
                         POINTER(c_bool), #x_is_global
                         POINTER(c_bool), #y_is_global                         
                         POINTER(c_int),  #tile_count
                         POINTER(c_int),  #position
                         POINTER(c_int),  #whalo
                         POINTER(c_int),  #shalo
    ]


    #cFMS_define_domains
    lib.cFMS_define_domains.restype = c_int
    lib.cFMS_define_domains.argtypes = [
        ndptr(dtype=np.int32, shape=(4), flags=C), #global_indices
        ndptr(dtype=np.int32, shape=(2), flags=C), #layout
        POINTER(c_int),                            #npelist
        ndptr(dtype=np.int32, ndim=(1), flags=C),  #pelist
        POINTER(c_int),                            #xflags
        POINTER(c_int),                            #yflags
        POINTER(c_int),                            #xhalo
        POINTER(c_int),                            #yhalo
        ndptr(dtype=np.int32, ndim=(1), flags=C),  #xextent
        ndptr(dtype=np.int32, ndim=(1), flags=C),  #yextent
        ndptr(dtype=np.int32, ndim=(2), flags=C),  #maskmap
        c_char_p,                                  #name
        POINTER(c_bool),                           #symmetry
        ndptr(dtype=np.int32, shape(2), flags=C),  #memory_size
        POINTER(c_int),                            #whalo
        POINTER(c_int),                            #ehalo
        POINTER(c_int),                            #shalo
        POINTER(c_int),                            #nhalo
        POINTER(c_bool),                           #is_mosaic
        POINTER(c_int),                            #tile_count
        POINTER(c_int),                            #tile_id
        POINTER(c_bool),                           #complete
        POINTER(c_int),                            #x_cyclic_offset
        POINTER(c_int),                            #y_cyclic_offset
    ]

    #cFMS_define_io_domain
    lib.cFMS_define_io_domain.restype = None
    lib.cFMS_define_io_domain.argtypes = [
        ndptr(dtype=np.int32, shape=(2), flags=C), #io_layout
        POINTER(c_int) #domain_id
    ]

    #cFMS_define_layout
    lib.cFMS_define_layout.restype = None
    lib.cFMS_define_layout.argtypes = [
        ndptr(dtype=np.int32, shape=(4), flags=C), #global_indices
        POINTER(c_int),                            #ndivs
        ndptr(dtype=np.int32, shape=(2), flags=C), #layout
    ]

    #cFMS_define_nest_domains
    lib.cFMS_define_nest_domains.restype = c_int
    lib.cFMS_define_nest_domains.argtypes = [
        POINTER(c_int),                           #num_nest
        POINTER(c_int),                           #ntiles
        ndptr(dtype=np.int32, ndim=(1), flags=C), #nest_level
        ndptr(dtype=np.int32, ndim=(1), flags=C), #tile_fine
        ndptr(dtype=np.int32, ndim=(1), flags=C), #tile_corase
        ndptr(dtype=np.int32, ndim=(1), flags=C), #istart_coarse
        ndptr(dtype=np.int32, ndim=(1), flags=C), #icount_coarse
        ndptr(dtype=np.int32, ndim=(1), flags=C), #jstart_coarse
        ndptr(dtype=np.int32, ndim=(1), flags=C), #jcount_coarse
        ndptr(dtype=np.int32, ndim=(1), flags=C), #npes_nest_tiles
        ndptr(dtype=np.int32, ndim=(1), flags=C), #x_refine
        ndptr(dtype=np.int32, ndim=(1), flags=C), #y_refine
        POINTER(c_int),                           #domain_id
        POINTER(c_int),                           #extra_halo
        c_char_p                                  #name
    ]

    #cFMS_domain_is_initialized
    lib.cFMS_domain_is_initialized.restype = c_bool
    lib.cFMS_domain_is_initialized.argtypes = [POINTER(c_int)] #domain_id

    #cFMS_get_domain_name
    lib.cFMS_get_domain_name.restype = None
    lib.cFMS_get_domain_name.argtypes = [c_char_p,      #name
                                         POINTER(c_int) #domain_id
    ]

    #cFMS_get_layout
    lib.cFMS_get_layout.restype = None
    lib.cFMS_get_layout.argtypes = [
        ndptr(dtype=np.int32, shape=(2), flags=C), #layout
        POINTER(c_int) #domain_id
    ]

    #cFMS_get_domain_pelist
    lib.cFMS_get_domain_pelist.restype = None
    lib.cFMS_get_domain_pelist.argtypes = [
        ndptr(dtype=np.int32, ndim=1, order=C), #pelist
        POINTER(c_int)                          #domain_id
    ]
              
    #cFMS_set_current_domain
    lib.cFMS_set_current_domain.restype = None
    lib.cFMS_set_current_domain.argtypes = [POINTER(c_int)] #domain_id

    #cFMS_set_current_nest_domain
    lib.cFMS_set_current_domain.restype = None
    lib.cFMS_set_current_domain.argtypes = [POINTER(c_int)] #domain_id


