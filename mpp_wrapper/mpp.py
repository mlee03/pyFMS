#!/usr/bin/env python3

import ctypes as c
import numpy as np
import dataclasses


def setarg_i4(arg) :
    if arg == None :
        arg_t = c.POINTER(c.c_int)
    else :
        arg = [arg] if len(arg) == 0 else arg
        arg = np.ctypeslib.as_array( np.array(arg, dtype=np.int32) )
        arg_t = np.ctypeslib.ndpointer( dtype=c.c_int, shape=np.shape(arg), flags='FORTRAN')
    return arg, arg_t

def setarg_r4(arg) :
    if arg == None :
        arg_t = c.POINTER(c.c_float32)
    else :
        arg = [arg] if len(arg) == 0 else arg
        arg = np.ctypeslib.as_array( np.array(arg, dtype=np.float32) )
        arg_t = np.ctypeslib.ndpointer( dtype=c.c_float, shape=np.shape(arg), flags='FORTRAN')
    return arg, arg_t

def setarg_r8(arg) :
    if arg == None :
        arg_t = c.POINTER(c.c_double)
    else :
        arg = [arg] if len(arg) == 0 else arg
        arg = np.ctypeslib.as_array( np.array(arg, dtype=np.floag64) )
        arg_t = np.ctypeslib.ndpointer( dtype=c.c_double, shape=np.shape(arg), flags='FORTRAN')
    return arg, arg_t

def setarg_c(arg) :
    if arg == None :
        arg_t = c.POINTER(c.c_char_p)
    else :
        arg = c.byref( c.c_char_p( arg.encode('ascii') ) )
        arg_t = c.POINTER(c.c_char_p)
    return arg, arg_t

def setarg_bool(arg) :
    if arg == None :
        arg_t = c.POINTER(c.c_bool)
    else :
        arg = [arg] if len(arg) == 0 else arg
        arg = np.ctypeslib.as_array( np.array(arg, dtype=np.bool) )
        arg_t = np.ctypeslib.ndpointer( dtype=c.c_bool, shape=np.shape(arg), flags='FORTRAN')
    return arg, arg_t


def setarg_size(arg, ndim) :
    if arg == None :
        argsize = [ c.byref(c.c_int(1)) for i in range(ndim) ]
        argsize_t = [ c.POINTER(c.c_int) for i in range(ndim) ]
    else :
        argsize = [ c.byref(c.c_int(isize)) for isize in np.shape(arg) ]
        argsize_t = [ c.POINTER(c.c_int) for i in range(ndim) ]
    return argsize, argsize_t


@dataclasses.dataclass
class MPP() :

    libFMS : c.CDLL = None
    
    def init(self, flags=None, localcomm=None, test_level=None, alt_input_nml_path=None) :

        _mpp_init = getattr(self.libFMS, "__py_mpp_mod_MOD_py_mpp_init")
        
        flags, flags_t = setarg_i4(flags)
        localcomm, localcomm_t = setarg_i4(localcomm)
        test_level, test_level_t = setarg_i4(test_level)
        alt_input_nml_path, alt_input_nml_path_t = setarg_c(alt_input_nml_path)
        
        _mpp_init.argtypes = [ flags_t, localcomm_t, test_level_t, alt_input_nml_path_t ]
        _mpp_init.restype = None
        
        _mpp_init( flags, localcomm, test_level, alt_input_nml_path )

        
    def define_domains2d(self, global_indices, layout, pelist=None,
                         xflags=None, yflags=None, xhalo=None, yhalo=None, xextent=None, yextent=None,
                         maskmap=None, name=None, symmetry=None, memory_size=None,
                         whalo=None, ehalo=None, shalo=None, nhalo=None, is_mosaic=None, tile_count=None,
                         tile_id=None, complete=None, x_cyclic_offset=None, y_cyclic_offset=None) :

        _mpp_define_domains2d = getattr(self.libFMS, "__py_mpp_mod_MOD_py_mpp_define_domains2d")
        
        global_indices, global_indices_t = setarg_i4(global_indices)
        layout, layout_t = setarg_i4(layout)
        pelist, pelist_t = setarg_i4(pelist) #array(:)
        xflags, xflags_t = setarg_i4(xflags)
        yflags, yflags_t = setarg_i4(xflags)
        xhalo, xhalo_t = setarg_i4(xflags)
        yhalo, yhalo_t = setarg_i4(yflags)
        xextent, xextent_t = setarg_i4(xextent) #array(:)
        yextent, yextent_t = setarg_i4(yextent)
        maskmap, maskmap_t = setarg_bool(maskmap) #array(:)
        name, name_t = setarg_c(name)
        symmetry, symmetry_t = setarg_bool(symmetry)
        memory_size, memory_size_t = setarg_i4(memory_size) #array(:,:)
        whalo, whalo_t = setarg_i4(whalo)
        ehalo, ehalo_t = setarg_i4(ehalo)
        shalo, shalo_t = setarg_i4(shalo)
        nhalo, nhalo_t = setarg_i4(nhalo)
        is_mosaic, is_mosaic_t = setarg_bool(is_mosaic)
        tile_count, tile_count_t = setarg_i4(tile_count)
        tile_id, tile_id_t = setarg_i4(tile_id)
        complete, complete_t = setarg_bool(complete)
        x_cyclic_offset, x_cyclic_offset_t = setarg_i4(x_cyclic_offset)
        y_cyclic_offset, y_cyclic_offset_t = setarg_i4(y_cyclic_offset)    

        npelist, npelist_t = setarg_size(pelist,1)
        nxextent, nxextent_t = setarg_size(xextent,1)
        nyextent, nyextent_t = setarg_size(yextent,1)
        nmaskmap, nmaskmap_t = setarg_size(maskmap,2)        
        nmemory_size, nmemory_size_t = setarg_size(memory_size,1)

        _mpp_define_domains2d.argtypes = [ global_indices_t, layout_t, *npelist_t, *nxextent_t, *nyextent_t,
                                           *nmaskmap_t, *nmemory_size_t, pelist_t, xflags_t, yflags_t,
                                           xhalo_t, yhalo_t, xextent_t, yextent_t, maskmap_t, name_t, symmetry_t,
                                           memory_size_t, whalo_t, ehalo_t, shalo_t, nhalo_t, is_mosaic_t, tile_count_t,
                                           tile_id_t, complete_t, x_cyclic_offset_t, y_cyclic_offset_t ]

        _mpp_define_domains2d.restype = None

        _mpp_define_domains2d( global_indices, layout, *npelist, *nxextent, *nyextent,
                               *nmaskmap, *nmemory_size, pelist, xflags, yflags,
                               xhalo, yhalo, xextent, yextent, maskmap, name, symmetry,
                               memory_size, whalo, ehalo, shalo, nhalo, is_mosaic, tile_count,
                               tile_id, complete, x_cyclic_offset, y_cyclic_offset )

    def get_layout2d(self) :

        _mpp_get_layout2d = getattr(self.libFMS, "__py_mpp_mod_MOD_py_mpp_get_layout2d") 

        layout, layout_t = setarg_i4([1,1])

        _mpp_get_layout2d.argtypes = [ layout_t ]
        _mpp_get_layout2d.restype = None

        _mpp_get_layout2d(layout)

        return layout

        
