import dataclasses
import ctypes
import numpy

@dataclasses.datacass:
class HorizInterp():

    def create_xgrid_2dx_2d_order1(cFMS: ctypes.CDLL,
                                   nlon_src: int,
                                   nlat_src: int,
                                   nlon_tgt: int,
                                   nlat_tgt: int,
                                   lon_src: npt.NDArray[np.float64],
                                   lat_src: npt.NDArray[np.float64],
                                   lon_tgt: npt.NDArray[np.float64],
                                   lat_tgt: npt.NDArray[np.float64],
                                   mask_src: npt.NDArray[np.float64]) \
                                   -> tuple[npt.NDArray[np.int32],
                                            npt.NDArray[np.int32],
                                            npt.NDArray[np.int32],
                                            npt.NDArray[np.int32],
                                            npt.NDArray[np.float64]]:

        ngrid_src = nlon_src*nlat_src
        ngrid_tgt = nlon_tgt*nlat_tgt

        ngrid_src_p1 = (nlon_src+1) * (nlat_src+1)
        ngrid_tgt_p1 = (nlon_tgt+1) * (nlat_tgt+1)

        maxxgrid = self.get_maxxgrid()
        
        nlon_src_t = ctypes.c_int
        nlat_src_t = ctypes.c_int
        nlon_tgt_t = ctypes.c_int
        nlat_tgt_t = ctypes.c_int
        lon_src_ndp = np.ctypeslib.ndpointer(dtype=np.float64, shape=(ngrid_src_p1), flags='C_CONTIGUOUS')
        lat_src_ndp = np.ctypeslib.ndpointer(dtype=np.float64, shape=(ngrid_src_p1), flags='C_CONTIGUOUS')
        lon_tgt_ndp = np.ctypeslib.ndpointer(dtype=np.float64, shape=(ngrid_tgt_p1), flags='C_CONTIGUOUS')
        lat_tgt_ndp = np.ctypeslib.ndpointer(dtype=np.float64, shape=(ngrid_tgt_p1), flags='C_CONTIGUOUS')
        mask_src_ndp = np.ctypeslib.ndpointer(dtype=np.float64, shape=(ngrid_src_p1), flags='C_CONTIGUOUS')
        i_src_ndp = np.ctypeslib.ndpointer(dtype=np.int32, shape=(maxxgrid), flags='C_CONTIGUOUS')
        j_src_ndp = np.ctypeslib.ndpointer(dtype=np.int32, shape=(maxxgrid), flags='C_CONTIGUOUS')
        i_tgt_ndp = np.ctypeslib.ndpointer(dtype=np.int32, shape=(maxxgrid), flags='C_CONTIGUOUS')
        j_tgt_ndp = np.ctypeslib.ndpointer(dtype=np.int32, shape=(maxxgrid), flags='C_CONTIGUOUS')
        xarea_ndp = np.ctypeslib.ndpointer(dtype=np.float64, shape=(maxxgrid), flags='C_CONTIGUOUS')
        
        i_src_c = np.zeros(maxxgrid, dtype=np.int32)
        j_src_c = np.zeros(maxxgrid, dtype=np.int32)
        i_tgt_c = np.zeros(maxxgrid, dtype=np.int32)
        j_tgt_c = np.zeros(maxxgrid, dtype=np.int32)
        xarea_c = np.zeros(maxxgrid, dtype=np.float64)

        _create_xgrid = self.cFMS.create_xgrid_2dx2d_order1

        _create_xgrid.restype = ctypes.c_int        
        _create_xgrid.argtypes = [ctypes.POINTER(nlon_src_t),
                                  ctypes.POINTER(nlat_src_t),
                                  ctypes.POINTER(nlon_tgt_t),
                                  ctypes.POINTER(nlat_tgt_t),
                                  lon_src_ndp,
                                  lat_src_ndp,
                                  lon_tgt_ndp,
                                  lat_tgt_ndp,
                                  mask_src_ndp,
                                  i_src_ndp,
                                  j_src_ndp,
                                  i_tgt_ndp,
                                  j_tgt_ndp,
                                  xarea_ndp]
        
        nlon_src_c = nlon_src_t(nlon_src)
        nlat_src_c = nlat_src_t(nlat_src)
        nlon_tgt_c = nlon_tgt_t(nlon_tgt)
        nlat_tgt_c = nlat_tgt_t(nlat_tgt

        nxgrid = _create_xgrid(ctypes.byref(nlon_src_c),
                               ctypes.byref(nlat_src_c),
                               ctypes.byref(nlon_tgt_c),
                               ctypes.byref(nlat_tgt_c),
                               lon_src,
                               lat_src,
                               lon_tgt,
                               lat_tgt,
                               mask_src,
                               i_src_c,
                               j_src_c,
                               i_tgt_c,
                               j_tgt_c,
                               xarea_c)

        return i_src_c, j_src_c, i_tgt_c, j_tgt_c, xarea_c

    
