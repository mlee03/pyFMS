import ctypes
import numpy.typing as npt
from typing import Any

class pyDataOverride:

    def __init__(self, cFMS: ctypes.CDLL = None):
        self.cfms = cFMS

    def data_override_init(
        self,
        atm_domain_id: int | None,
        ocn_domain_id: int | None,
        ice_domain_id: int | None,
        land_domain_id: int | None,
        land_domainUG_id: int | None,
        mode: int | None,
    ):

        _data_override_init = self.cfms.cFMS_data_override_init

        atm_domain_id_t = ctypes.c_int
        ocn_domain_id_t = ctypes.c_int
        ice_domain_id_t = ctypes.c_int
        land_domain_id_t = ctypes.c_int
        land_domainUG_id_t = ctypes.c_int
        mode_t = ctypes.c_int

        atm_domain_id_c = (
            atm_domain_id_t(atm_domain_id) if atm_domain_id is not None else None
        )
        ocn_domain_id_c = (
            ocn_domain_id_t(ocn_domain_id) if ocn_domain_id is not None else None
        )
        ice_domain_id_c = (
            ice_domain_id_t(ice_domain_id) if ice_domain_id is not None else None
        )
        land_domain_id_c = (
            land_domain_id_t(land_domain_id) if land_domain_id is not None else None
        )
        land_domainUG_id_c = (
            land_domainUG_id_t(land_domainUG_id)
            if land_domainUG_id is not None
            else None
        )
        mode_c = mode_t(mode) if mode is not None else None

        _data_override_init.restype = None
        _data_override_init.argtypes = [
            ctypes.POINTER(atm_domain_id_t),
            ctypes.POINTER(ocn_domain_id_t),
            ctypes.POINTER(ice_domain_id_t),
            ctypes.POINTER(land_domain_id_t),
            ctypes.POINTER(land_domainUG_id_t),
            ctypes.POINTER(mode_t),
        ]

        _data_override_init(
            atm_domain_id_c,
            ocn_domain_id_c,
            ice_domain_id_c,
            land_domain_id_c,
            land_domainUG_id_c,
            mode_c,
        )


    def data_override_2d(self,
                         gridname: str,
                         fieldname: str,
                         data_shape: list[int],
                         data_type: Any, 
                         is_in: int | None,
                         ie_in: int | None,
                         js_in: int | None,
                         je_in: int | None) -> npt.NDArray:

        _data_override_2d_cfloat = self.cfms.cFMS_data_override_2d_cfloat
        
        gridname_t = ctypes.c_char_p
        fieldname_t = ctypes.c_char_p
        data_shape_t = np.ctypeslib.ndpointer(dtype=np.int32, ndim=(1), shape=(2))
        data_t = np.ctypeslib.ndpointer(dtype=data_type, ndim=(2), shape=data_shape)
        override_t = ctypes.c_bool        
        is_in_t = ctypes.c_int
        ie_in_t = ctypes.c_int
        js_in_t = ctypes.c_int
        je_in_t = ctypes.c_int

        gridname_c = gridname_t(gridname.encode("utf-8"))
        fieldname_c = fieldname_t(fieldname.encode("utf-8"))
        data_shape_c = np.array(data_shape, dtype=np.int32)
        data = np.ascontinguousarray(np.zeroes(data_shape, dtype=data_type, order="C"))
        override = override_t(False)
        is_in_c = is_in_t(is_in) if is_in is not None else None
        js_in_c = js_in_t(js_in) if js_in is not None else None
        ie_in_c = ie_in_t(ie_in) if ie_in is not None else None
        je_in_c = je_in_t(je_in) if je_in is not None else None

        
        _data_override_2d_cfloat.restype = None
        _data_override_2d_cfloat.argtypes = [gridname_t,
                                             fieldname_t,
                                             data_shape_t,
                                             data_t,
                                             ctypes.POINTER(override_t),
                                             ctypes.POINTER(is_in_t),
                                             ctypes.POINTER(ie_in_t),
                                             ctypes.POINTER(js_in_t),
                                             ctypes.POINTER(je_in_t)]
        _data_override_2d_cfloat(gridname_c,
                                 fieldname_c,
                                 data_shape_c,
                                 data,
                                 override,
                                 is_in_c,
                                 js_in_c,
                                 ie_in_c,
                                 je_in_c)

        return data, override.value
                                 
                                 
                                             
                         
