#!/usr/bin/env python3

import ctypes as c
import numpy as np
import dataclasses
import os
from pyfms.pyFMS_data_handling import *

#TODO:  get localcomm from pace
#TODO:  define domain via GFDL_atmos_cubed_sphere/tools/fv_mp_mod


@dataclasses.dataclass
class FMS() :

    clibFMS_path : str = None
    clibFMS : c.CDLL = None
    alt_input_nml_path : str = "input/input.nml"
    localcomm : int = None    
    
    def __post_init__(self) :

        if self.clibFMS_path == None :
            raise ValueError("Please define the library file path, e.g., as  libFMS(clibFMS_path=./clibFMS.so)")

        if not os.path.isfile(self.clibFMS_path) :
            raise ValueError(f"Library {self.clibFMS_path} does not exist")

        if self.clibFMS == None : self.clibFMS = c.cdll.LoadLibrary(self.clibFMS_path)
        
        self.fms_init(self.clibFMS, self.localcomm, self.alt_input_nml_path)

    def pyfms_init(self, clibFMS: c.CDLL=None, localcomm: int=None, alt_input_nml_path: str="input/input.nml") :
        _fms_init = clibFMS.cFMS_init
        localcomm_p, localcomm_t = setscalar_Cint32(localcomm)
        alt_input_nml_path_p, alt_input_nml_path_t = set_Cchar(alt_input_nml_path)
        _fms_init.argtypes = [ localcomm_t, alt_input_nml_path_t ]
        _fms_init.restype  = None
        _fms_init( localcomm_p, alt_input_nml_path_p )

    def pyfms_end(self):
        _fms_end = self.clibFMS.cFMS_end
        _fms_end()
        
    def pyfms_set_npes(self, npes_in: int=None):
        _fms_set_npes = self.clibFMS.cFMS_set_npes
        npes_in_p, npes_in_t = setscalar_Cint32(npes_in)
        _fms_set_npes.argtypes = [npes_in_t]
        _fms_set_npes.restype = None
        _fms_set_npes(npes_in_p)
        
    def define_domains2d(self, global_indices, layout, pelist=[None],
                         xflags=None, yflags=None, xhalo=None, yhalo=None, xextent=[None], yextent=[None],
                         maskmap=[None], name=None, symmetry=None, memory_size=[None],
                         whalo=None, ehalo=None, shalo=None, nhalo=None, is_mosaic=None, tile_count=None,
                         tile_id=None, complete=None, x_cyclic_offset=None, y_cyclic_offset=None) :

        _mpp_define_domains2d = self.clibFMS.cfms_define_domains2d

        global_indices_p, global_indices_t = setarray_Cint32(global_indices)
        layout_p, layout_t = setarray_Cint32(layout)
        
        pelist_p, pelist_t = setarray_Cint32(pelist)    #array(:)
        xflags_p, xflags_t = setscalar_Cint32(xflags)
        yflags_p, yflags_t = setscalar_Cint32(xflags)
        xhalo_p, xhalo_t = setscalar_Cint32(xflags)
        yhalo_p, yhalo_t = setscalar_Cint32(yflags)
        xextent_p, xextent_t = setarray_Cint32(xextent) #array(:)
        yextent_p, yextent_t = setarray_Cint32(yextent) #array(:)
        maskmap_p, maskmap_t = setarray_Cbool(maskmap)  #array(:)
        name_p, name_t       = set_Cchar(name)
        symmetry_p, symmetry_t       = setscalar_Cbool(symmetry)
        memory_size_p, memory_size_t = setarray_Cint32(memory_size) #array(:,:)
        whalo_p, whalo_t = setscalar_Cint32(whalo)
        ehalo_p, ehalo_t = setscalar_Cint32(ehalo)
        shalo_p, shalo_t = setscalar_Cint32(shalo)
        nhalo_p, nhalo_t = setscalar_Cint32(nhalo)
        is_mosaic_p, is_mosaic_t   = setscalar_Cbool(is_mosaic)
        tile_count_p, tile_count_t = setscalar_Cint32(tile_count)
        tile_id_p, tile_id_t   = setscalar_Cint32(tile_id)
        complete_p, complete_t = setscalar_Cbool(complete)
        x_cyclic_offset_p, x_cyclic_offset_t = setscalar_Cint32(x_cyclic_offset)
        y_cyclic_offset_p, y_cyclic_offset_t = setscalar_Cint32(y_cyclic_offset)    

        npelist,  npelist_t  = set_sizevars(pelist,1)
        nxextent, nxextent_t = set_sizevars(xextent,1)
        nyextent, nyextent_t = set_sizevars(yextent,1)
        nmaskmap, nmaskmap_t = set_sizevars(maskmap,2)        
        nmemory_size, nmemory_size_t = set_sizevars(memory_size,1)

        _mpp_define_domains2d.argtypes = [ global_indices_t, layout_t, *npelist_t, *nxextent_t, *nyextent_t,
                                           *nmaskmap_t, *nmemory_size_t, pelist_t, xflags_t, yflags_t,
                                           xhalo_t, yhalo_t, xextent_t, yextent_t, maskmap_t, name_t, symmetry_t,
                                           memory_size_t, whalo_t, ehalo_t, shalo_t, nhalo_t, is_mosaic_t, tile_count_t,
                                           tile_id_t, complete_t, x_cyclic_offset_t, y_cyclic_offset_t ]

        _mpp_define_domains2d.restype = None
        
        _mpp_define_domains2d( global_indices_p, layout_p, *npelist, *nxextent, *nyextent,
                               *nmaskmap, *nmemory_size, pelist_p, xflags_p, yflags_p,
                               xhalo_p, yhalo_p, xextent_p, yextent_p, maskmap_p, name_p, symmetry_p,
                               memory_size_p, whalo_p, ehalo_p, shalo_p, nhalo_p, is_mosaic_p, tile_count_p,
                               tile_id_p, complete_p, x_cyclic_offset_p, y_cyclic_offset_p )

        
    
