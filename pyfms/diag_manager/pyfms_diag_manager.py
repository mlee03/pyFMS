import ctypes
from typing import Optional

import numpy as np
from numpy.typing import NDArray

from pyfms.pyfms_data_handling import(
    setarray_Cint32,
    setscalar_Cint32,
    set_Cchar,
)

class pyFMS_diag_manager:
    
    def __init__(self, clibFMS: ctypes.CDLL = None):
        self.clibFMS = clibFMS

    def diag_init(
            self,
            diag_model_subset: Optional[int] = None,
            time_init: Optional[NDArray] = None,
            calendar_type: Optional[int] = None,
    ) -> str:
        err_msg = ""

        _cfms_diag_init = self.clibFMS.cFMS_diag_init

        diag_model_subset_c, diag_model_subset_t = setscalar_Cint32(diag_model_subset)
        time_init_p, time_init_t = setarray_Cint32(time_init)
        calendar_type_c, calendar_type_t = setscalar_Cint32(calendar_type)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_diag_init.argtypes = [
            diag_model_subset_t,
            time_init_t,
            calendar_type_t,
            err_msg_t,
        ]
        _cfms_diag_init.restype = None

        _cfms_diag_init(
            diag_model_subset_c,
            time_init_p,
            calendar_type_c,
            err_msg_c
        )

        return err_msg_c.value.decode('utf-8')
    
    def diag_set_field_init_time(
        self,
        seconds: Optional[int] = None,
        days: Optional[int] = None,
        ticks: Optional[int] = None,
    ):
        _cfms_diag_set_field_init_time = self.clibFMS.cFMS_diag_set_field_init_time

        seconds_c, seconds_t = setscalar_Cint32(seconds)
        days_c, days_t = setscalar_Cint32(days)
        ticks_c, ticks_t = setscalar_Cint32(ticks)

        _cfms_diag_set_field_init_time.argtypes = [
            seconds_t,
            days_t,
            ticks_t,
        ]
        _cfms_diag_set_field_init_time.restype = None

        _cfms_diag_set_field_init_time(
            seconds_c,
            days_t,
            ticks_t
        )
