#!/usr/bin/env python3

import ctypes
import os
from .pyfms_utils.data_handling import set_Cchar, setscalar_Cint32

class pyFMS:

    __cfms_path: str = None
    __cfms: ctypes.CDLL = None
    __initialized = False

    @classmethod
    def setlib(cls, cfms_path, cfms):
        if cls.__initialized: pass
        cls.__cfms_path = cfms_path
        cls.__cfms = cfms
        cls.__initialized = True
        
    @classmethod
    def changelib(cls, cfms):
        cls.__cfms = cfms
        cls.__initialized = True

    @classmethod
    def getlib(cls):
        return cls.__cfms_path, cls.__cfms

    @classmethod
    def get_initialized(cls):
        return cls.__is_initialized
    
    @classmethod
    def init(cls,
             alt_input_nml_path: str = None,
             localcomm: int = None,
             ndomain: int = None,
             nnest_domain: int = None,
             calendar_type: int = None,
    ):
        
        _cfms_init = cls.__cfms.cFMS_init
        
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

    """
    Subroutine: pyfms_end

    Calls the termination routines for all modules in the MPP package.
    Termination routine for the fms module. It also calls destructor routines
    for the mpp, mpp_domains, and mpp_io modules. If this routine is called
    more than once it will return silently. There are no arguments.
    """

    @classmethod
    def pyfms_end(cls):
        _cfms_end = cls.__cfms.cFMS_end
        _cfms_end.restype = None
        _cfms_end()


    @classmethod
    def set_pelist_npes(cls, npes_in: int):
        _cfms_set_npes = cls.__cfms.cFMS_set_pelist_npes

        npes_in_c, npes_in_t = setscalar_Cint32(npes_in)

        _cfms_set_npes.argtypes = [npes_in_t]
        _cfms_set_npes.restype = None

        _cfms_set_npes(npes_in_c)
