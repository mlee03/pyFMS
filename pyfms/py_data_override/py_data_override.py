import ctypes
from typing import Any

import numpy as np
import numpy.typing as npt
from . import argtypes
from ..py_mpp.py_mpp import mpp
from ..utils.ctypes_utils import setargs, setargs_str, setargs_arr, setargs_list, arraytype

class data_override:

    """
    Parameters for initializing data_override in FMS
    These parameters can be specified through data_override.init()
    mode=CFLOAT_MODE initializes data_override in 32-bit mode for real variables
    mode=CDOUBLE_MODE initializes data_override in 64-bit mode for real variables
    if mode is not specified, both 32-bit and 64-bit modes are initialized
    """

    CFLOAT_MODE: int = None
    CDOUBLE_MODE: int = None

    __libpath: str = None
    __lib: type[ctypes.CDLL] = None

    @classmethod
    def setlib(cls, libpath: str, lib: type[ctypes.CDLL]):
        cls.__libpath = libpath
        cls.__lib = lib

    @classmethod
    def lib(cls) -> type[ctypes.CDLL]:
        return cls.__lib

    @classmethod
    def libpath(cls) -> str:
        return cls.__libpath

    """
    pyfms.data_override.init()
    Calls data_override_init in FMS.  Domain_id's are required to pass in the
    domains data_override_init.  Domain_id's is generated through mpp_domains.define
    """

    @classmethod
    def init(
        cls,
        atm_domain_id: int = None,
        ocn_domain_id: int = None,
        ice_domain_id: int = None,
        land_domain_id: int = None,
        land_domainUG_id: int = None,
        mode: int = None,
    ):

        CFLOAT_MODE = int(ctypes.c_int.in_dll(cls.lib(), "CFLOAT_MODE").value)
        CDOUBLE_MODE = int(ctypes.c_int.in_dll(cls.lib(), "CDOUBLE_MODE").value)

        arglist = []
        setargs(atm_domain_id, ctypes.c_int, arglist)
        setargs(ocn_domain_id, ctypes.c_int, arglist)
        setargs(ice_domain_id, ctypes.c_int, arglist)
        setargs(land_domain_id, ctypes.c_int, arglist)
        setargs(land_domainUG_id, ctypes.c_int, arglist)
        setargs(mode, ctypes.c_int, arglist)
        
        data_override_init = cls.lib().cFMS_data_override_init
        data_override_init.restype = None
        data_override_init.argtypes = argtypes.data_override_init
                                        
        data_override_init(*arglist)

    """
    pyfms.data_override.set_time()
    Sets the time type in cFMS.  The set time will be used to specify
    targeted time for temporal interpolation in FMS data_override
    """

    @classmethod
    def set_time(
        cls,
        year: int = None,
        month: int = None,
        day: int = None,
        hour: int = None,
        minute: int = None,
        second: int = None,
        tick: int = None,
    ):

        data_override_set_time = cls.lib().cFMS_data_override_set_time

        arglist = []
        setargs(year, ctypes.c_int, arglist)
        setargs(month, ctypes.c_int, arglist)
        setargs(day, ctypes.c_int, arglist)
        setargs(hour, ctypes.c_int, arglist)
        setargs(minute, ctypes.c_int, arglist)
        setargs(second, ctypes.c_int, arglist)
        setargs(tick, ctypes.c_int, arglist)        
        error_msg_c = setargs_str(" ", arglist)
        
        data_override_set_time.restype = None
        data_override_set_time.argtypes = argtypes.data_override_set_time
        data_override_set_time(*arglist)

    """
    pyfms.data_override.override_scalar
    Calls data_override in FMS for scalar variables
    """

    @classmethod
    def override_scalar(
        cls,
        gridname: str,
        fieldname: str,
        datatype: np.float32|np.float64, 
        data_index: int = None,
    ) -> (np.float32|np.float64, bool):

        if datatype is np.float32:
            data_override_scalar = cls.lib().cFMS_data_override_0d_cfloat
        elif datatype is np.float64:
            data_override_scalar = cls.lib().cFMS_data_override_0d_cdouble
        else:
            mpp.error(mpp.FATAL, "datatype not supported in data_override")
            raise RuntimeError("datatype not supported in data_override")
        
        arglist = []
        setargs_str(gridname, arglist)
        setargs_str(fieldname, arglist)
        data_c = setargs(0.0, np.ctypeslib.as_ctypes_type(datatype), arglist)
        override_c = setargs(False, ctypes.c_bool, arglist)
        setargs(data_index, ctypes.c_int, arglist)

        #argtypes.data_override_scalar[2] = np.ctypeslib.as_ctypes_type(datatype)

        data_override_scalar.restype = None
        data_override_scalar.argtypes = argtypes.data_override_scalar
        data_override_scalar(*arglist)

        return data_c.value, override_c.value
        
    
    """
    pyfms.data_override.override
    Calls data override in FMS
    """

    @classmethod
    def override(
        cls,
        gridname: str,
        fieldname: str,
        data: npt.NDArray,
        is_in: int = None,
        ie_in: int = None,
        js_in: int = None,
        je_in: int = None,
    ) -> bool:

        if data.dtype is np.dtype(np.float32):
            if data.ndim == 2:
                _data_override = cls.lib().cFMS_data_override_2d_cfloat
            if data.ndim == 3:
                _data_override = cls.lib().cFMS_data_override_3d_cfloat
        elif data.dtype is np.dtype(np.float64):
            if data.ndim == 2:
                _data_override = cls.lib().cFMS_data_override_2d_cdouble
            if data.ndim == 3:
                _data_override = cls.lib().cFMS_data_override_3d_cdouble
        else:
            mpp.error(mpp.FATAL, f"datatype {data.dtype} not supported in data_override")
            raise RuntimeError(f"datatype {data.dtype} not supported in data_override")

        arglist = []
        setargs_str(gridname, arglist)
        setargs_str(fieldname, arglist)
        datashape = setargs_list(data.shape, np.int32, arglist)
        setargs_arr(data, data.dtype, arglist)
        override_c = setargs(False, ctypes.c_bool, arglist)
        setargs(is_in, ctypes.c_int, arglist)
        setargs(ie_in, ctypes.c_int, arglist)
        setargs(js_in, ctypes.c_int, arglist)
        setargs(je_in, ctypes.c_int, arglist)

        data_override.restype = None

        data_override.argtypes = argtypes.data_override
        data_override.argtypes[2] = arraytype(datashape, np.int32)
        data_override.argtypes[3] = arraytype(data, data.dtype)
        
        data_override(*arglist)

        return override_c.value
    
