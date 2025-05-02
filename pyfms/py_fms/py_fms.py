#!/usr/bin/env python3

import ctypes

from . import argtypes
from ..py_mpp.py_mpp_domains import mpp_domains
from ..py_mpp.py_mpp import mpp
from ..utils.constants import constants
from ..utils.ctypes_utils import setargs, setargs_arr, setargs_str


class fms:

    __libpath: str = None
    __lib: type[ctypes.CDLL] = None

    THIRTY_DAY_MONTHS: int = None
    GREGORIAN: int = None
    JULIAN: int = None
    NOLEAP: int = None

    @classmethod
    def setlib(cls, libpath: str, lib: type[ctypes.CDLL]):
        cls.__lib_path = libpath
        cls.__lib = lib

    @classmethod
    def lib(cls) -> type[ctypes.CDLL]:
        return cls.__lib

    @classmethod
    def libpath(cls) -> str:
        return cls.__libpath

    @classmethod
    def init(
        cls,
        alt_input_nml_path: str = None,
        localcomm: int = None,
        ndomain: int = None,
        nnest_domain: int = None,
        calendar_type: int = None,
    ):
        def get_constant(variable):
            return int(ctypes.c_int.in_dll(cls.lib(), variable).value)

        cls.THIRTY_DAY_MONTHS = get_constant("THIRTY_DAY_MONTHS")
        cls.GREGORIAN = get_constant("GREGORIAN")
        cls.JULIAN = get_constant("JULIAN")
        cls.NOLEAP = get_constant("NOLEAP")

        arglist = []
        setargs(localcomm, ctypes.c_int, arglist) 
        setargs_str(alt_input_nml_path, arglist)
        setargs(ndomain, ctypes.c_int, arglist)
        setargs(nnest_domain, ctypes.c_int, arglist)
        setargs(calendar_type, ctypes.c_int, arglist)

        cfms_init = cls.lib().cFMS_init
        cfms_init.argtypes = argtypes.fms_init
        cfms_init.restype = None
        cfms_init(*arglist)
        
        mpp.init()
        mpp_domains.init()
        constants.init()

    """
    Subroutine: pyfms_end

    Calls the termination routines for all modules in the MPP package.
    Termination routine for the fms module. It also calls destructor routines
    for the mpp, mpp_domains, and mpp_io modules. If this routine is called
    more than once it will return silently. There are no arguments.
    """

    @classmethod
    def end(cls):
        cfms_end = cls.lib().cFMS_end
        cfms_end.restype = None
        cfms_end()
        
