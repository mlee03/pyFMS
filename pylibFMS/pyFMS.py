#!/usr/bin/env python3

import ctypes as c
import numpy as np
import dataclasses
import os
from pyFMS_utils import *

#TODO:  get localcomm from pace
#TODO:  define domain via GFDL_atmos_cubed_sphere/tools/fv_mp_mod

@dataclasses.dataclass
class FMS() :

    pylibFMS_path : str = None
    pylibFMS : c.CDLL = None
    alt_input_nml_path : str = "input/input.nml"
    localcomm : int = None    
    
    def __post_init__(self) :

        if self.pylibFMS_path == None :
            raise ValueError("Please define the library file path, e.g., as  libFMS(pylibFMS_path=./pylibFMS.so)")

        if not os.path.isfile(self.pylibFMS_path) :
            raise ValueError(f"Library {self.pylibFMS_path} does not exist")

        if self.pylibFMS == None : self.pylibFMS = c.cdll.LoadLibrary(self.pylibFMS_path)
    
        _fms_init = getattr(self.pylibFMS, "__cfms_mod_MOD_cfms_fms_init")
        localcomm, localcomm_t = setargs_Cint32(self.localcomm)
        alt_input_nml_path, alt_input_nml_path_t = setargs_Cchar(self.alt_input_nml_path)

        _fms_init.argtypes = [ localcomm_t, alt_input_nml_path_t ]
        _fms_init.restype = None

        _fms_init(localcomm, alt_input_nml_path)
        
        
    def define_domains2d(self, global_indices, layout, pelist=None,
                         xflags=None, yflags=None, xhalo=None, yhalo=None, xextent=None, yextent=None,
                         maskmap=None, name=None, symmetry=None, memory_size=None,
                         whalo=None, ehalo=None, shalo=None, nhalo=None, is_mosaic=None, tile_count=None,
                         tile_id=None, complete=None, x_cyclic_offset=None, y_cyclic_offset=None) :

        _mpp_define_domains2d = getattr(self.libFMS, "__cfms_mod_MOD_cfms_define_domains2d")
        
        global_indices, global_indices_t = setargs_Cint32(global_indices)
        layout, layout_t = setargs_Cint32(layout)
        pelist, pelist_t = setargs_Cint32(pelist) #array(:)
        xflags, xflags_t = setargs_Cint32(xflags)
        yflags, yflags_t = setargs_Cint32(xflags)
        xhalo, xhalo_t = setargs_Cint32(xflags)
        yhalo, yhalo_t = setargs_Cint32(yflags)
        xextent, xextent_t = setargs_Cint32(xextent) #array(:)
        yextent, yextent_t = setargs_Cint32(yextent)
        maskmap, maskmap_t = setargs_Cbool(maskmap) #array(:)
        name, name_t = setargs_Cchar(name)
        symmetry, symmetry_t = setargs_Cbool(symmetry)
        memory_size, memory_size_t = setargs_Cint32(memory_size) #array(:,:)
        whalo, whalo_t = setargs_Cint32(whalo)
        ehalo, ehalo_t = setargs_Cint32(ehalo)
        shalo, shalo_t = setargs_Cint32(shalo)
        nhalo, nhalo_t = setargs_Cint32(nhalo)
        is_mosaic, is_mosaic_t = setargs_Cbool(is_mosaic)
        tile_count, tile_count_t = setargs_Cint32(tile_count)
        tile_id, tile_id_t = setargs_Cint32(tile_id)
        complete, complete_t = setargs_Cbool(complete)
        x_cyclic_offset, x_cyclic_offset_t = setargs_Cint32(x_cyclic_offset)
        y_cyclic_offset, y_cyclic_offset_t = setargs_Cint32(y_cyclic_offset)    

        npelist, npelist_t = setargs_size(pelist,1)
        nxextent, nxextent_t = setargs_size(xextent,1)
        nyextent, nyextent_t = setargs_size(yextent,1)
        nmaskmap, nmaskmap_t = setargs_size(maskmap,2)        
        nmemory_size, nmemory_size_t = setargs_size(memory_size,1)

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

        _mpp_get_layout2d = getattr(self.libFMS, "__cfms_mod_MOD_cfms_get_layout2d") 

        layout, layout_t = setargs_Cint32([1,1])

        _mpp_get_layout2d.argtypes = [ layout_t ]
        _mpp_get_layout2d.restype = None

        _mpp_get_layout2d(layout)

        return layout

        
    
