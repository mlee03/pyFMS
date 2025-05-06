#!/usr/bin/env python3

from ctypes import CDLL, c_bool, c_double, c_float, c_int, POINTER

from ..py_mpp.py_mpp_domains import mpp_domains
from ..utils import constants
from ..utils.data_handling import set_Cchar, setscalar_Cint32


_libpath: str = None
_lib: type[CDLL] = None

NOTE: int = None
WARNING: int = None
FATAL: int = None
THIRTY_DAY_MONTHS: int = None
GREGORIAN: int = None
JULIAN: int = None
NOLEAP: int = None


def setlib(libpath: str, lib: type[CDLL]):
    global _libpath, _lib
    _lib_path = libpath
    _lib = lib
    
def lib() -> type[CDLL]:
    return _lib

def libpath(cls) -> str:
    return _libpath


def constants_init():
    def get_constant(variable):
        return int(c_int.in_dll(_lib, variable).value)
    
    global NOTE, WARNING, FATAL
    global THIRTY_DAY_MONTHS, GREGORIAN, JULIAN, NOLEAP

    NOTE = get_constant("NOTE")
    WARNING = get_constant("WARNING")
    FATAL = get_constant("FATAL")
    THIRTY_DAY_MONTHS = get_constant("THIRTY_DAY_MONTHS")
    GREGORIAN = get_constant("GREGORIAN")
    JULIAN = get_constant("JULIAN")
    NOLEAP = get_constant("NOLEAP")

    
def init(
        alt_input_nml_path: str = None,
        localcomm: int = None,
        ndomain: int = None,
        nnest_domain: int = None,
        calendar_type: int = None,
):
    
    cfms_init = _lib.cFMS_init
    
    localcomm_c, localcomm_t = setscalar_Cint32(localcomm)
    alt_input_nml_path_c, alt_input_nml_path_t = set_Cchar(alt_input_nml_path)
    ndomain_c, ndomain_t = setscalar_Cint32(ndomain)
    nnest_domain_c, nnest_domain_t = setscalar_Cint32(nnest_domain)
    calendar_type_c, calendar_type_t = setscalar_Cint32(calendar_type)
    
    _cfms_init.argtypes = [
        localcomm_t,
        alt_input_nml_path_t,
        ndomain_t,
        nnest_domain_t,
        calendar_type_t,
    ]
    _cfms_init.restype = None
    
    _cfms_init(
        localcomm_c,
        alt_input_nml_path_c,
        ndomain_c,
        nnest_domain_c,
        calendar_type_c,
    )
    mpp_domains.init()
    constants.init()
    
"""
Subroutine: pyfms_end

Calls the termination routines for all modules in the MPP package.
Termination routine for the fms module. It also calls destructor routines
for the mpp, mpp_domains, and mpp_io modules. If this routine is called
more than once it will return silently. There are no arguments.
"""

def end(cls):
    cfms_end = _lib.cFMS_end
    cfms_end.restype = None
    cfms_end()
