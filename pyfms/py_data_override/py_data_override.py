import ctypes
from typing import Optional

import numpy as np


class pyDataOverride:

    def __init__(self, cFMS: ctypes.CDLL = None):
        self.cfms = cFMS

    def data_override_init(
        self,
        atm_domain_id: Optional[int] = None,
        ocn_domain_id: Optional[int] = None,
        ice_domain_id: Optional[int] = None,
        land_domain_id: Optional[int] = None,
        land_domainUG_id: Optional[int] = None,
        mode: Optional[int] = None,
    ):

        _data_override_init = self.cfms.cFMS_data_override_init

        atm_domain_id_t = ctypes.c_int
        ocn_domain_id_t = ctypes.c_int
        ice_domain_id_t = ctypes.c_int
        land_domain_id_t = ctypes.c_int
        land_domainUG_id_t = ctypes.c_int
        mode_t = ctypes.c_int

        if atm_domain_id is not None:
            atm_domain_id = atm_domain_id_t(atm_domain_id)
        if ocn_domain_id is not None:
            ocn_domain_id = ocn_domain_id_t(ocn_domain_id)
        if ice_domain_id is not None:
            ice_domain_id = ice_domain_id_t(ice_domain_id)
        if land_domain_id is not None:
            land_domain_id = land_domain_id_t(land_domain_id)
        if land_domainUG_id is not None:
            land_domainUG_id = land_domainUG_id_t(land_domainUG_id)
        if mode is not None:
            mode = mode_t(mode)

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
            atm_domain_id,
            ocn_domain_id,
            ice_domain_id,
            land_domain_id,
            land_domainUG_id,
            mode,
        )
