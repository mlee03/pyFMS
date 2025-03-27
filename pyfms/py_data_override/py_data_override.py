import ctypes
from typing import Any
import numpy.typing as npt

import numpy as np


class pyDataOverride:

    def __init__(self, cFMS: ctypes.CDLL = None):
        self.cfms = cFMS

    def data_override_init(
        self,
        atm_domain_id: int | None = None,
        ocn_domain_id: int | None = None,
        ice_domain_id: int | None = None,
        land_domain_id: int | None = None,
        land_domainUG_id: int | None = None,
        mode: int | None = None,
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

    def data_override_set_time(
        self,
        year: int | None = None,
        month: int | None = None,
        day: int | None = None,
        hour: int | None = None,
        minute: int | None = None,
        second: int | None = None,
        tick: int | None = None,
    ):

        _data_override_set_time = self.cfms.cFMS_data_override_set_time

        year_t = ctypes.c_int
        month_t = ctypes.c_int
        day_t = ctypes.c_int
        hour_t = ctypes.c_int
        minute_t = ctypes.c_int
        second_t = ctypes.c_int
        tick_t = ctypes.c_int
        err_msg_t = ctypes.c_char_p

        year_c = year_t(year) if year is not None else None
        month_c = month_t(month) if month is not None else None
        day_c = day_t(day) if day is not None else None
        hour_c = hour_t(hour) if hour is not None else None
        minute_c = minute_t(minute) if minute is not None else None
        second_c = second_t(second) if second is not None else None
        tick_c = tick_t(tick) if tick is not None else None
        err_msg_c = err_msg_t("NONE".encode("utf-8"))

        _data_override_set_time.restype = None
        _data_override_set_time.argtypes = [
            ctypes.POINTER(year_t),
            ctypes.POINTER(month_t),
            ctypes.POINTER(day_t),
            ctypes.POINTER(hour_t),
            ctypes.POINTER(minute_t),
            ctypes.POINTER(second_t),
            ctypes.POINTER(tick_t),
            ctypes.POINTER(err_msg_t),
        ]

        _data_override_set_time(
            year_c, month_c, day_c, hour_c, minute_c, second_c, tick_c, err_msg_c
        )

    def data_override_scalar(
        self,
        gridname: str,
        fieldname: str,
        data_type: Any,
        data_index: int | None = None,
    ) -> np.float32 | np.float64:

        _data_override_scalar = self.cfms.cFMS_data_override_0d_cdouble
        gridname_t = ctypes.c_char_p
        fieldname_t = ctypes.c_char_p
        data_t = ctypes.c_float if data_type is np.float32 else ctypes.c_double
        override_t = ctypes.c_bool
        data_index_t = ctypes.c_int

        gridname_c = gridname_t(gridname.encode("utf-8"))
        fieldname_c = fieldname_t(fieldname.encode("utf-8"))
        data_c = data_t(-99.99)
        override_c = ctypes.c_bool(False)
        data_index_c = data_index_t(data_index) if data_index is not None else None

        _data_override_scalar.restype = None
        _data_override_scalar.argtypes = [
            gridname_t,
            fieldname_t,
            ctypes.POINTER(data_t),
            ctypes.POINTER(override_t),
            ctypes.POINTER(data_index_t),
        ]

        _data_override_scalar(gridname_c, fieldname_c, data_c, override_c, data_index_c)

        # TODO:  add check for override
        return data_c.value

    def data_override_2d_float(self,
                               gridname: str,
                               fieldname: str,
                               data_shape: list[int],
                               data_type: Any, 
                               is_in: int | None = None,
                               ie_in: int | None = None,
                               js_in: int | None = None,
                               je_in: int | None = None) -> npt.NDArray:
        
        _data_override_2d_cfloat = self.cfms.cFMS_data_override_2d_cfloat
        
        ndata = np.prod(data_shape)
        
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
        data = np.ascontiguousarray(np.zeros(data_shape, dtype=np.float32, order="C"))
        override = override_t(False)
        is_in_c = is_in_t(is_in) if is_in is not None else None
        js_in_c = js_in_t(js_in) if js_in is not None else None
        ie_in_c = ie_in_t(ie_in) if ie_in is not None else None
        je_in_c = je_in_t(je_in) if je_in is not None else None

        
        _data_override_2d_cdouble.restype = None
        _data_override_2d_cdouble.argtypes = [gridname_t,
                                             fieldname_t,
                                             data_shape_t,
                                             data_t,
                                             ctypes.POINTER(override_t),
                                             ctypes.POINTER(is_in_t),
                                             ctypes.POINTER(ie_in_t),
                                             ctypes.POINTER(js_in_t),
                                             ctypes.POINTER(je_in_t)]
        _data_override_2d_cdouble(gridname_c,
                                 fieldname_c,
                                 data_shape_c,
                                 data,
                                 override,
                                 is_in_c,
                                 js_in_c,
                                 ie_in_c,
                                 je_in_c)

        #TODO add check for override
        return data
    
    
    def data_override_2d_double(self,
                                gridname: str,
                                fieldname: str,
                                data_shape: list[int],
                                is_in: int | None = None,
                                ie_in: int | None = None,
                                js_in: int | None = None,
                                je_in: int | None = None) -> npt.NDArray:
        
        _data_override_2d_cdouble = self.cfms.cFMS_data_override_2d_cdouble
        
        ndata = np.prod(data_shape)
        
        gridname_t = ctypes.c_char_p
        fieldname_t = ctypes.c_char_p
        data_shape_t = np.ctypeslib.ndpointer(dtype=np.int32, ndim=(1), shape=(2))
        data_t = np.ctypeslib.ndpointer(dtype=np.float64, ndim=(2), shape=data_shape)
        override_t = ctypes.c_bool        
        is_in_t = ctypes.c_int
        ie_in_t = ctypes.c_int
        js_in_t = ctypes.c_int
        je_in_t = ctypes.c_int
        
        gridname_c = gridname_t(gridname.encode("utf-8"))
        fieldname_c = fieldname_t(fieldname.encode("utf-8"))
        data_shape_c = np.array(data_shape, dtype=np.int32)
        data = np.ascontiguousarray(np.zeros(data_shape, dtype=np.float64, order="C"))
        override = override_t(False)
        is_in_c = is_in_t(is_in) if is_in is not None else None
        js_in_c = js_in_t(js_in) if js_in is not None else None
        ie_in_c = ie_in_t(ie_in) if ie_in is not None else None
        je_in_c = je_in_t(je_in) if je_in is not None else None

        
        _data_override_2d_cdouble.restype = None
        _data_override_2d_cdouble.argtypes = [gridname_t,
                                             fieldname_t,
                                             data_shape_t,
                                             data_t,
                                             ctypes.POINTER(override_t),
                                             ctypes.POINTER(is_in_t),
                                             ctypes.POINTER(ie_in_t),
                                             ctypes.POINTER(js_in_t),
                                             ctypes.POINTER(je_in_t)]
        _data_override_2d_cdouble(gridname_c,
                                 fieldname_c,
                                 data_shape_c,
                                 data,
                                 override,
                                 is_in_c,
                                 js_in_c,
                                 ie_in_c,
                                 je_in_c)

        #TODO add check for override
        return data

    def data_override_2d(self,
                         gridname: str,
                         fieldname: str,
                         data_shape: list[int],
                         data_type: Any,
                         is_in: int | None = None,
                         ie_in: int | None = None,
                         js_in: int | None = None,
                         je_in: int | None = None) -> npt.NDArray:

        if data_type is np.float32 :
            return self.data_override_2d_float(gridname=gridname,
                                               fieldname=fieldname,
                                               data_shape=data_shape,
                                               is_in=is_in,
                                               ie_in=ie_in,
                                               js_in=js_in,
                                               je_in=je_in) 
        
        if data_type is np.float64 :
            return self.data_override_2d_double(gridname=gridname,
                                                fieldname=fieldname,
                                                data_shape=data_shape,
                                                is_in=is_in,
                                                ie_in=ie_in,
                                                js_in=js_in,
                                                je_in=je_in)
