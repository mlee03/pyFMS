import ctypes as ct
import dataclasses
from typing import Optional

import numpy as np
from numpy.typing import NDArray

from pyfms import pyFMS_mpp
from pyfms.pyFMS_data_handling import (
    set_Cchar,
    set_multipointer,
    setarray_Cint32,
    setscalar_Cbool,
    setscalar_Cint32,
)


@dataclasses.dataclass
class pyFMS_mpp_domains(pyFMS_mpp):
    clibFMS: ct.CDLL = None

    """
    Subroutine: define_domains

    This method will pass its arguments to set the values for a domain

    Returns: In the Fortan source, global_indices, tile_count, and
    tile_id will be updated. The NumPy array passed for the
    global_indices argument will be updated automatically, the objects
    passed for the tile_count and tile_id arguments should also be set
    to the result of the method to update their values.
    """

    def define_domains(
        self,
        global_indices: NDArray,
        layout: NDArray,
        domain_id: Optional[int] = None,
        pelist: Optional[NDArray] = None,
        xflags: Optional[int] = None,
        yflags: Optional[int] = None,
        xhalo: Optional[int] = None,
        yhalo: Optional[int] = None,
        xextent: Optional[NDArray] = None,
        yextent: Optional[NDArray] = None,
        maskmap: Optional[NDArray[np.bool_]] = None,
        name: Optional[str] = None,
        symmetry: Optional[bool] = None,
        memory_size: Optional[NDArray] = None,
        whalo: Optional[int] = None,
        ehalo: Optional[int] = None,
        shalo: Optional[int] = None,
        nhalo: Optional[int] = None,
        is_mosaic: Optional[bool] = None,
        tile_count: Optional[int] = None,
        tile_id: Optional[int] = None,
        complete: Optional[bool] = None,
        x_cyclic_offset: Optional[int] = None,
        y_cyclic_offset: Optional[int] = None,
    ):

        _cfms_define_domains = self.clibFMS.cFMS_define_domains

        global_indices_p, global_indices_t = setarray_Cint32(global_indices)
        layout_p, layout_t = setarray_Cint32(layout)
        domain_id_c, domain_id_t = setscalar_Cint32(domain_id)
        pelist_p, pelist_t = setarray_Cint32(pelist)
        xflags_c, xflags_t = setscalar_Cint32(xflags)
        yflags_c, yflags_t = setscalar_Cint32(yflags)
        xhalo_c, xhalo_t = setscalar_Cint32(xhalo)
        yhalo_c, yhalo_t = setscalar_Cint32(yhalo)
        xextent_p, xextent_t = setarray_Cint32(xextent)
        yextent_p, yextent_t = setarray_Cint32(yextent)
        maskmap_p, maskmap_t = set_multipointer(arg=maskmap, num_ptr=2)
        name_c, name_t = set_Cchar(name)
        symmetry_c, symmetry_t = setscalar_Cbool(symmetry)
        memory_size_p, memory_size_t = setarray_Cint32(memory_size)
        whalo_c, whalo_t = setscalar_Cint32(whalo)
        ehalo_c, ehalo_t = setscalar_Cint32(ehalo)
        shalo_c, shalo_t = setscalar_Cint32(shalo)
        nhalo_c, nhalo_t = setscalar_Cint32(nhalo)
        is_mosaic_c, is_mosaic_t = setscalar_Cbool(is_mosaic)
        tile_count_c, tile_count_t = setscalar_Cint32(tile_count)
        tile_id_c, tile_id_t = setscalar_Cint32(tile_id)
        complete_c, complete_t = setscalar_Cbool(complete)
        x_cyclic_offset_c, x_cyclic_offset_t = setscalar_Cint32(x_cyclic_offset)
        y_cyclic_offset_c, y_cyclic_offset_t = setscalar_Cint32(y_cyclic_offset)

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
            y_cyclic_offset_t,
        ]

        _cfms_define_domains.restype = None

        _cfms_define_domains(
            global_indices_p,
            layout_p,
            domain_id_c,
            pelist_p,
            xflags_c,
            yflags_c,
            xhalo_c,
            yhalo_c,
            xextent_p,
            yextent_p,
            maskmap_p,
            name_c,
            symmetry_c,
            memory_size_p,
            whalo_c,
            ehalo_c,
            shalo_c,
            nhalo_c,
            is_mosaic_c,
            tile_count_c,
            tile_id_c,
            complete_c,
            x_cyclic_offset_c,
            y_cyclic_offset_c,
        )

    """
    Subroutine: define_io_domains

    Arguments of this method will define data for I/O domain

    Returns: No return
    """

    def define_io_domain(self, io_layout: NDArray, domain_id: Optional[int] = None):
        _cfms_define_io_domain = self.clibFMS.cFMS_define_io_domain

        io_layout_p, io_layout_t = setarray_Cint32(io_layout)
        domain_id_c, domain_id_t = setscalar_Cint32(domain_id)

        _cfms_define_io_domain.argtypes = [io_layout_t, domain_id_t]
        _cfms_define_io_domain.restype = None

        _cfms_define_io_domain(io_layout_p, domain_id_c)

    """
    Subroutine: define_layout

    Arguments passed to this method will define the layout to be used

    Returns: In the Fortran source, the passed layout argument is updated.
    The passed NumPy Array for layout will be updated automatically.
    """

    def define_layout(
        self,
        global_indices: NDArray,
        ndivs: int,
        layout: NDArray,
    ):
        _cfms_define_layout = self.clibFMS.cFMS_define_layout

        global_indices_p, global_indices_t = setarray_Cint32(global_indices)
        ndivs_c, ndivs_t = setscalar_Cint32(ndivs)
        layout_p, layout_t = setarray_Cint32(layout)

        _cfms_define_layout.argtypes = [global_indices_t, ndivs_t, layout_t]
        _cfms_define_layout.restype = None

        _cfms_define_layout(global_indices_p, ndivs_c, layout_p)

    """
    Subroutine: define_nest_domains

    Arguments passed to this method will define data for nest domains

    Returns: No return
    """

    def define_nest_domains(
        self,
        num_nest: int,
        ntiles: int,
        nest_level: NDArray,
        tile_fine: NDArray,
        tile_coarse: NDArray,
        istart_coarse: NDArray,
        icount_coarse: NDArray,
        jstart_coarse: NDArray,
        jcount_coarse: NDArray,
        npes_nest_tile: NDArray,
        x_refine: NDArray,
        y_refine: NDArray,
        nest_domain_id: Optional[int] = None,
        domain_id: Optional[int] = None,
        extra_halo: Optional[int] = None,
        name: Optional[str] = None,
    ):
        _cfms_define_nest_domain = self.clibFMS.cFMS_define_nest_domains

        num_nest_p, num_nest_t = setscalar_Cint32(num_nest)
        ntiles_c, ntiles_t = setscalar_Cint32(ntiles)
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
        nest_domain_id_c, nest_domain_id_t = setscalar_Cint32(nest_domain_id)
        domain_id_c, domain_id_t = setscalar_Cint32(domain_id)
        extra_halo_c, extra_halo_t = setscalar_Cint32(extra_halo)
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
            domain_id_t,
            extra_halo_t,
            name_t,
        ]
        _cfms_define_nest_domain.restype = None

        _cfms_define_nest_domain(
            num_nest_p,
            ntiles_c,
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
            nest_domain_id_c,
            domain_id_c,
            extra_halo_c,
            name_p,
        )

    """
    Function: domain_is_initialized

    Method will return a boolean value representing the state of domain
    initialization

    Returns: Boolean
    """

    def domain_is_initialized(self, domain_id: Optional[int] = None) -> bool:
        _cfms_domain_is_initialized = self.clibFMS.cFMS_domain_is_initialized

        domain_id_c, domain_id_t = setscalar_Cint32(domain_id)

        _cfms_domain_is_initialized.argtypes = [domain_id_t]
        _cfms_domain_is_initialized.restype = ct.c_bool

        return _cfms_domain_is_initialized(domain_id_c)

    """
    Subroutine: get_compute_domain

    Arguments passed to function will generate and update data for a
    compute domain

    Returns: In the Fortran source, when passed in xbegin, xend, ybegin, yend,
    xsize, xmax_size, ysize, ymax_size, x_is_global, y_is_global, and
    tile_count are updated. To obtain access to the updated value the flag
    associated with the desired variable should be set to true.
    This method will return a dictionary containing values for those arguments
    which were passed, overwriting the passed value.
    """

    def get_compute_domain(
        self,
        domain_id: Optional[int] = None,
        get_xbegin: Optional[bool] = False,
        get_xend: Optional[bool] = False,
        get_ybegin: Optional[bool] = False,
        get_yend: Optional[bool] = False,
        get_xsize: Optional[bool] = False,
        get_xmax_size: Optional[bool] = False,
        get_ysize: Optional[bool] = False,
        get_ymax_size: Optional[bool] = False,
        get_x_is_global: Optional[bool] = False,
        get_y_is_global: Optional[bool] = False,
        get_tile_count: Optional[bool] = False,
        position: Optional[int] = None,
        whalo: Optional[int] = None,
        shalo: Optional[int] = None,
    ) -> dict:
        _cfms_get_compute_domain = self.clibFMS.cFMS_get_compute_domain

        domain_id_c, domain_id_t = setscalar_Cint32(domain_id)
        xbegin_c, xbegin_t = setscalar_Cint32(arg=get_xbegin, get=True)
        xend_c, xend_t = setscalar_Cint32(arg=get_xend, get=True)
        ybegin_c, ybegin_t = setscalar_Cint32(arg=get_ybegin, get=True)
        yend_c, yend_t = setscalar_Cint32(arg=get_yend, get=True)
        xsize_c, xsize_t = setscalar_Cint32(arg=get_xsize, get=True)
        xmax_size_c, xmax_size_t = setscalar_Cint32(arg=get_xmax_size, get=True)
        ysize_c, ysize_t = setscalar_Cint32(arg=get_ysize, get=True)
        ymax_size_c, ymax_size_t = setscalar_Cint32(arg=get_ymax_size, get=True)
        x_is_global_c, x_is_global_t = setscalar_Cbool(arg=get_x_is_global, get=True)
        y_is_global_c, y_is_global_t = setscalar_Cbool(arg=get_y_is_global, get=True)
        tile_count_c, tile_count_t = setscalar_Cint32(arg=get_tile_count, get=True)
        position_c, position_t = setscalar_Cint32(position)
        whalo_c, whalo_t = setscalar_Cint32(whalo)
        shalo_c, shalo_t = setscalar_Cint32(shalo)

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
            shalo_t,
        ]
        _cfms_get_compute_domain.restype = None

        _cfms_get_compute_domain(
            domain_id_c,
            xbegin_c,
            xend_c,
            ybegin_c,
            yend_c,
            xsize_c,
            xmax_size_c,
            ysize_c,
            ymax_size_c,
            x_is_global_c,
            y_is_global_c,
            tile_count_c,
            position_c,
            whalo_c,
            shalo_c,
        )

        out_dict = {}
        out_dict["xbegin"] = xbegin_c.value if get_xbegin else None
        out_dict["xend"] = xend_c.value if get_xend else None
        out_dict["ybegin"] = ybegin_c.value if get_ybegin else None
        out_dict["yend"] = yend_c.value if get_yend else None
        out_dict["xsize"] = xsize_c.value if get_xsize else None
        out_dict["xmax_size"] = xmax_size_c.value if get_xmax_size else None
        out_dict["ysize"] = ysize_c.value if get_ysize else None
        out_dict["ymax_size"] = ymax_size_c.value if get_ymax_size else None
        out_dict["x_is_global"] = x_is_global_c.value if get_x_is_global else None
        out_dict["y_is_global"] = y_is_global_c.value if get_y_is_global else None
        out_dict["tile_count"] = tile_count_c.value if get_tile_count else None

        return out_dict

    """
    Subroutine: get_data_domain

    Arguments passed to function will generate and update data for a
    data domain

    Returns: In the Fortran source, when passed in xbegin, xend, ybegin, yend,
    xsize, xmax_size, ysize, ymax_size, x_is_global, y_is_global, and
    tile_count are updated. To obtain access to the updated value the flag
    associated with the desired variable should be set to true.
    This method will return a dictionary containing values for those arguments
    which were passed, overwriting the passed value.
    """

    def get_data_domain(
        self,
        domain_id: Optional[int] = None,
        get_xbegin: Optional[bool] = False,
        get_xend: Optional[bool] = False,
        get_ybegin: Optional[bool] = False,
        get_yend: Optional[bool] = False,
        get_xsize: Optional[bool] = False,
        get_xmax_size: Optional[bool] = False,
        get_ysize: Optional[bool] = False,
        get_ymax_size: Optional[bool] = False,
        get_x_is_global: Optional[bool] = False,
        get_y_is_global: Optional[bool] = False,
        get_tile_count: Optional[bool] = False,
        position: Optional[int] = None,
        whalo: Optional[int] = None,
        shalo: Optional[int] = None,
    ) -> dict:
        _cfms_get_data_domain = self.clibFMS.cFMS_get_data_domain

        domain_id_c, domain_id_t = setscalar_Cint32(domain_id)
        xbegin_c, xbegin_t = setscalar_Cint32(arg=get_xbegin, get=True)
        xend_c, xend_t = setscalar_Cint32(arg=get_xend, get=True)
        ybegin_c, ybegin_t = setscalar_Cint32(arg=get_ybegin, get=True)
        yend_c, yend_t = setscalar_Cint32(arg=get_yend, get=True)
        xsize_c, xsize_t = setscalar_Cint32(arg=get_xsize, get=True)
        xmax_size_c, xmax_size_t = setscalar_Cint32(arg=get_xmax_size, get=True)
        ysize_c, ysize_t = setscalar_Cint32(arg=get_ysize, get=True)
        ymax_size_c, ymax_size_t = setscalar_Cint32(arg=get_ymax_size, get=True)
        x_is_global_c, x_is_global_t = setscalar_Cbool(arg=get_x_is_global, get=True)
        y_is_global_c, y_is_global_t = setscalar_Cbool(arg=get_y_is_global, get=True)
        tile_count_c, tile_count_t = setscalar_Cint32(arg=get_tile_count, get=True)
        position_c, position_t = setscalar_Cint32(position)
        whalo_c, whalo_t = setscalar_Cint32(whalo)
        shalo_c, shalo_t = setscalar_Cint32(shalo)

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
            shalo_t,
        ]
        _cfms_get_data_domain.restype = None

        _cfms_get_data_domain(
            domain_id_c,
            xbegin_c,
            xend_c,
            ybegin_c,
            yend_c,
            xsize_c,
            xmax_size_c,
            ysize_c,
            ymax_size_c,
            x_is_global_c,
            y_is_global_c,
            tile_count_c,
            position_c,
            whalo_c,
            shalo_c,
        )

        out_dict = {}
        out_dict["xbegin"] = xbegin_c.value if get_xbegin else None
        out_dict["xend"] = xend_c.value if get_xend else None
        out_dict["ybegin"] = ybegin_c.value if get_ybegin else None
        out_dict["yend"] = yend_c.value if get_yend else None
        out_dict["xsize"] = xsize_c.value if get_xsize else None
        out_dict["xmax_size"] = xmax_size_c.value if get_xmax_size else None
        out_dict["ysize"] = ysize_c.value if get_ysize else None
        out_dict["ymax_size"] = ymax_size_c.value if get_ymax_size else None
        out_dict["x_is_global"] = x_is_global_c.value if get_x_is_global else None
        out_dict["y_is_global"] = y_is_global_c.value if get_y_is_global else None
        out_dict["tile_count"] = tile_count_c.value if get_tile_count else None

        return out_dict

    """
    Subroutine: get_domain_name

    The passed domain_name string object will be updated with the domain name
    respective to the arguments passed

    Returns: In Fortran source, domain_name is updated. The Python object passed as
    the argument for domain_name should be set to the result of the call to update
    its value as well.
    """

    def get_domain_name(self, domain_name: str, domain_id: Optional[int] = None) -> str:
        _cfms_get_domain_name = self.clibFMS.cFMS_get_domain_name

        domain_name_c, domain_name_t = set_Cchar(domain_name)
        domain_id_c, domain_id_t = setscalar_Cint32(domain_id)

        _cfms_get_domain_name.argtypes = [domain_name_t, domain_id_t]
        _cfms_get_domain_name.restype = None

        _cfms_get_domain_name(domain_name_c, domain_id_c)

        return domain_id_c.value.decode("utf-8")

    """
    Subroutine: get_layout

    Updates layout NumPy array to contain layout data

    Returns: Passed layout NumPy array will be automatically updated
    """

    def get_layout(self, layout: NDArray, domain_id: Optional[int] = None):
        _cfms_get_layout = self.clibFMS.cFMS_get_layout

        layout_p, layout_t = setarray_Cint32(layout)
        domain_id_c, domain_id_t = setscalar_Cint32(domain_id)

        _cfms_get_layout.argtypes = [layout_t, domain_id_t]
        _cfms_get_layout.restype = None

        _cfms_get_layout(layout_p, domain_id_c)

    """
    Subroutine: get_domain_pelist

    Updates layout NumPy array to contain pelist

    Returns: Passed layout NumPy array will be automatically updated
    """

    def get_domain_pelist(self, pelist: NDArray, domain_id: Optional[int]):
        _cfms_get_domain_pelist = self.clibFMS.cFMS_get_domain_pelist

        pelist_p, pelist_t = setarray_Cint32(pelist)
        domain_id_c, domain_id_t = setscalar_Cint32(domain_id)

        _cfms_get_domain_pelist.argtypes = [pelist_t, domain_id_t]
        _cfms_get_domain_pelist.restype = None

        _cfms_get_domain_pelist(pelist_p, domain_id_c)

    """
    Subroutine: set_compute_domain

    Passed arguments will set data for compute domain

    Returns: In Fortran source, xbegin, xend, ybegin, yend, xsize,
    ysize, x_is_global, y_is_global, and tile_count are updated.
    Python objects passed as arguments should be set to the result
    of the call.
    Returns: In the Fortran source, when passed in xbegin, xend, ybegin, yend,
    xsize, ysize, x_is_global, y_is_global, and tile_count are updated. To
    obtain access to their values, an integer Python object should be passed
    in as an argument for the desired variable.
    This method will return a dictionary containing values for those arguments
    which were passed, overwriting the passed value.
    """

    def set_compute_domain(
        self,
        domain_id: Optional[int] = None,
        xbegin: Optional[int] = None,
        xend: Optional[int] = None,
        ybegin: Optional[int] = None,
        yend: Optional[int] = None,
        xsize: Optional[int] = None,
        ysize: Optional[int] = None,
        x_is_global: Optional[bool] = False,
        y_is_global: Optional[bool] = False,
        tile_count: Optional[int] = None,
        whalo: Optional[int] = None,
        shalo: Optional[int] = None,
    ) -> dict:
        _cfms_set_compute_domain = self.clibFMS.cFMS_set_compute_domain

        domain_id_c, domain_id_t = setscalar_Cint32(domain_id)
        xbegin_c, xbegin_t = setscalar_Cint32(xbegin)
        xend_c, xend_t = setscalar_Cint32(xend)
        ybegin_c, ybegin_t = setscalar_Cint32(ybegin)
        yend_c, yend_t = setscalar_Cint32(yend)
        xsize_c, xsize_t = setscalar_Cint32(xsize)
        ysize_c, ysize_t = setscalar_Cint32(ysize)
        x_is_global_c, x_is_global_t = setscalar_Cbool(x_is_global)
        y_is_global_c, y_is_global_t = setscalar_Cbool(y_is_global)
        tile_count_c, tile_count_t = setscalar_Cint32(tile_count)
        whalo_c, whalo_t = setscalar_Cint32(whalo)
        shalo_c, shalo_t = setscalar_Cint32(shalo)

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
            shalo_t,
        ]
        _cfms_set_compute_domain.restype = None

        _cfms_set_compute_domain(
            domain_id_c,
            xbegin_c,
            xend_c,
            ybegin_c,
            yend_c,
            xsize_c,
            ysize_c,
            x_is_global_c,
            y_is_global_c,
            tile_count_c,
            whalo_c,
            shalo_c,
        )

        out_dict = {}
        out_dict["xbegin"] = xbegin_c.value if xbegin is not None else xbegin
        out_dict["xend"] = xend_c.value if xend is not None else xend
        out_dict["ybegin"] = ybegin_c.value if ybegin is not None else ybegin
        out_dict["yend"] = yend_c.value if yend is not None else yend
        out_dict["xsize"] = xsize_c.value if xsize is not None else xsize
        out_dict["ysize"] = ysize_c.value if ysize is not None else ysize
        out_dict["x_is_global"] = (
            x_is_global_c.value if x_is_global is not None else x_is_global
        )
        out_dict["y_is_global"] = (
            y_is_global_c.value if y_is_global is not None else y_is_global
        )
        out_dict["tile_count"] = (
            tile_count_c.value if tile_count is not None else tile_count
        )

        return out_dict

    """
    Subroutine: set_current_domain

    Sets domain to current_domain, updating the id of the current_domain
    to domain_id
    """

    def set_current_domain(self, domain_id: Optional[int] = None):
        _cfms_set_current_domain = self.clibFMS.cFMS_set_current_domain

        domain_id_c, domain_id_t = setscalar_Cint32(domain_id)

        _cfms_set_current_domain.argtypes = [domain_id_t]
        _cfms_set_current_domain.restype = None

        _cfms_set_current_domain(domain_id_c)

    """
    Subroutine: set_current_nest_domain

    Sets nest_domain to current_nest_domain, and updates id of current_nest_domain
    to nest_domain_id
    """

    def set_current_nest_domain(self, nest_domain_id: Optional[int] = None):
        _cfms_set_current_nest_domain = self.clibFMS.cFMS_set_current_nest_domain

        nest_domain_id_c, nest_domain_id_t = setscalar_Cint32(nest_domain_id)

        _cfms_set_current_nest_domain.argtypes = [nest_domain_id_t]
        _cfms_set_current_nest_domain.restype = None

        _cfms_set_current_nest_domain(nest_domain_id_c)

    """
    Subroutine: set_data_domain

    Passed arguments will set data for data domain

    Returns: In the Fortran source, when passed in xbegin, xend, ybegin, yend,
    xsize, ysize, x_is_global, y_is_global, and tile_count are updated. To
    obtain access to their values, an integer Python object should be passed
    in as an argument for the desired variable.
    This method will return a dictionary containing values for those arguments
    which were passed, overwriting the passed value.
    """

    def set_data_domain(
        self,
        domain_id: Optional[int] = None,
        xbegin: Optional[int] = None,
        xend: Optional[int] = None,
        ybegin: Optional[int] = None,
        yend: Optional[int] = None,
        xsize: Optional[int] = None,
        ysize: Optional[int] = None,
        x_is_global: Optional[bool] = None,
        y_is_global: Optional[bool] = None,
        tile_count: Optional[int] = None,
        whalo: Optional[int] = None,
        shalo: Optional[int] = None,
    ) -> dict:
        _cfms_set_data_domain = self.clibFMS.cFMS_set_data_domain

        domain_id_c, domain_id_t = setscalar_Cint32(domain_id)
        xbegin_c, xbegin_t = setscalar_Cint32(xbegin)
        xend_c, xend_t = setscalar_Cint32(xend)
        ybegin_c, ybegin_t = setscalar_Cint32(ybegin)
        yend_c, yend_t = setscalar_Cint32(yend)
        xsize_c, xsize_t = setscalar_Cint32(xsize)
        ysize_c, ysize_t = setscalar_Cint32(ysize)
        x_is_global_c, x_is_global_t = setscalar_Cbool(x_is_global)
        y_is_global_c, y_is_global_t = setscalar_Cbool(y_is_global)
        tile_count_c, tile_count_t = setscalar_Cint32(tile_count)
        whalo_c, whalo_t = setscalar_Cint32(whalo)
        shalo_c, shalo_t = setscalar_Cint32(shalo)

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
            domain_id_c,
            xbegin_c,
            xend_c,
            ybegin_c,
            yend_c,
            xsize_c,
            ysize_c,
            x_is_global_c,
            y_is_global_c,
            tile_count_c,
            whalo_c,
            shalo_c,
        )

        out_dict = {}
        out_dict["xbegin"] = xbegin_c.value if xbegin is not None else xbegin
        out_dict["xend"] = xend_c.value if xend is not None else xend
        out_dict["ybegin"] = ybegin_c.value if ybegin is not None else ybegin
        out_dict["yend"] = yend_c.value if yend is not None else yend
        out_dict["xsize"] = xsize_c.value if xsize is not None else xsize
        out_dict["ysize"] = ysize_c.value if ysize is not None else ysize
        out_dict["x_is_global"] = (
            x_is_global_c.value if x_is_global is not None else x_is_global
        )
        out_dict["y_is_global"] = (
            y_is_global_c.value if y_is_global is not None else y_is_global
        )
        out_dict["tile_count"] = (
            tile_count_c.value if tile_count is not None else tile_count
        )

        return out_dict

    """
    Subroutine: set_global_domain

    Passed arguments will set data for data domain

    Returns: In Fortran source, xbegin, xend, ybegin, yend, xsize,
    ysize, and tile_count are updated.
    Python objects passed as arguments should be set to the result
    of the call.
    Returns: In the Fortran source, when passed in xbegin, xend, ybegin, yend,
    xsize, ysize, and tile_count are updated. To obtain access to their values,
    an integer Python object should be passed in as an argument for the
    desired variable.
    This method will return a dictionary containing values for those arguments
    which were passed, overwriting the passed value.
    """

    def set_global_domain(
        self,
        domain_id: Optional[int] = None,
        xbegin: Optional[int] = None,
        xend: Optional[int] = None,
        ybegin: Optional[int] = None,
        yend: Optional[int] = None,
        xsize: Optional[int] = None,
        ysize: Optional[int] = None,
        tile_count: Optional[int] = None,
        whalo: Optional[int] = None,
        shalo: Optional[int] = None,
    ) -> dict:
        _cfms_set_global_domain = self.clibFMS.cFMS_set_global_domain

        domain_id_c, domain_id_t = setscalar_Cint32(domain_id)
        xbegin_c, xbegin_t = setscalar_Cint32(xbegin)
        xend_c, xend_t = setscalar_Cint32(xend)
        ybegin_c, ybegin_t = setscalar_Cint32(ybegin)
        yend_c, yend_t = setscalar_Cint32(yend)
        xsize_c, xsize_t = setscalar_Cint32(xsize)
        ysize_c, ysize_t = setscalar_Cint32(ysize)
        tile_count_c, tile_count_t = setscalar_Cint32(tile_count)
        whalo_c, whalo_t = setscalar_Cint32(whalo)
        shalo_c, shalo_t = setscalar_Cint32(shalo)

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
            domain_id_c,
            xbegin_c,
            xend_c,
            ybegin_c,
            yend_c,
            xsize_c,
            ysize_c,
            tile_count_c,
            whalo_c,
            shalo_c,
        )

        out_dict = {}
        out_dict["xbegin"] = xbegin_c.value if xbegin is not None else xbegin
        out_dict["xend"] = xend_c.value if xend is not None else xend
        out_dict["ybegin"] = ybegin_c.value if ybegin is not None else ybegin
        out_dict["yend"] = yend_c.value if yend is not None else yend
        out_dict["xsize"] = xsize_c.value if xsize is not None else xsize
        out_dict["ysize"] = ysize_c.value if ysize is not None else ysize
        out_dict["tile_count"] = (
            tile_count_c.value if tile_count is not None else tile_count
        )

        return out_dict
