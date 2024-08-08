#!/usr/bin/env python3

from ctypes import *
import numpy as np

mpp_domain = cdll.LoadLibrary("./ndsl_fms.so")

global_indices = np.ctypeslib.as_array( np.array([1,1,1,1], dtype=np.int32) )
ndvis = c_int(1)
layout = np.ctypeslib.as_array( np.array([1,1], dtype=np.int32) )


#ndsl_mpp_define_layout2d = mpp_domain.__ndsl_mpp_domain_mod_MOD_ndsl_mpp_define_layout2d
#ndsl_mpp_define_layout2d.argtypes = [ np.ctypeslib.ndpointer(dtype=c_int, shape=(4,), flags="FORTRAN"),
#                                      POINTER(c_int),
#                                      np.ctypeslib.ndpointer(dtype=c_int, shape=(2,), flags="FORTRAN") ]
#ndsl_mpp_define_layout2d.restype = None
#ndsl_mpp_define_layout2d( global_indices, byref(ndvis), layout )

##

ndsl_mpp_define_domains2d = mpp_domain.__ndsl_mpp_domain_mod_MOD_ndsl_mpp_define_domains2d

global_indices_type = np.ctypeslib.ndpointer(dtype=c_int, shape=(4), flags="FORTRAN")
layout_type = np.ctypeslib.ndpointer(dtype=c_int, shape=(2), flags="FORTRAN")

n_pelist_type = POINTER(c_int)  ; n_pelist = c_int(0)
n_xextent_type = POINTER(c_int) ; n_xextent = c_int(0)
n_yextent_type = POINTER(c_int) ; n_yextent = c_int(0)
n1_maskmap_type = POINTER(c_int) ; n1_maskmap = c_int(0)
n2_maskmap_type = POINTER(c_int) ; n2_maskmap = c_int(0)
n_memory_size_type = POINTER(c_int)  ; n_memory_size = c_int(0)

if n_pelist.value > 0 :    
    pelist_type = np.ctypeslib.ndpointer(dtype=c_int, shape=(n_pelist.value), flags="FORTRAN")
    pelist = np.ctypeslib.as_array( np.array([1],dtype=np.int32) )
else :
    pelist_type = POINTER(c_int)
    pelist = None

xflags_type = POINTER(c_int) ; xflags = None
yflags_type = POINTER(c_int) ; yflags = None
xhalo_type  = POINTER(c_int) ; xhalo = None
yhalo_type  = POINTER(c_int) ; yhalo = None

if n_xextent.value > 0 :
    xextent_type = np.ctypeslib.ndpointer(dtype=c_int, shape=(n_xextent.value), flags="FORTRAN")
    xextent = np.ctypeslib.as_array( np.array([1], dtype=np.int32) )
else :
    xextent_type = POINTER(c_int)
    xextent = None

if n_yextent.value > 0 :    
    yextent_type = np.ctypeslib.ndpointer(dtype=c_int, shape=(n_yextent.value), flags="FORTRAN")
    yextent = np.ctypeslib.as_array( np.array([1], dtype=np.int32) )
else :
    yextent_type = POINTER(c_int)
    yextent = None

if n1_maskmap.value > 0 :
    maskmap_type = np.ctypeslib.ndpointer(dtype=c_bool, shape=(n1_maskmap.value, n2_maskmap.value), flags="FORTRAN")
    maskmap = np.ctypeslib.as_array( np.array([True], dtype=np.int32) )
else :
    maskmap_type = POINTER(c_bool)
    maskmap = None
 
name_type      = POINTER(c_char_p)  ; name = c_char_p(b"test")
symmetry_type  = POINTER(c_bool)    ; symmetry = None
is_mosaic_type = POINTER(c_bool)    ; is_mosaic = None

if n_memory_size.value > 0 :
    memory_size_type = np.ctypeslib.ndpointer(dtype=c_int, shape=(n_memory_size.value), flags="FORTRAN")
    memory_size=np.ctypeslib.as_array( np.array([1], dtype=np.int32) )
else :
    memory_size_type = POINTER(c_int)
    memory_size = None
    
whalo_type = POINTER(c_int) ; whalo = None
ehalo_type = POINTER(c_int) ; ehalo = None
shalo_type = POINTER(c_int) ; shalo = None
nhalo_type = POINTER(c_int) ; nhalo = None
tile_count_type = POINTER(c_int) ; tile_count = None
tile_id_type    = POINTER(c_int) ; tile_id = None
complete_type   = POINTER(c_bool) ; complete = None
x_cyclic_offset_type = POINTER(c_int) ; x_cyclic_offset = None
y_cyclic_offset_type = POINTER(c_int) ; y_cyclic_offset = None

ndsl_mpp_define_domains2d.argtypes = [ global_indices_type, layout_type, 
                                       n_pelist_type, n_xextent_type, n_yextent_type, n1_maskmap_type, n2_maskmap_type, n_memory_size_type, 
                                       pelist_type, xflags_type, yflags_type, xhalo_type, yhalo_type, xextent_type, yextent_type,
                                       maskmap_type, name_type, symmetry_type, 
                                       memory_size_type, whalo_type, ehalo_type, shalo_type, nhalo_type, is_mosaic_type, tile_count_type,
                                       tile_id_type, complete_type, x_cyclic_offset_type, y_cyclic_offset_type ]

ndsl_mpp_define_domains2d.restype = None

ndsl_mpp_define_domains2d(global_indices, layout,
                          n_pelist, n_xextent, n_yextent, n1_maskmap, n2_maskmap, n_memory_size, 
                          pelist, xflags, yflags, xhalo, yhalo,  xextent, yextent, maskmap, name, symmetry, 
                          memory_size, whalo, ehalo, shalo, nhalo, is_mosaic, tile_count, tile_id, 
                          complete, x_cyclic_offset, y_cyclic_offset)

                                       




