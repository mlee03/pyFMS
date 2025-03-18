import ctypes
from typing import Optional

from numpy.typing import NDArray

from pyfms.pyfms_data_handling import (
    set_Cchar,
    setarray_Cdouble,
    setarray_Cfloat,
    setscalar_Cint32,
    setscalar_Cbool,
)

class pyFMS_diag_axis_init:

    def __init__(self, clibFMS: ctypes.CDLL = None):
        self.clibFMS = clibFMS

    def diag_axis_init_cdouble(
        self,
        name: str,
        naxis_data: int,
        axis_data: NDArray,
        units: str,
        cart_name: str,
        long_name: Optional[str] = None,
        set_name: Optional[str] = None,
        direction: Optional[int] = None,
        edges: Optional[int] = None,
        aux: Optional[str] = None,
        req: Optional[str] = None,
        tile_count: Optional[int] = None,
        domain_position: Optional[int] = None,
        not_xy: Optional[bool] = None,
    ) -> int:
        _cfms_diag_axis_init_cdouble = self.clibFMS.cFMS_diag_axis_init_cdouble

        long_name = long_name[:64]
        set_name = set_name[:64]

        name_c, name_t = set_Cchar(name)
        naxis_data_c, naxis_data_t = setscalar_Cint32(naxis_data)
        axis_data_p, axis_data_t = setarray_Cdouble(axis_data)
        units_c, units_t = set_Cchar(units)
        cart_name_c, cart_name_t = set_Cchar(cart_name)
        long_name_c, long_name_t = set_Cchar(long_name)
        set_name_c, set_name_t = set_Cchar(set_name)
        direction_c, direction_t = setscalar_Cint32(direction)
        edges_c, edges_t = setscalar_Cint32(edges)
        aux_c, aux_t = set_Cchar(aux)
        req_c, req_t = set_Cchar(req)
        tile_count_c, tile_count_t = setscalar_Cint32(tile_count)
        domain_position_c, domain_position_t = setscalar_Cint32(domain_position)
        not_xy_c, not_xy_t = setscalar_Cbool[not_xy]

        _cfms_diag_axis_init_cdouble.argtypes = [
            name_t,
            naxis_data_t,
            axis_data_t,
            units_t,
            cart_name_t,
            long_name_t,
            set_name_t,
            direction_t,
            edges_t,
            aux_t,
            req_t,
            tile_count_t,
            domain_position_t,
            not_xy_t,
        ]
        _cfms_diag_axis_init_cdouble.restype = ctypes.c_int

        return _cfms_diag_axis_init_cdouble(
            name_c,
            naxis_data_c,
            axis_data_p,
            units_c,
            cart_name_c,
            long_name_c,
            set_name_c,
            direction_c,
            edges_c,
            aux_c,
            req_c,
            tile_count_c,
            domain_position_c,
            not_xy_c,
        )

    def diag_axis_init_cfloat(
        self,
        name: str,
        naxis_data: int,
        axis_data: NDArray,
        units: str,
        cart_name: str,
        long_name: Optional[str] = None,
        set_name: Optional[str] = None,
        direction: Optional[int] = None,
        edges: Optional[int] = None,
        aux: Optional[str] = None,
        req: Optional[str] = None,
        tile_count: Optional[int] = None,
        domain_position: Optional[int] = None,
        not_xy: Optional[bool] = None,
    ) -> int:
        _cfms_diag_axis_init_cfloat = self.clibFMS.cFMS_diag_axis_init_cfloat

        if long_name is not None:
            long_name = long_name[:64]
        if set_name is not None:
            set_name = set_name[:64]

        name_c, name_t = set_Cchar(name)
        naxis_data_c, naxis_data_t = setscalar_Cint32(naxis_data)
        axis_data_p, axis_data_t = setarray_Cfloat(axis_data)
        units_c, units_t = set_Cchar(units)
        cart_name_c, cart_name_t = set_Cchar(cart_name)
        long_name_c, long_name_t = set_Cchar(long_name)
        set_name_c, set_name_t = set_Cchar(set_name)
        direction_c, direction_t = setscalar_Cint32(direction)
        edges_c, edges_t = setscalar_Cint32(edges)
        aux_c, aux_t = set_Cchar(aux)
        req_c, req_t = set_Cchar(req)
        tile_count_c, tile_count_t = setscalar_Cint32(tile_count)
        domain_position_c, domain_position_t = setscalar_Cint32(domain_position)
        not_xy_c, not_xy_t = setscalar_Cbool(not_xy)

        _cfms_diag_axis_init_cfloat.argtypes = [
            name_t,
            naxis_data_t,
            axis_data_t,
            units_t,
            cart_name_t,
            long_name_t,
            set_name_t,
            direction_t,
            edges_t,
            aux_t,
            req_t,
            tile_count_t,
            domain_position_t,
            not_xy_t,
        ]
        _cfms_diag_axis_init_cfloat.restype = ctypes.c_int

        return _cfms_diag_axis_init_cfloat(
            name_c,
            naxis_data_c,
            axis_data_p,
            units_c,
            cart_name_c,
            long_name_c,
            set_name_c,
            direction_c,
            edges_c,
            aux_c,
            req_c,
            tile_count_c,
            domain_position_c,
            not_xy_c,
        )
