import ctypes as ct
import dataclasses
from typing import List, Optional

from pyfms.pyFMS_data_handling import *

@dataclasses.dataclass
class pyFMS_mpp:
    clibFMS: ct.CDLL = None
    
    def pyfms_declare_pelist(self, pelist: List[int], name_c: Optional[str]=None, commID: Optional[int]=None):
        _cfms_declare_pelist = self.clibFMS.cFMS_declare_pelist

        pelist_p, pelist_t = setarray_Cint32(pelist)
        name_c_p, name_c_t = set_Cchar(name_c)
        commID_p, commID_t = setscalar_Cint32(commID)

        _cfms_declare_pelist.argtypes = [pelist_t, name_c_t, commID_t]
        _cfms_declare_pelist.restype = None

        _cfms_declare_pelist(pelist_p, name_c_p, commID_p)

    def pyfms_get_current_pelist(self, pelist: List[int], name: Optional[str]=None, commID: Optional[int]=None):
        _cfms_get_current_pelist = self.clibFMS.cFMS_get_current_pelist

        pelist_p, pelist_t = setarray_Cint32(pelist)
        name_p, name_t = set_Cchar(name)
        commID_p, commID_t = setscalar_Cint32(commID)

        _cfms_get_current_pelist.argtypes = [pelist_t, name_t, commID_t]
        _cfms_get_current_pelist.restype = None

        _cfms_get_current_pelist(pelist_p, name_p, commID_p)

    def pyfms_npes(self) -> ct.c_int32:
        _cfms_npes = self.clibFMS.cFMS_npes

        _cfms_npes.restype = ct.c_int32

        return _cfms_npes()
    
    def pyfms_pe(self) -> ct.c_int32:
        _cfms_pe = self.clibFMS.cFMS_pe

        _cfms_pe.restype = ct.c_int32

        return _cfms_pe()
    
    def pyfms_set_current_pelist(self, pelist: Optional[List[int]]=None, no_sync: Optional[bool]=None):
        _cfms_set_current_pelist = self.clibFMS.cFMS_set_current_pelist

        pelist_p, pelist_t = setarray_Cint32(pelist)
        no_sync_p, no_sync_t = setscalar_Cbool(no_sync)

        _cfms_set_current_pelist.argtypes = [pelist_t, no_sync_t]
        _cfms_set_current_pelist.restype = None

        _cfms_set_current_pelist(pelist_p, no_sync_p)