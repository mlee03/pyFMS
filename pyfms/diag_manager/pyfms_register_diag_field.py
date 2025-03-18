import ctypes
from typing import Optional

from numpy.typing import NDArray

from pyfms.pyfms_data_handling import (
    set_Cchar,
    setarray_Cdouble,
    setarray_Cfloat,
    setarray_Cint32,
    setscalar_Cbool,
    setscalar_Cdouble,
    setscalar_Cfloat,
    setscalar_Cint32,
)

class pyFMS_register_diag_field:

    def __init__(self, clibFMS: ctypes.CDLL = None):
        self.clibFMS = clibFMS

    def register_diag_field_array_cint(
        self,
        module_name: str,
        field_name: str,
        axes: Optional[NDArray] = None,
        long_name: Optional[str] = None,
        units: Optional[str] = None,
        missing_value: Optional[int] = None,
        range: Optional[NDArray] = None,
        mask_variant: Optional[bool] = None,
        standard_name: Optional[str] = None,
        verbose: Optional[bool] = None,
        do_not_log: Optional[bool] = None,
        err_msg: Optional[str] = None,
        interp_method: Optional[str] = None,
        tile_count: Optional[int] = None,
        area: Optional[int] = None,
        volume: Optional[int] = None,
        realm: Optional[str] = None,
        multiple_send_data: Optional[bool] = None,
    ) -> int:

        module_name = module_name[:64]
        field_name = field_name[:64]
        if long_name is not None:
            long_name = long_name[:64]
        if units is not None:
            units = units[:64]
        if standard_name is not None:
            standard_name = standard_name[:64]
        if err_msg is not None:
            err_msg = err_msg[:64]
        if interp_method is not None:
            interp_method = interp_method[:64]
        if realm is not None:
            realm = realm[:64]

        _cfms_register_diag_field_array_cint = (
            self.clibFMS.cFMS_register_diag_field_array_cint
        )

        module_name_c, module_name_t = set_Cchar(module_name)
        field_name_c, field_name_t = set_Cchar(field_name)
        axes_p, axes_t = setarray_Cint32(axes)
        long_name_c, long_name_t = set_Cchar(long_name)
        units_c, units_t = set_Cchar(units)
        missing_value_c, missing_value_t = setscalar_Cint32(missing_value)
        range_p, range_t = setarray_Cint32(range)
        mask_variant_c, mask_variant_t = setscalar_Cbool(mask_variant)
        standard_name_c, standard_name_t = set_Cchar(standard_name)
        verbose_c, verbose_t = setscalar_Cbool(verbose)
        do_not_log_c, do_not_log_t = setscalar_Cbool(do_not_log)
        err_msg_c, err_msg_t = set_Cchar(err_msg)
        interp_method_c, interp_method_t = set_Cchar(interp_method)
        tile_count_c, tile_count_t = setscalar_Cint32(tile_count)
        area_c, area_t = setscalar_Cint32(area)
        volume_c, volume_t = setscalar_Cint32(volume)
        realm_c, realm_t = set_Cchar(realm)
        multiple_send_data_c, multiple_send_data_t = setscalar_Cbool(multiple_send_data)

        _cfms_register_diag_field_array_cint.argtypes = [
            module_name_t,
            field_name_t,
            axes_t,
            long_name_t,
            units_t,
            missing_value_t,
            range_t,
            mask_variant_t,
            standard_name_t,
            verbose_t,
            do_not_log_t,
            err_msg_t,
            interp_method_t,
            tile_count_t,
            area_t,
            volume_t,
            realm_t,
            multiple_send_data_t,
        ]
        _cfms_register_diag_field_array_cint.restype = ctypes.c_int

        return _cfms_register_diag_field_array_cint(
            module_name_c,
            field_name_c,
            axes_p,
            long_name_c,
            units_c,
            missing_value_c,
            range_p,
            mask_variant_c,
            standard_name_c,
            verbose_c,
            do_not_log_c,
            err_msg_c,
            interp_method_c,
            tile_count_c,
            area_c,
            volume_c,
            realm_c,
            multiple_send_data_c,
        )

    def register_diag_field_array_cdouble(
        self,
        module_name: str,
        field_name: str,
        axes: Optional[NDArray] = None,
        long_name: Optional[str] = None,
        units: Optional[str] = None,
        missing_value: Optional[float] = None,
        range: Optional[NDArray] = None,
        mask_variant: Optional[bool] = None,
        standard_name: Optional[str] = None,
        verbose: Optional[bool] = None,
        do_not_log: Optional[bool] = None,
        err_msg: Optional[str] = None,
        interp_method: Optional[str] = None,
        tile_count: Optional[int] = None,
        area: Optional[int] = None,
        volume: Optional[int] = None,
        realm: Optional[str] = None,
        multiple_send_data: Optional[bool] = None,
    ) -> int:

        module_name = module_name[:64]
        field_name = field_name[:64]
        if long_name is not None:
            long_name = long_name[:64]
        if units is not None:
            units = units[:64]
        if standard_name is not None:
            standard_name = standard_name[:64]
        if err_msg is not None:
            err_msg = err_msg[:64]
        if interp_method is not None:
            interp_method = interp_method[:64]
        if realm is not None:
            realm = realm[:64]

        _cfms_register_diag_field_array_cdouble = (
            self.clibFMS.cFMS_register_diag_field_array_cdouble
        )

        module_name_c, module_name_t = set_Cchar(module_name)
        field_name_c, field_name_t = set_Cchar(field_name)
        axes_p, axes_t = setarray_Cint32(axes)
        long_name_c, long_name_t = set_Cchar(long_name)
        units_c, units_t = set_Cchar(units)
        missing_value_c, missing_value_t = setscalar_Cdouble(missing_value)
        range_p, range_t = setarray_Cdouble(range)
        mask_variant_c, mask_variant_t = setscalar_Cbool(mask_variant)
        standard_name_c, standard_name_t = set_Cchar(standard_name)
        verbose_c, verbose_t = setscalar_Cbool(verbose)
        do_not_log_c, do_not_log_t = setscalar_Cbool(do_not_log)
        err_msg_c, err_msg_t = set_Cchar(err_msg)
        interp_method_c, interp_method_t = set_Cchar(interp_method)
        tile_count_c, tile_count_t = setscalar_Cint32(tile_count)
        area_c, area_t = setscalar_Cint32(area)
        volume_c, volume_t = setscalar_Cint32(volume)
        realm_c, realm_t = set_Cchar(realm)
        multiple_send_data_c, multiple_send_data_t = setscalar_Cbool(multiple_send_data)

        _cfms_register_diag_field_array_cdouble.argtypes = [
            module_name_t,
            field_name_t,
            axes_t,
            long_name_t,
            units_t,
            missing_value_t,
            range_t,
            mask_variant_t,
            standard_name_t,
            verbose_t,
            do_not_log_t,
            err_msg_t,
            interp_method_t,
            tile_count_t,
            area_t,
            volume_t,
            realm_t,
            multiple_send_data_t,
        ]
        _cfms_register_diag_field_array_cdouble.restype = ctypes.c_int

        return _cfms_register_diag_field_array_cdouble(
            module_name_c,
            field_name_c,
            axes_p,
            long_name_c,
            units_c,
            missing_value_c,
            range_p,
            mask_variant_c,
            standard_name_c,
            verbose_c,
            do_not_log_c,
            err_msg_c,
            interp_method_c,
            tile_count_c,
            area_c,
            volume_c,
            realm_c,
            multiple_send_data_c,
        )

    def register_diag_field_array_cfloat(
        self,
        module_name: str,
        field_name: str,
        axes: Optional[NDArray] = None,
        long_name: Optional[str] = None,
        units: Optional[str] = None,
        missing_value: Optional[float] = None,
        range: Optional[NDArray] = None,
        mask_variant: Optional[bool] = None,
        standard_name: Optional[str] = None,
        verbose: Optional[bool] = None,
        do_not_log: Optional[bool] = None,
        err_msg: Optional[str] = None,
        interp_method: Optional[str] = None,
        tile_count: Optional[int] = None,
        area: Optional[int] = None,
        volume: Optional[int] = None,
        realm: Optional[str] = None,
        multiple_send_data: Optional[bool] = None,
    ) -> int:

        module_name = module_name[:64]
        field_name = field_name[:64]
        if long_name is not None:
            long_name = long_name[:64]
        if units is not None:
            units = units[:64]
        if standard_name is not None:
            standard_name = standard_name[:64]
        if err_msg is not None:
            err_msg = err_msg[:64]
        if interp_method is not None:
            interp_method = interp_method[:64]
        if realm is not None:
            realm = realm[:64]

        _cfms_register_diag_field_array_cfloat = (
            self.clibFMS.cFMS_register_diag_field_array_cfloat
        )

        module_name_c, module_name_t = set_Cchar(module_name)
        field_name_c, field_name_t = set_Cchar(field_name)
        axes_p, axes_t = setarray_Cint32(axes)
        long_name_c, long_name_t = set_Cchar(long_name)
        units_c, units_t = set_Cchar(units)
        missing_value_c, missing_value_t = setscalar_Cfloat(missing_value)
        range_p, range_t = setarray_Cfloat(range)
        mask_variant_c, mask_variant_t = setscalar_Cbool(mask_variant)
        standard_name_c, standard_name_t = set_Cchar(standard_name)
        verbose_c, verbose_t = setscalar_Cbool(verbose)
        do_not_log_c, do_not_log_t = setscalar_Cbool(do_not_log)
        err_msg_c, err_msg_t = set_Cchar(err_msg)
        interp_method_c, interp_method_t = set_Cchar(interp_method)
        tile_count_c, tile_count_t = setscalar_Cint32(tile_count)
        area_c, area_t = setscalar_Cint32(area)
        volume_c, volume_t = setscalar_Cint32(volume)
        realm_c, realm_t = set_Cchar(realm)
        multiple_send_data_c, multiple_send_data_t = setscalar_Cbool(multiple_send_data)

        _cfms_register_diag_field_array_cfloat.argtypes = [
            module_name_t,
            field_name_t,
            axes_t,
            long_name_t,
            units_t,
            missing_value_t,
            range_t,
            mask_variant_t,
            standard_name_t,
            verbose_t,
            do_not_log_t,
            err_msg_t,
            interp_method_t,
            tile_count_t,
            area_t,
            volume_t,
            realm_t,
            multiple_send_data_t,
        ]
        _cfms_register_diag_field_array_cfloat.restype = ctypes.c_int

        return _cfms_register_diag_field_array_cfloat(
            module_name_c,
            field_name_c,
            axes_p,
            long_name_c,
            units_c,
            missing_value_c,
            range_p,
            mask_variant_c,
            standard_name_c,
            verbose_c,
            do_not_log_c,
            err_msg_c,
            interp_method_c,
            tile_count_c,
            area_c,
            volume_c,
            realm_c,
            multiple_send_data_c,
        )

    def register_diag_field_scalar_cint(
        self,
        module_name: str,
        field_name: str,
        long_name: Optional[str] = None,
        units: Optional[str] = None,
        standard_name: Optional[str] = None,
        missing_value: Optional[int] = None,
        range: Optional[NDArray] = None,
        do_not_log: Optional[bool] = None,
        err_msg: Optional[str] = None,
        area: Optional[int] = None,
        volume: Optional[int] = None,
        realm: Optional[str] = None,
        multiple_send_data: Optional[bool] = None,
    ) -> int:

        module_name = module_name[:64]
        field_name = field_name[:64]
        if long_name is not None:
            long_name = long_name[:64]
        if units is not None:
            units = units[:64]
        if standard_name is not None:
            standard_name = standard_name[:64]
        if err_msg is not None:
            err_msg = err_msg[:64]
        if realm is not None:
            realm = realm[:64]

        _cfms_register_diag_field_scalar_cint = (
            self.clibFMS.cFMS_register_diag_field_scalar_cint
        )

        module_name_c, module_name_t = set_Cchar(module_name)
        field_name_c, field_name_t = set_Cchar(field_name)
        long_name_c, long_name_t = set_Cchar(long_name)
        units_c, units_t = set_Cchar(units)
        standard_name_c, standard_name_t = set_Cchar(standard_name)
        missing_value_c, missing_value_t = setscalar_Cint32(missing_value)
        range_p, range_t = setarray_Cint32(range)
        do_not_log_c, do_not_log_t = setscalar_Cbool(do_not_log)
        err_msg_c, err_msg_t = set_Cchar(err_msg)
        area_c, area_t = setscalar_Cint32(area)
        volume_c, volume_t = setscalar_Cint32(volume)
        realm_c, realm_t = set_Cchar(realm)
        multiple_send_data_c, multiple_send_data_t = setscalar_Cbool(multiple_send_data)

        _cfms_register_diag_field_scalar_cint.argtypes = [
            module_name_t,
            field_name_t,
            long_name_t,
            units_t,
            standard_name_t,
            missing_value_t,
            range_t,
            do_not_log_t,
            err_msg_t,
            area_t,
            volume_t,
            realm_t,
            multiple_send_data_t,
        ]
        _cfms_register_diag_field_scalar_cint.restype = ctypes.c_int

        return _cfms_register_diag_field_scalar_cint(
            module_name_c,
            field_name_c,
            long_name_c,
            units_c,
            standard_name_c,
            missing_value_c,
            range_p,
            do_not_log_c,
            err_msg_c,
            area_c,
            volume_c,
            realm_c,
            multiple_send_data_c,
        )

    def register_diag_field_scalar_cdouble(
        self,
        module_name: str,
        field_name: str,
        long_name: Optional[str] = None,
        units: Optional[str] = None,
        standard_name: Optional[str] = None,
        missing_value: Optional[float] = None,
        range: Optional[NDArray] = None,
        do_not_log: Optional[bool] = None,
        err_msg: Optional[str] = None,
        area: Optional[int] = None,
        volume: Optional[int] = None,
        realm: Optional[str] = None,
        multiple_send_data: Optional[bool] = None,
    ) -> int:

        module_name = module_name[:64]
        field_name = field_name[:64]
        if long_name is not None:
            long_name = long_name[:64]
        if units is not None:
            units = units[:64]
        if standard_name is not None:
            standard_name = standard_name[:64]
        if err_msg is not None:
            err_msg = err_msg[:64]
        if realm is not None:
            realm = realm[:64]

        _cfms_register_diag_field_scalar_cdouble = (
            self.clibFMS.cFMS_register_diag_field_scalar_cdouble
        )

        module_name_c, module_name_t = set_Cchar(module_name)
        field_name_c, field_name_t = set_Cchar(field_name)
        long_name_c, long_name_t = set_Cchar(long_name)
        units_c, units_t = set_Cchar(units)
        standard_name_c, standard_name_t = set_Cchar(standard_name)
        missing_value_c, missing_value_t = setscalar_Cdouble(missing_value)
        range_p, range_t = setarray_Cdouble(range)
        do_not_log_c, do_not_log_t = setscalar_Cbool(do_not_log)
        err_msg_c, err_msg_t = set_Cchar(err_msg)
        area_c, area_t = setscalar_Cint32(area)
        volume_c, volume_t = setscalar_Cint32(volume)
        realm_c, realm_t = set_Cchar(realm)
        multiple_send_data_c, multiple_send_data_t = setscalar_Cbool(multiple_send_data)

        _cfms_register_diag_field_scalar_cdouble.argtypes = [
            module_name_t,
            field_name_t,
            long_name_t,
            units_t,
            standard_name_t,
            missing_value_t,
            range_t,
            do_not_log_t,
            err_msg_t,
            area_t,
            volume_t,
            realm_t,
            multiple_send_data_t,
        ]
        _cfms_register_diag_field_scalar_cdouble.restype = ctypes.c_int

        return _cfms_register_diag_field_scalar_cdouble(
            module_name_c,
            field_name_c,
            long_name_c,
            units_c,
            standard_name_c,
            missing_value_c,
            range_p,
            do_not_log_c,
            err_msg_c,
            area_c,
            volume_c,
            realm_c,
            multiple_send_data_c,
        )
    
    def register_diag_field_scalar_cfloat(
        self,
        module_name: str,
        field_name: str,
        long_name: Optional[str] = None,
        units: Optional[str] = None,
        standard_name: Optional[str] = None,
        missing_value: Optional[float] = None,
        range: Optional[NDArray] = None,
        do_not_log: Optional[bool] = None,
        err_msg: Optional[str] = None,
        area: Optional[int] = None,
        volume: Optional[int] = None,
        realm: Optional[str] = None,
        multiple_send_data: Optional[bool] = None,
    ) -> int:

        module_name = module_name[:64]
        field_name = field_name[:64]
        if long_name is not None:
            long_name = long_name[:64]
        if units is not None:
            units = units[:64]
        if standard_name is not None:
            standard_name = standard_name[:64]
        if err_msg is not None:
            err_msg = err_msg[:64]
        if realm is not None:
            realm = realm[:64]

        _cfms_register_diag_field_scalar_cfloat = (
            self.clibFMS.cFMS_register_diag_field_scalar_cfloat
        )

        module_name_c, module_name_t = set_Cchar(module_name)
        field_name_c, field_name_t = set_Cchar(field_name)
        long_name_c, long_name_t = set_Cchar(long_name)
        units_c, units_t = set_Cchar(units)
        standard_name_c, standard_name_t = set_Cchar(standard_name)
        missing_value_c, missing_value_t = setscalar_Cfloat(missing_value)
        range_p, range_t = setarray_Cfloat(range)
        do_not_log_c, do_not_log_t = setscalar_Cbool(do_not_log)
        err_msg_c, err_msg_t = set_Cchar(err_msg)
        area_c, area_t = setscalar_Cint32(area)
        volume_c, volume_t = setscalar_Cint32(volume)
        realm_c, realm_t = set_Cchar(realm)
        multiple_send_data_c, multiple_send_data_t = setscalar_Cbool(multiple_send_data)

        _cfms_register_diag_field_scalar_cfloat.argtypes = [
            module_name_t,
            field_name_t,
            long_name_t,
            units_t,
            standard_name_t,
            missing_value_t,
            range_t,
            do_not_log_t,
            err_msg_t,
            area_t,
            volume_t,
            realm_t,
            multiple_send_data_t,
        ]
        _cfms_register_diag_field_scalar_cfloat.restype = ctypes.c_int

        return _cfms_register_diag_field_scalar_cfloat(
            module_name_c,
            field_name_c,
            long_name_c,
            units_c,
            standard_name_c,
            missing_value_c,
            range_p,
            do_not_log_c,
            err_msg_c,
            area_c,
            volume_c,
            realm_c,
            multiple_send_data_c,
        )