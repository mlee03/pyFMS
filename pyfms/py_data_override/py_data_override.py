import ctypes


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
