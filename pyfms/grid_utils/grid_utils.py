import ctypes
import dataclasses
import numpy as np

@dataclasses.datacass
class GridUtils():

    def get_grid_area(cFMS: ctypes.CDLL,
                      nlon: int,
                      nlat: int,
                      lon: npt.NDArray[np.float64],
                      lat: npt.NDArray[np.float64]):
        
        ncells = nlon*nlat
        ngridpts = (nlon+1) * (nlat+1)        
        
        nlon_t = ctypes.c_int
        nlat_t = ctypes.c_int
        lon_t = np.ctypeslib.ndpointer(dtype=np.float64, shape=(ngridpts), flags='C_CONTIGUOUS')
        lat_t = np.ctypeslib.ndpointer(dtype=np.float64, shape=(ngridpts), flags='C_CONTIGUOUS')
        area_t = np.ctypeslib.ndpointer(dtype=np.float64, shape=(ncells), flags='C_CONTIGUOUS')
        
        nlon_c = nlon_t(nlon)
        nlat_c = nlat_t(nlat)
        area = np.zeros(ncells, dtype=np.float64)
        
        _get_grid_area = self.cFMS.get_grid_area
        
        _get_grid_area.restype = None
        _get_grid_area.argtype = [ctypes.POINTER(nlon_t),
                                  ctypes.POINTER(nlat_t),
                                  lon_t,
                                  lat_t,
                                  area_t]
        
        nlon_c = nlon_t(nlon)
        nlat_c = nlat_t(nlat)
        
        _get_grid_area(ctypes.byref(nlon_c),
                       ctypes.byref(nlat_c),
                       lon_t,
                       lat_t,
                       area_t)
                       

