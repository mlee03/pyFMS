import ctypes as ct
import dataclasses
from typing import List, Optional

import numpy as np
import numpy.typing as npt

from pyfms.pyFMS_data_handling import *
from pyfms import pyFMS_mpp

@dataclasses.dataclass
class pyFMS_mpp_domains(pyFMS_mpp):
    clibFMS: ct.CDLL = None
    
    def pyfms_define_domains(
            self,
            global_indices: List[int], 
            layout: List[int], 
            domain_id: Optional[int] = None,
            pelist: Optional[List[int]]=None, 
            xflags: Optional[int]=None, 
            yflags: Optional[int]=None,
            xhalo: Optional[int]=None, 
            yhalo: Optional[int]=None, 
            xextent: Optional[List[int]]=None,
            yextent: Optional[List[int]]=None, 
            maskmap: Optional[npt.NDArray[np.bool_]]=None,
            name: Optional[str]=None, 
            symmetry: Optional[bool]=None, 
            memory_size: Optional[List[int]]=None,
            whalo: Optional[int]=None, 
            ehalo: Optional[int]=None, 
            shalo: Optional[int]=None,
            nhalo: Optional[int]=None, 
            is_mosaic: Optional[bool]=None, 
            tile_count: Optional[int]=None,
            tile_id: Optional[int]=None, 
            complete: Optional[bool]=None, 
            x_cyclic_offset: Optional[int]=None,
            y_cyclic_offset: Optional[int]=None
    ) :

        _cfms_define_domains = self.clibFMS.cFMS_define_domains

        global_indices_p, global_indices_t = setarray_Cint32(global_indices)
        layout_p, layout_t = setarray_Cint32(layout)
        domain_id_p, domain_id_t = setscalar_Cint32(domain_id)
        pelist_p, pelist_t = setarray_Cint32(pelist)    #array(:)
        xflags_p, xflags_t = setscalar_Cint32(xflags)
        yflags_p, yflags_t = setscalar_Cint32(yflags)
        xhalo_p, xhalo_t = setscalar_Cint32(xhalo)
        yhalo_p, yhalo_t = setscalar_Cint32(yhalo)
        xextent_p, xextent_t = setarray_Cint32(xextent) #array(:)
        yextent_p, yextent_t = setarray_Cint32(yextent) #array(:)
        maskmap_p, maskmap_t = setarray_Cbool(maskmap)  #array(:)
        name_p, name_t       = set_Cchar(name)
        symmetry_p, symmetry_t = setscalar_Cbool(symmetry)
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

        _cfms_define_domains.argtypes = [
            global_indices_t, 
            layout_t, 
            domain_id_t, 
            pelist_t, 
            xflags_t, 
            yflags_t,
            xhalo_t, 
            yhalo_t, 
            xextent_t, 
            yextent_t, 
            maskmap_t, 
            name_t, 
            symmetry_t,
            memory_size_t, 
            whalo_t, 
            ehalo_t, 
            shalo_t, 
            nhalo_t, 
            is_mosaic_t,
            tile_count_t, 
            tile_id_t, 
            complete_t, 
            x_cyclic_offset_t, 
            y_cyclic_offset_t
        ]

        _cfms_define_domains.restype = None

        _cfms_define_domains(
            global_indices_p, 
            layout_p, 
            domain_id_p, 
            pelist_p, 
            xflags_p, 
            yflags_p,
            xhalo_p, 
            yhalo_p, 
            xextent_p, 
            yextent_p, 
            maskmap_p, 
            name_p, 
            symmetry_p,
            memory_size_p, 
            whalo_p, 
            ehalo_p, 
            shalo_p, 
            nhalo_p, 
            is_mosaic_p,
            tile_count_p, 
            tile_id_p, 
            complete_p, 
            x_cyclic_offset_p, 
            y_cyclic_offset_p,
        )

    def pyfms_define_io_domain(self, io_layout: List[int], domain_id: Optional[int]=None):
        _cfms_define_io_domain = self.clibFMS.cFMS_define_io_domain

        io_layout_p, io_layout_t = setarray_Cint32(io_layout)
        domain_id_p, domain_id_t = setscalar_Cint32(domain_id)

        _cfms_define_io_domain.argtypes = [io_layout_t, domain_id_t]
        _cfms_define_io_domain.restype = None

        _cfms_define_io_domain(io_layout_p, domain_id_p)

    def pyfms_define_layout(self, global_indices: List[int], ndivs: int, layout: List[int]):
        _cfms_define_layout = self.clibFMS.cFMS_define_layout

        global_indices_p, global_indices_t = setarray_Cint32(global_indices)
        ndivs_p, ndivs_t = setscalar_Cint32(ndivs)
        layout_p, layout_t = setarray_Cint32(layout)

        _cfms_define_layout.argtypes = [global_indices_t, ndivs_t, layout_t]
        _cfms_define_layout.restype = None

        _cfms_define_layout(global_indices_p, ndivs_p, layout_p)

    def pyfms_define_nest_domains(
            self, 
            num_nest: int, 
            ntiles: int, 
            nest_level: List[int], 
            tile_fine: List[int], 
            tile_coarse: List[int],
            istart_coarse: List[int], 
            icount_coarse: List[int], 
            jstart_coarse: List[int], 
            jcount_coarse: List[int],
            npes_nest_tile: List[int], 
            x_refine: List[int], 
            y_refine: List[int], 
            nest_domain_id: Optional[int]=None,
            extra_halo: Optional[int]=None, 
            name: Optional[str]=None,
    ):
        _cfms_define_nest_domain = self.clibFMS.cFMS_define_nest_domain

        num_nest_p, num_nest_t = setarray_Cint32(num_nest)
        ntiles_p, ntiles_t = setscalar_Cint32(ntiles)
        nest_level_p, nest_level_t = setarray_Cint32(nest_level)
        tile_fine_p, tile_fine_t = setarray_Cint32(tile_fine)
        tile_coarse_p, tile_coarse_t = setarray_Cint32(tile_coarse)
        istart_coarse_p, istart_coarse_t = setarray_Cint32(istart_coarse)
        icount_coarse_p, icount_coarse_t = setarray_Cint32(icount_coarse)
        jstart_coarse_p, jstart_coarse_t = setarray_Cint32(jstart_coarse)
        jcount_coarse_p, jcount_coarse_t = setarray_Cint32(jcount_coarse)
        npes_nest_tile_p, npes_nest_tile_t = setarray_Cint32(npes_nest_tile)
        x_refine_p, x_refine_t = setarray_Cint32(x_refine)
        y_refine_p, y_refine_t = setarray_Cint32(y_refine)
        nest_domain_id_p, nest_domain_id_t = setscalar_Cint32(nest_domain_id)
        extra_halo_p, extra_halo_t = setscalar_Cint32(extra_halo)
        name_p, name_t = set_Cchar(name)

        _cfms_define_nest_domain.argtypes = [
            num_nest_t, 
            ntiles_t, 
            nest_level_t, 
            tile_fine_t, 
            tile_coarse_t, 
            istart_coarse_t, 
            icount_coarse_t, 
            jstart_coarse_t, 
            jcount_coarse_t, 
            npes_nest_tile_t, 
            x_refine_t,
            y_refine_t, 
            nest_domain_id_t, 
            extra_halo_t, 
            name_t
        ]
        _cfms_define_nest_domain.restype = None

        _cfms_define_nest_domain(
            num_nest_p, 
            ntiles_p, 
            nest_level_p, 
            tile_fine_p, 
            tile_coarse_p, 
            istart_coarse_p,
            icount_coarse_p, 
            jstart_coarse_p, 
            jcount_coarse_p, 
            npes_nest_tile_p, 
            x_refine_p, 
            y_refine_p, 
            nest_domain_id_p, 
            extra_halo_p, 
            name_p
        )

    def pyfms_domain_is_initialized(self, domain_id: Optional[int]=None) -> ct.c_bool:
        _cfms_domain_is_initialized = self.clibFMS.cFMS_domain_is_initialized

        domain_id_p, domain_id_t = setscalar_Cint32(domain_id)

        _cfms_domain_is_initialized.argtypes = [domain_id_t]
        _cfms_domain_is_initialized.restype = ct.c_bool
        
        return _cfms_domain_is_initialized(domain_id_p)
    
    def pyfms_get_compute_domain(
            self, 
            domain_id: Optional[int]=None, 
            xbegin: Optional[int]=None, 
            xend: Optional[int]=None,
            ybegin: Optional[int]=None, 
            yend: Optional[int]=None, 
            xsize: Optional[int]=None,
            xmax_size: Optional[int]=None,
            ysize: Optional[int]=None, 
            ymax_size: Optional[int]=None,
            x_is_global: Optional[bool]=None, 
            y_is_global: Optional[bool]=None,
            tile_count: Optional[int]=None,
            position: Optional[int]=None,
            whalo: Optional[int]=None,
            shalo: Optional[int]=None, 
    ):
        _cfms_get_compute_domain = self.clibFMS.cFMS_get_data_domain

        domain_id_p, domain_id_t = setscalar_Cint32(domain_id)
        xbegin_p, xbegin_t = setscalar_Cint32(xbegin)
        xend_p, xend_t = setscalar_Cint32(xend)
        ybegin_p, ybegin_t = setscalar_Cint32(ybegin)
        yend_p, yend_t = setscalar_Cint32(yend)
        xsize_p, xsize_t = setscalar_Cint32(xsize)
        xmax_size_p, xmax_size_t = setscalar_Cint32(xmax_size)
        ysize_p, ysize_t = setscalar_Cint32(ysize)
        ymax_size_p, ymax_size_t = setscalar_Cint32(ymax_size)
        x_is_global_p, x_is_global_t = setscalar_Cbool(x_is_global)
        y_is_global_p, y_is_global_t = setscalar_Cbool(y_is_global)
        tile_count_p, tile_count_t = setscalar_Cint32(tile_count)
        position_p, position_t = setscalar_Cint32(position)
        whalo_p, whalo_t = setscalar_Cint32(whalo)
        shalo_p, shalo_t = setscalar_Cint32(shalo)

        _cfms_get_compute_domain.argtypes = [
            domain_id_t, 
            xbegin_t, 
            xend_t, 
            ybegin_t, 
            yend_t, 
            xsize_t,
            xmax_size_t,
            ysize_t, 
            ymax_size_t,
            x_is_global_t, 
            y_is_global_t, 
            tile_count_t,
            position_t,
            whalo_t,
            shalo_t
        ]
        _cfms_get_compute_domain.restype = None

        _cfms_get_compute_domain(
            domain_id_p, 
            xbegin_p, 
            xend_p, 
            ybegin_p, 
            yend_p, 
            xsize_p,
            xmax_size_p,
            ysize_p, 
            ymax_size_p,
            x_is_global_p, 
            y_is_global_p, 
            tile_count_p,
            position_p,
            whalo_p,
            shalo_p,
        )

    def pyfms_get_data_domain(
            self, 
            domain_id: Optional[int]=None, 
            xbegin: Optional[int]=None, 
            xend: Optional[int]=None,
            ybegin: Optional[int]=None, 
            yend: Optional[int]=None, 
            xsize: Optional[int]=None,
            xmax_size: Optional[int]=None,
            ysize: Optional[int]=None, 
            ymax_size: Optional[int]=None,
            x_is_global: Optional[bool]=None, 
            y_is_global: Optional[bool]=None,
            tile_count: Optional[int]=None,
            position: Optional[int]=None,
            whalo: Optional[int]=None,
            shalo: Optional[int]=None, 
    ):
        _cfms_get_data_domain = self.clibFMS.cFMS_get_data_domain

        domain_id_p, domain_id_t = setscalar_Cint32(domain_id)
        xbegin_p, xbegin_t = setscalar_Cint32(xbegin)
        xend_p, xend_t = setscalar_Cint32(xend)
        ybegin_p, ybegin_t = setscalar_Cint32(ybegin)
        yend_p, yend_t = setscalar_Cint32(yend)
        xsize_p, xsize_t = setscalar_Cint32(xsize)
        xmax_size_p, xmax_size_t = setscalar_Cint32(xmax_size)
        ysize_p, ysize_t = setscalar_Cint32(ysize)
        ymax_size_p, ymax_size_t = setscalar_Cint32(ymax_size)
        x_is_global_p, x_is_global_t = setscalar_Cbool(x_is_global)
        y_is_global_p, y_is_global_t = setscalar_Cbool(y_is_global)
        tile_count_p, tile_count_t = setscalar_Cint32(tile_count)
        position_p, position_t = setscalar_Cint32(position)
        whalo_p, whalo_t = setscalar_Cint32(whalo)
        shalo_p, shalo_t = setscalar_Cint32(shalo)

        _cfms_get_data_domain.argtypes = [
            domain_id_t, 
            xbegin_t, 
            xend_t, 
            ybegin_t, 
            yend_t, 
            xsize_t,
            xmax_size_t,
            ysize_t, 
            ymax_size_t,
            x_is_global_t, 
            y_is_global_t, 
            tile_count_t,
            position_t,
            whalo_t,
            shalo_t
        ]
        _cfms_get_data_domain.restype = None

        _cfms_get_data_domain(
            domain_id_p, 
            xbegin_p, 
            xend_p, 
            ybegin_p, 
            yend_p, 
            xsize_p,
            xmax_size_p,
            ysize_p, 
            ymax_size_p,
            x_is_global_p, 
            y_is_global_p, 
            tile_count_p,
            position_p,
            whalo_p,
            shalo_p,
        )

    def pyfms_get_domain_name(self, domain_name: str, domain_id: Optional[int]=None):
        _cfms_get_domain_name = self.clibFMS.cFMS_get_domain_name

        domain_name_p, domain_name_t = set_Cchar(domain_name)
        domain_id_p, domain_id_t = setscalar_Cint32(domain_id)

        _cfms_get_domain_name.argtypes = [domain_name_t, domain_id_t]
        _cfms_get_domain_name.restype = None

        _cfms_get_domain_name(domain_name_p, domain_id_p)

    def pyfms_get_layout(self, layout: List[int], domain_id: Optional[int]=None):
        _cfms_get_layout = self.clibFMS.cFMS_get_layout

        layout_p, layout_t = setarray_Cint32(layout)
        domain_id_p, domain_id_t = setscalar_Cint32(domain_id)

        _cfms_get_layout.argtypes = [layout_t, domain_id_t]
        _cfms_get_layout.restype = None

        _cfms_get_layout(layout_p, domain_id_p)

    def pyfms_get_domain_pelist(self, pelist: List[int], domain_id: Optional[int]):
        _cfms_get_domain_pelist = self.clibFMS.cFMS_get_domain_pelist

        pelist_p, pelist_t = setarray_Cint32(pelist)
        domain_id_p, domain_id_t = setscalar_Cint32(domain_id)

        _cfms_get_domain_pelist.argtypes = [pelist_t, domain_id_t]
        _cfms_get_domain_pelist.restype = None

        _cfms_get_domain_pelist(pelist_p, domain_id_p)
    
    def pyfms_set_compute_domain(
            self, 
            domain_id: Optional[int]=None, 
            xbegin: Optional[int]=None, 
            xend: Optional[int]=None,
            ybegin: Optional[int]=None, 
            yend: Optional[int]=None, 
            xsize: Optional[int]=None,
            ysize: Optional[int]=None, 
            x_is_global: Optional[bool]=None, 
            y_is_global: Optional[bool]=None,
            tile_count: Optional[int]=None,
            whalo: Optional[int]=None,
            shalo: Optional[int]=None, 
    ):
        _cfms_set_compute_domain = self.clibFMS.cFMS_set_compute_domain

        domain_id_p, domain_id_t = setscalar_Cint32(domain_id)
        xbegin_p, xbegin_t = setscalar_Cint32(xbegin)
        xend_p, xend_t = setscalar_Cint32(xend)
        ybegin_p, ybegin_t = setscalar_Cint32(ybegin)
        yend_p, yend_t = setscalar_Cint32(yend)
        xsize_p, xsize_t = setscalar_Cint32(xsize)
        ysize_p, ysize_t = setscalar_Cint32(ysize)
        x_is_global_p, x_is_global_t = setscalar_Cbool(x_is_global)
        y_is_global_p, y_is_global_t = setscalar_Cbool(y_is_global)
        tile_count_p, tile_count_t = setscalar_Cint32(tile_count)
        whalo_p, whalo_t = setscalar_Cint32(whalo)
        shalo_p, shalo_t = setscalar_Cint32(shalo)

        _cfms_set_compute_domain.argtypes = [
            domain_id_t, 
            xbegin_t, 
            xend_t, 
            ybegin_t, 
            yend_t, 
            xsize_t,
            ysize_t, 
            x_is_global_t, 
            y_is_global_t, 
            tile_count_t,
            whalo_t,
            shalo_t
        ]
        _cfms_set_compute_domain.restype = None

        _cfms_set_compute_domain(
            domain_id_p, 
            xbegin_p, 
            xend_p, 
            ybegin_p, 
            yend_p, 
            xsize_p,
            ysize_p, 
            x_is_global_p, 
            y_is_global_p, 
            tile_count_p,
            whalo_p,
            shalo_p,
        )

    def pyfms_set_current_domain(self, domain_id: Optional[int]=None):
        _cfms_set_current_domain = self.clibFMS.cFMS_set_current_domain

        domain_id_p, domain_id_t = setscalar_Cint32(domain_id)

        _cfms_set_current_domain.argtypes = [domain_id_t]
        _cfms_set_current_domain.restype = None

        _cfms_set_current_domain(domain_id_p)

    def pyfms_set_current_nest_domain(self, nest_domain_id: Optional[int]=None):
        _cfms_set_current_nest_domain = self.clibFMS.cFMS_set_current_nest_domain

        nest_domain_id_p, nest_domain_id_t = setscalar_Cint32(nest_domain_id)

        _cfms_set_current_nest_domain.argtypes = [nest_domain_id_t]
        _cfms_set_current_nest_domain.restype = None

        _cfms_set_current_nest_domain(nest_domain_id_p)

    def pyfms_set_data_domain(
            self, 
            domain_id: Optional[int]=None, 
            xbegin: Optional[int]=None, 
            xend: Optional[int]=None,
            ybegin: Optional[int]=None, 
            yend: Optional[int]=None, 
            xsize: Optional[int]=None,
            ysize: Optional[int]=None, 
            x_is_global: Optional[bool]=None, 
            y_is_global: Optional[bool]=None,
            tile_count: Optional[int]=None,
            whalo: Optional[int]=None,
            shalo: Optional[int]=None,
    ):
        _cfms_set_data_domain = self.clibFMS.cFMS_set_data_domain

        domain_id_p, domain_id_t = setscalar_Cint32(domain_id)
        xbegin_p, xbegin_t = setscalar_Cint32(xbegin)
        xend_p, xend_t = setscalar_Cint32(xend)
        ybegin_p, ybegin_t = setscalar_Cint32(ybegin)
        yend_p, yend_t = setscalar_Cint32(yend)
        xsize_p, xsize_t = setscalar_Cint32(xsize)
        ysize_p, ysize_t = setscalar_Cint32(ysize)
        x_is_global_p, x_is_global_t = setscalar_Cbool(x_is_global)
        y_is_global_p, y_is_global_t = setscalar_Cbool(y_is_global)
        tile_count_p, tile_count_t = setscalar_Cint32(tile_count)
        whalo_p, whalo_t = setarray_Cint32(whalo)
        shalo_p, shalo_t = setarray_Cint32(shalo)

        _cfms_set_data_domain.argtypes = [
            domain_id_t, 
            xbegin_t, 
            xend_t, 
            ybegin_t, 
            yend_t, 
            xsize_t,
            ysize_t, 
            x_is_global_t, 
            y_is_global_t, 
            tile_count_t,
            whalo_t,
            shalo_t,
        ]
        _cfms_set_data_domain.restype = None

        _cfms_set_data_domain(
            domain_id_p, 
            xbegin_p, 
            xend_p, 
            ybegin_p, 
            yend_p, 
            xsize_p,
            ysize_p, 
            x_is_global_p, 
            y_is_global_p, 
            tile_count_p,
            whalo_p,
            shalo_p,
        )

    def pyfms_set_global_domain(
            self, 
            domain_id: Optional[int]=None, 
            xbegin: Optional[int]=None, 
            xend: Optional[int]=None,
            ybegin: Optional[int]=None, 
            yend: Optional[int]=None, 
            xsize: Optional[int]=None,
            ysize: Optional[int]=None, 
            tile_count: Optional[int]=None,
            whalo: Optional[int]=None,
            shalo: Optional[int]=None,

    ):
        _cfms_set_global_domain = self.clibFMS.cFMS_set_global_domain

        domain_id_p, domain_id_t = setscalar_Cint32(domain_id)
        xbegin_p, xbegin_t = setscalar_Cint32(xbegin)
        xend_p, xend_t = setscalar_Cint32(xend)
        ybegin_p, ybegin_t = setscalar_Cint32(ybegin)
        yend_p, yend_t = setscalar_Cint32(yend)
        xsize_p, xsize_t = setscalar_Cint32(xsize)
        ysize_p, ysize_t = setscalar_Cint32(ysize)
        tile_count_p, tile_count_t = setscalar_Cint32(tile_count)
        whalo_p, whalo_t = setscalar_Cint32(whalo)
        shalo_p, shalo_t = setscalar_Cint32(shalo)

        _cfms_set_global_domain.argtypes = [
            domain_id_t, 
            xbegin_t, 
            xend_t, 
            ybegin_t, 
            yend_t, 
            xsize_t,
            ysize_t, 
            tile_count_t,
            whalo_t,
            shalo_t,
        ]
        _cfms_set_global_domain.restype = None

        _cfms_set_global_domain(
            domain_id_p, 
            xbegin_p, 
            xend_p, 
            ybegin_p, 
            yend_p, 
            xsize_p,
            ysize_p, 
            tile_count_p,
            whalo_p,
            shalo_p,
        )

