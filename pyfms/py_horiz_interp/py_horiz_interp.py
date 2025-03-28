import ctypes

from typing import Any

import numpy as np
import numpy.typing as npt


class pyFMS_horiz_interp:
    def __init__(self, cfms: ctypes.CDLL):
        self.cfms = cfms

    def get_maxxgrid(self) -> np.int32:
        self.cfms.get_maxxgrid.restype = np.int32
        return self.cfms.get_maxxgrid()

    def create_xgrid_2dx2d_order1(
        self,
        nlon_src: int,
        nlat_src: int,
        nlon_tgt: int,
        nlat_tgt: int,
        lon_src: npt.NDArray[np.float64],
        lat_src: npt.NDArray[np.float64],
        lon_tgt: npt.NDArray[np.float64],
        lat_tgt: npt.NDArray[np.float64],
        mask_src: npt.NDArray[np.float64],
    ) -> dict:

        ngrid_src = nlon_src * nlat_src
        ngrid_tgt = nlon_tgt * nlat_tgt

        ngrid_src_p1 = (nlon_src + 1) * (nlat_src + 1)
        ngrid_tgt_p1 = (nlon_tgt + 1) * (nlat_tgt + 1)

        maxxgrid = self.get_maxxgrid()

        nlon_src_t = ctypes.c_int
        nlat_src_t = ctypes.c_int
        nlon_tgt_t = ctypes.c_int
        nlat_tgt_t = ctypes.c_int
        maxxgrid_t = ctypes.c_int
        lon_src_ndp = np.ctypeslib.ndpointer(
            dtype=np.float64, shape=(ngrid_src_p1), flags="C_CONTIGUOUS"
        )
        lat_src_ndp = np.ctypeslib.ndpointer(
            dtype=np.float64, shape=(ngrid_src_p1), flags="C_CONTIGUOUS"
        )
        lon_tgt_ndp = np.ctypeslib.ndpointer(
            dtype=np.float64, shape=(ngrid_tgt_p1), flags="C_CONTIGUOUS"
        )
        lat_tgt_ndp = np.ctypeslib.ndpointer(
            dtype=np.float64, shape=(ngrid_tgt_p1), flags="C_CONTIGUOUS"
        )
        mask_src_ndp = np.ctypeslib.ndpointer(
            dtype=np.float64, shape=(ngrid_src_p1), flags="C_CONTIGUOUS"
        )
        i_src_ndp = np.ctypeslib.ndpointer(
            dtype=np.int32, shape=(maxxgrid), flags="C_CONTIGUOUS"
        )
        j_src_ndp = np.ctypeslib.ndpointer(
            dtype=np.int32, shape=(maxxgrid), flags="C_CONTIGUOUS"
        )
        i_tgt_ndp = np.ctypeslib.ndpointer(
            dtype=np.int32, shape=(maxxgrid), flags="C_CONTIGUOUS"
        )
        j_tgt_ndp = np.ctypeslib.ndpointer(
            dtype=np.int32, shape=(maxxgrid), flags="C_CONTIGUOUS"
        )
        xarea_ndp = np.ctypeslib.ndpointer(
            dtype=np.float64, shape=(maxxgrid), flags="C_CONTIGUOUS"
        )

        i_src = np.zeros(maxxgrid, dtype=np.int32)
        j_src = np.zeros(maxxgrid, dtype=np.int32)
        i_tgt = np.zeros(maxxgrid, dtype=np.int32)
        j_tgt = np.zeros(maxxgrid, dtype=np.int32)
        xarea = np.zeros(maxxgrid, dtype=np.float64)

        _create_xgrid = self.cfms.cFMS_create_xgrid_2dx2d_order1

        _create_xgrid.restype = ctypes.c_int
        _create_xgrid.argtypes = [
            ctypes.POINTER(nlon_src_t),
            ctypes.POINTER(nlat_src_t),
            ctypes.POINTER(nlon_tgt_t),
            ctypes.POINTER(nlat_tgt_t),
            lon_src_ndp,
            lat_src_ndp,
            lon_tgt_ndp,
            lat_tgt_ndp,
            mask_src_ndp,
            ctypes.POINTER(maxxgrid_t),
            i_src_ndp,
            j_src_ndp,
            i_tgt_ndp,
            j_tgt_ndp,
            xarea_ndp,
        ]

        nlon_src_c = nlon_src_t(nlon_src)
        nlat_src_c = nlat_src_t(nlat_src)
        nlon_tgt_c = nlon_tgt_t(nlon_tgt)
        nlat_tgt_c = nlat_tgt_t(nlat_tgt)
        maxxgrid_c = maxxgrid_t(maxxgrid)

        nxgrid = _create_xgrid(
            ctypes.byref(nlon_src_c),
            ctypes.byref(nlat_src_c),
            ctypes.byref(nlon_tgt_c),
            ctypes.byref(nlat_tgt_c),
            lon_src,
            lat_src,
            lon_tgt,
            lat_tgt,
            mask_src,
            maxxgrid_c,
            i_src,
            j_src,
            i_tgt,
            j_tgt,
            xarea,
        )

        return {
            "nxgrid": nxgrid,
            "i_src": i_src[:nxgrid],
            "j_src": j_src[:nxgrid],
            "i_tgt": i_tgt[:nxgrid],
            "j_tgt": j_tgt[:nxgrid],
            "xarea": xarea[:nxgrid],
        }

    def horiz_interp_init(self, ninterp: int = None):
        _cfms_horiz_interp_init = self.cfms.cFMS_horiz_interp_init

        ninterp_c, ninterp_t = ctypes.c_int(ninterp), ctypes.POINTER(ctypes.c_int)

        _cfms_horiz_interp_init.argtypes = [ninterp_t]
        _cfms_horiz_interp_init.restype = None

        _cfms_horiz_interp_init(ctypes.byref(ninterp_c))

    def set_current_interp(self, interp_id: int = None):
        _cfms_set_current_interp = self.cfms.cFMS_set_current_interp

        interp_id_c, interp_id_t = ctypes.c_int(interp_id), ctypes.POINTER(ctypes.c_int)

        _cfms_set_current_interp.argtypes = [interp_id_t]
        _cfms_set_current_interp.restype = None

        _cfms_set_current_interp(ctypes.byref(interp_id_c))

    def get_interp(
            self,
            datatype: Any,
            interp_id: int = None,
            nxgrid: int = None,
            ilon_ptr: npt.NDArray = None,
            ilon_shape: list[int] = None,
            jlat_ptr: npt.NDArray = None,
            jlat_shape: list[int] = None,
            i_lon_ptr: npt.NDArray = None,
            i_lon_shape: list[int] = None,
            j_lat_ptr: npt.NDArray = None,
            j_lat_shape: list[int] = None,
            found_neighbors_ptr: npt.NDArray = None,
            found_neighbors_shape: list[int] = None,
            num_found_ptr: npt.NDArray = None,
            num_found_shape: list[int] = None,
            nlon_src: int = None,
            nlat_src: int = None,
            nlon_dst: int = None,
            nlat_dst: int = None,
            interp_method: int = None,
            I_am_initialized: bool = None,
            version: int = None,
            i_src_ptr: npt.NDArray = None,
            i_src_shape: list[int] = None,
            j_src_ptr: npt.NDArray = None,
            j_src_shape: list[int] = None,
            i_dst_ptr: npt.NDArray = None,
            i_dst_shape: int = None,
            j_dst_ptr: npt.NDArray = None,
            j_dst_shape: int = None,
            faci_ptr: npt.NDArray = None,
            faci_shape: npt.NDArray = None,
            facj_ptr: npt.NDArray = None,
            facj_shape: npt.NDArray = None,
            area_src_ptr: npt.NDArray = None,
            area_src_shape: npt.NDArray = None,
            area_dst_ptr: npt.NDArray = None,
            area_dst_shape: npt.NDArray = None,
            wti_ptr: npt.NDArray = None,
            wti_shape: npt.NDArray = None,
            wtj_ptr: npt.NDArray = None,
            wtj_shape: npt.NDArray = None,
            src_dist_ptr: npt.NDArray = None,
            src_dist_shape: npt.NDArray = None,
            rat_x_ptr: npt.NDArray = None,
            rat_x_shape: npt.NDArray = None,
            rat_y_ptr: npt.NDArray = None,
            rat_y_shape: npt.NDArray = None,
            lon_in_ptr: npt.NDArray = None,
            lon_in_shape: int = None,
            lat_in_ptr: npt.NDArray = None,
            lat_in_shape: int = None,    
            area_frac_dst_ptr: npt.NDArray = None,
            area_frac_dst_shape: int = None,
            mask_in_ptr: npt.NDArray = None,
            mask_in_shape: npt.NDArray = None,
            max_src_dist: float = None,
            is_allocated: bool = None,
    ):
        if datatype is np.float64:
            _cfms_get_interp = self.cfms.cFMS_get_interp_cdouble
            faci_t = np.ctypeslib.ndpointer(dtype=np.float64, ndim=)
