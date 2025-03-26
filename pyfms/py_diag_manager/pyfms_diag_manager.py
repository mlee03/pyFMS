import ctypes
from typing import Optional

from numpy.typing import NDArray

from pyfms.pyfms_utils.data_handling import (
    set_Cchar,
    setarray_Cdouble,
    setarray_Cfloat,
    setarray_Cint32,
    setscalar_Cbool,
    setscalar_Cdouble,
    setscalar_Cfloat,
    setscalar_Cint32,
)


class pyFMS_diag_manager:

    def __init__(self, clibFMS: ctypes.CDLL = None):
        self.clibFMS = clibFMS

    def diag_end(self):
        _cfms_diag_end = self.clibFMS.cFMS_diag_end

        _cfms_diag_end.restype = None

        _cfms_diag_end()

    def diag_init(
        self,
        diag_model_subset: Optional[int] = None,
        time_init: Optional[NDArray] = None,
        err_msg: Optional[str] = None,
    ) -> str:
        if err_msg is not None:
            err_msg = err_msg[:128]

        _cfms_diag_init = self.clibFMS.cFMS_diag_init

        diag_model_subset_c, diag_model_subset_t = setscalar_Cint32(diag_model_subset)
        time_init_p, time_init_t = setarray_Cint32(time_init)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_diag_init.argtypes = [
            diag_model_subset_t,
            time_init_t,
            err_msg_t,
        ]
        _cfms_diag_init.restype = None

        _cfms_diag_init(diag_model_subset_c, time_init_p, err_msg_c)

        return err_msg_c.value.decode("utf-8")

    def diag_send_complete(
        self,
        diag_field_id: int,
        err_msg: Optional[str] = None,
    ) -> str:

        if err_msg is not None:
            err_msg = err_msg[:128]

        _cfms_diag_send_complete = self.clibFMS.CFMS_diag_send_complete

        diag_field_id_c, diag_field_id_t = setscalar_Cint32(diag_field_id)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_diag_send_complete.argtypes = [diag_field_id_t, err_msg_t]
        _cfms_diag_send_complete.restype = None

        _cfms_diag_send_complete(diag_field_id_c, err_msg_c)

        return err_msg_c.value.decode("utf-8")

    def diag_set_field_init_time(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: Optional[int] = None,
        tick: Optional[int] = None,
        err_msg: Optional[str] = None,
    ) -> str:

        if err_msg is not None:
            err_msg = err_msg[:128]

        _cfms_diag_set_field_init_time = self.clibFMS.cFMS_diag_set_field_init_time

        year_c, year_t = setscalar_Cint32(year)
        month_c, month_t = setscalar_Cint32(month)
        day_c, day_t = setscalar_Cint32(day)
        hour_c, hour_t = setscalar_Cint32(hour)
        minute_c, minute_t = setscalar_Cint32(minute)
        second_c, second_t = setscalar_Cint32(second)
        tick_c, tick_t = setscalar_Cint32(tick)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_diag_set_field_init_time.argtypes = [
            year_t,
            month_t,
            day_t,
            hour_t,
            minute_t,
            second_t,
            tick_t,
            err_msg_t,
        ]
        _cfms_diag_set_field_init_time.restype = None

        _cfms_diag_set_field_init_time(
            year_c, month_c, day_c, hour_c, minute_c, second_c, tick_c, err_msg_c
        )

        return err_msg_c.value.decode("utf-8")

    def diag_set_field_timestep(
        self,
        diag_field_id: int,
        dseconds: int,
        ddays: Optional[int] = None,
        dticks: Optional[int] = None,
        err_msg: Optional[str] = None,
    ) -> str:

        if err_msg is not None:
            err_msg = err_msg[:128]

        _cfms_diag_set_field_timestep = self.clibFMS.cFMS_diag_set_field_timestep

        diag_field_id_c, diag_field_id_t = setscalar_Cint32(diag_field_id)
        dseconds_c, dseconds_t = setscalar_Cint32(dseconds)
        ddays_c, ddays_t = setscalar_Cint32(ddays)
        dticks_c, dticks_t = setscalar_Cint32(dticks)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_diag_set_field_timestep.argtypes = [
            diag_field_id_t,
            dseconds_t,
            ddays_t,
            dticks_t,
            err_msg_t,
        ]
        _cfms_diag_set_field_timestep.restype = None

        _cfms_diag_set_field_timestep(
            diag_field_id_c, dseconds_c, ddays_c, dticks_c, err_msg_c
        )

        return err_msg_c.value.decode("utf-8")

    def diag_advance_field_time(
        self,
        diag_field_id: int,
    ):
        _cfms_diag_advance_field_time = self.clibFMS.cFMS_diag_advance_field_time

        diag_field_id_c, diag_field_id_t = setscalar_Cint32(diag_field_id)

        _cfms_diag_advance_field_time.argtypes = [diag_field_id_t]
        _cfms_diag_advance_field_time.restype = None

        _cfms_diag_advance_field_time(diag_field_id_c)

    def diag_set_time_end(
        self,
        year: Optional[int] = None,
        month: Optional[int] = None,
        day: Optional[int] = None,
        hour: Optional[int] = None,
        minute: Optional[int] = None,
        second: Optional[int] = None,
        tick: Optional[int] = None,
        err_msg: Optional[str] = None,
    ):
        if err_msg is not None:
            err_msg = err_msg[:128]

        _cfms_set_time_end = self.clibFMS.diag_set_time_end

        year_c, year_t = setscalar_Cint32(year)
        month_c, month_t = setscalar_Cint32(month)
        day_c, day_t = setscalar_Cint32(day)
        hour_c, hour_t = setscalar_Cint32(hour)
        minute_c, minute_t = setscalar_Cint32(minute)
        second_c, second_t = setscalar_Cint32(second)
        tick_c, tick_t = setscalar_Cint32(tick)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_set_time_end.argtypes = [
            year_t,
            month_t,
            day_t,
            hour_t,
            minute_t,
            second_t,
            tick_t,
            err_msg_t,
        ]
        _cfms_set_time_end.restype = None

        _cfms_set_time_end(
            year_c,
            month_c,
            day_c,
            hour_c,
            minute_c,
            second_c,
            tick_c,
            err_msg_c,
        )

    def diag_axis_init_cdouble(
        self,
        name: str,
        naxis_data: int,
        axis_data: NDArray,
        units: str,
        cart_name: str,
        long_name: Optional[str] = None,
        set_name: Optional[str] = None,
        direction: Optional[int] = None,
        edges: Optional[int] = None,
        aux: Optional[str] = None,
        req: Optional[str] = None,
        tile_count: Optional[int] = None,
        domain_position: Optional[int] = None,
        not_xy: Optional[bool] = None,
    ) -> int:
        _cfms_diag_axis_init_cdouble = self.clibFMS.cFMS_diag_axis_init_cdouble

        long_name = long_name[:64]
        set_name = set_name[:64]

        name_c, name_t = set_Cchar(name)
        naxis_data_c, naxis_data_t = setscalar_Cint32(naxis_data)
        axis_data_p, axis_data_t = setarray_Cdouble(axis_data)
        units_c, units_t = set_Cchar(units)
        cart_name_c, cart_name_t = set_Cchar(cart_name)
        long_name_c, long_name_t = set_Cchar(long_name)
        set_name_c, set_name_t = set_Cchar(set_name)
        direction_c, direction_t = setscalar_Cint32(direction)
        edges_c, edges_t = setscalar_Cint32(edges)
        aux_c, aux_t = set_Cchar(aux)
        req_c, req_t = set_Cchar(req)
        tile_count_c, tile_count_t = setscalar_Cint32(tile_count)
        domain_position_c, domain_position_t = setscalar_Cint32(domain_position)
        not_xy_c, not_xy_t = setscalar_Cbool(not_xy)

        _cfms_diag_axis_init_cdouble.argtypes = [
            name_t,
            naxis_data_t,
            axis_data_t,
            units_t,
            cart_name_t,
            long_name_t,
            set_name_t,
            direction_t,
            edges_t,
            aux_t,
            req_t,
            tile_count_t,
            domain_position_t,
            not_xy_t,
        ]
        _cfms_diag_axis_init_cdouble.restype = ctypes.c_int

        return _cfms_diag_axis_init_cdouble(
            name_c,
            naxis_data_c,
            axis_data_p,
            units_c,
            cart_name_c,
            long_name_c,
            set_name_c,
            direction_c,
            edges_c,
            aux_c,
            req_c,
            tile_count_c,
            domain_position_c,
            not_xy_c,
        )

    def diag_axis_init_cfloat(
        self,
        name: str,
        naxis_data: int,
        axis_data: NDArray,
        units: str,
        cart_name: str,
        long_name: Optional[str] = None,
        set_name: Optional[str] = None,
        direction: Optional[int] = None,
        edges: Optional[int] = None,
        aux: Optional[str] = None,
        req: Optional[str] = None,
        tile_count: Optional[int] = None,
        domain_position: Optional[int] = None,
        not_xy: Optional[bool] = None,
    ) -> int:
        _cfms_diag_axis_init_cfloat = self.clibFMS.cFMS_diag_axis_init_cfloat

        if long_name is not None:
            long_name = long_name[:64]
        if set_name is not None:
            set_name = set_name[:64]

        name_c, name_t = set_Cchar(name)
        naxis_data_c, naxis_data_t = setscalar_Cint32(naxis_data)
        axis_data_p, axis_data_t = setarray_Cfloat(axis_data)
        units_c, units_t = set_Cchar(units)
        cart_name_c, cart_name_t = set_Cchar(cart_name)
        long_name_c, long_name_t = set_Cchar(long_name)
        set_name_c, set_name_t = set_Cchar(set_name)
        direction_c, direction_t = setscalar_Cint32(direction)
        edges_c, edges_t = setscalar_Cint32(edges)
        aux_c, aux_t = set_Cchar(aux)
        req_c, req_t = set_Cchar(req)
        tile_count_c, tile_count_t = setscalar_Cint32(tile_count)
        domain_position_c, domain_position_t = setscalar_Cint32(domain_position)
        not_xy_c, not_xy_t = setscalar_Cbool(not_xy)

        _cfms_diag_axis_init_cfloat.argtypes = [
            name_t,
            naxis_data_t,
            axis_data_t,
            units_t,
            cart_name_t,
            long_name_t,
            set_name_t,
            direction_t,
            edges_t,
            aux_t,
            req_t,
            tile_count_t,
            domain_position_t,
            not_xy_t,
        ]
        _cfms_diag_axis_init_cfloat.restype = ctypes.c_int

        return _cfms_diag_axis_init_cfloat(
            name_c,
            naxis_data_c,
            axis_data_p,
            units_c,
            cart_name_c,
            long_name_c,
            set_name_c,
            direction_c,
            edges_c,
            aux_c,
            req_c,
            tile_count_c,
            domain_position_c,
            not_xy_c,
        )

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

    """
    2d send data wrappers
    """

    def diag_send_data_2d_cint(
        self,
        diag_field_id: int,
        field_shape: NDArray,
        field: NDArray,
        err_msg: Optional[str] = None,
    ) -> bool:

        err_msg = err_msg[:128]

        _cfms_diag_send_data_2d_cint = self.clibFMS.cFMS_diag_send_data_2d_cint

        diag_field_id_c, diag_field_id_t = setscalar_Cint32(diag_field_id)
        field_shape_p, field_shape_t = setarray_Cint32(field_shape)
        field_p, field_t = setarray_Cint32(field)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_diag_send_data_2d_cint.argtypes = [
            diag_field_id_t,
            field_shape_t,
            field_t,
            err_msg_t,
        ]
        _cfms_diag_send_data_2d_cint.restype = ctypes.c_bool

        return _cfms_diag_send_data_2d_cint(
            diag_field_id_c,
            field_shape_p,
            field_p,
            err_msg_c,
        )

    def diag_send_data_2d_cdouble(
        self,
        diag_field_id: int,
        field_shape: NDArray,
        field: NDArray,
        err_msg: Optional[str] = None,
    ) -> bool:

        err_msg = err_msg[:128]

        _cfms_diag_send_data_2d_cdouble = self.clibFMS.cFMS_diag_send_data_2d_cdouble

        diag_field_id_c, diag_field_id_t = setscalar_Cint32(diag_field_id)
        field_shape_p, field_shape_t = setarray_Cint32(field_shape)
        field_p, field_t = setarray_Cdouble(field)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_diag_send_data_2d_cdouble.argtypes = [
            diag_field_id_t,
            field_shape_t,
            field_t,
            err_msg_t,
        ]
        _cfms_diag_send_data_2d_cdouble.restype = ctypes.c_bool

        return _cfms_diag_send_data_2d_cdouble(
            diag_field_id_c,
            field_shape_p,
            field_p,
            err_msg_c,
        )

    def diag_send_data_2d_cfloat(
        self,
        diag_field_id: int,
        field_shape: NDArray,
        field: NDArray,
        err_msg: Optional[str] = None,
    ) -> bool:

        err_msg = err_msg[:128]

        _cfms_diag_send_data_2d_cfloat = self.clibFMS.cFMS_diag_send_data_2d_cfloat

        diag_field_id_c, diag_field_id_t = setscalar_Cint32(diag_field_id)
        field_shape_p, field_shape_t = setarray_Cint32(field_shape)
        field_p, field_t = setarray_Cfloat(field)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_diag_send_data_2d_cfloat.argtypes = [
            diag_field_id_t,
            field_shape_t,
            field_t,
            err_msg_t,
        ]
        _cfms_diag_send_data_2d_cfloat.restype = ctypes.c_bool

        return _cfms_diag_send_data_2d_cfloat(
            diag_field_id_c,
            field_shape_p,
            field_p,
            err_msg_c,
        )

    """
    3d send data wrappers
    """

    def diag_send_data_3d_cint(
        self,
        diag_field_id: int,
        field_shape: NDArray,
        field: NDArray,
        err_msg: Optional[str] = None,
    ) -> bool:

        err_msg = err_msg[:128]

        _cfms_diag_send_data_3d_cint = self.clibFMS.cFMS_diag_send_data_3d_cint

        diag_field_id_c, diag_field_id_t = setscalar_Cint32(diag_field_id)
        field_shape_p, field_shape_t = setarray_Cint32(field_shape)
        field_p, field_t = setarray_Cint32(field)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_diag_send_data_3d_cint.argtypes = [
            diag_field_id_t,
            field_shape_t,
            field_t,
            err_msg_t,
        ]
        _cfms_diag_send_data_3d_cint.restype = ctypes.c_bool

        return _cfms_diag_send_data_3d_cint(
            diag_field_id_c,
            field_shape_p,
            field_p,
            err_msg_c,
        )

    def diag_send_data_3d_cdouble(
        self,
        diag_field_id: int,
        field_shape: NDArray,
        field: NDArray,
        err_msg: Optional[str] = None,
    ) -> bool:

        err_msg = err_msg[:128]

        _cfms_diag_send_data_3d_cdouble = self.clibFMS.cFMS_diag_send_data_3d_cdouble

        diag_field_id_c, diag_field_id_t = setscalar_Cint32(diag_field_id)
        field_shape_p, field_shape_t = setarray_Cint32(field_shape)
        field_p, field_t = setarray_Cdouble(field)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_diag_send_data_3d_cdouble.argtypes = [
            diag_field_id_t,
            field_shape_t,
            field_t,
            err_msg_t,
        ]
        _cfms_diag_send_data_3d_cdouble.restype = ctypes.c_bool

        return _cfms_diag_send_data_3d_cdouble(
            diag_field_id_c,
            field_shape_p,
            field_p,
            err_msg_c,
        )

    def diag_send_data_3d_cfloat(
        self,
        diag_field_id: int,
        field_shape: NDArray,
        field: NDArray,
        err_msg: Optional[str] = None,
    ) -> bool:

        err_msg = err_msg[:128]

        _cfms_diag_send_data_3d_cfloat = self.clibFMS.cFMS_diag_send_data_3d_cfloat

        diag_field_id_c, diag_field_id_t = setscalar_Cint32(diag_field_id)
        field_shape_p, field_shape_t = setarray_Cint32(field_shape)
        field_p, field_t = setarray_Cfloat(arg=field)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_diag_send_data_3d_cfloat.argtypes = [
            diag_field_id_t,
            field_shape_t,
            field_t,
            err_msg_t,
        ]
        _cfms_diag_send_data_3d_cfloat.restype = ctypes.c_bool

        return _cfms_diag_send_data_3d_cfloat(
            diag_field_id_c,
            field_shape_p,
            field_p,
            err_msg_c,
        )

    """
    4d send data wrappers
    """

    def diag_send_data_4d_cint(
        self,
        diag_field_id: int,
        field_shape: NDArray,
        field: NDArray,
        err_msg: Optional[str] = None,
    ) -> bool:

        err_msg = err_msg[:128]

        _cfms_diag_send_data_4d_cint = self.clibFMS.cFMS_diag_send_data_4d_cint

        diag_field_id_c, diag_field_id_t = setscalar_Cint32(diag_field_id)
        field_shape_p, field_shape_t = setarray_Cint32(field_shape)
        field_p, field_t = setarray_Cint32(field)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_diag_send_data_4d_cint.argtypes = [
            diag_field_id_t,
            field_shape_t,
            field_t,
            err_msg_t,
        ]
        _cfms_diag_send_data_4d_cint.restype = ctypes.c_bool

        return _cfms_diag_send_data_4d_cint(
            diag_field_id_c,
            field_shape_p,
            field_p,
            err_msg_c,
        )

    def diag_send_data_4d_cdouble(
        self,
        diag_field_id: int,
        field_shape: NDArray,
        field: NDArray,
        err_msg: Optional[str] = None,
    ) -> bool:

        err_msg = err_msg[:128]

        _cfms_diag_send_data_4d_cdouble = self.clibFMS.cFMS_diag_send_data_4d_cdouble

        diag_field_id_c, diag_field_id_t = setscalar_Cint32(diag_field_id)
        field_shape_p, field_shape_t = setarray_Cint32(field_shape)
        field_p, field_t = setarray_Cdouble(field)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_diag_send_data_4d_cdouble.argtypes = [
            diag_field_id_t,
            field_shape_t,
            field_t,
            err_msg_t,
        ]
        _cfms_diag_send_data_4d_cdouble.restype = ctypes.c_bool

        return _cfms_diag_send_data_4d_cdouble(
            diag_field_id_c,
            field_shape_p,
            field_p,
            err_msg_c,
        )

    def diag_send_data_4d_cfloat(
        self,
        diag_field_id: int,
        field_shape: NDArray,
        field: NDArray,
        err_msg: Optional[str] = None,
    ) -> bool:

        err_msg = err_msg[:128]

        _cfms_diag_send_data_4d_cfloat = self.clibFMS.cFMS_diag_send_data_4d_cfloat

        diag_field_id_c, diag_field_id_t = setscalar_Cint32(diag_field_id)
        field_shape_p, field_shape_t = setarray_Cint32(field_shape)
        field_p, field_t = setarray_Cfloat(field)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_diag_send_data_4d_cfloat.argtypes = [
            diag_field_id_t,
            field_shape_t,
            field_t,
            err_msg_t,
        ]
        _cfms_diag_send_data_4d_cfloat.restype = ctypes.c_bool

        return _cfms_diag_send_data_4d_cfloat(
            diag_field_id_c,
            field_shape_p,
            field_p,
            err_msg_c,
        )

    """
    5d send data wrappers
    """

    def diag_send_data_5d_cint(
        self,
        diag_field_id: int,
        field_shape: NDArray,
        field: NDArray,
        err_msg: Optional[str] = None,
    ) -> bool:

        err_msg = err_msg[:128]

        _cfms_diag_send_data_5d_cint = self.clibFMS.cFMS_diag_send_data_5d_cint

        diag_field_id_c, diag_field_id_t = setscalar_Cint32(diag_field_id)
        field_shape_p, field_shape_t = setarray_Cint32(field_shape)
        field_p, field_t = setarray_Cint32(field)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_diag_send_data_5d_cint.argtypes = [
            diag_field_id_t,
            field_shape_t,
            field_t,
            err_msg_t,
        ]
        _cfms_diag_send_data_5d_cint.restype = ctypes.c_bool

        return _cfms_diag_send_data_5d_cint(
            diag_field_id_c,
            field_shape_p,
            field_p,
            err_msg_c,
        )

    def diag_send_data_5d_cdouble(
        self,
        diag_field_id: int,
        field_shape: NDArray,
        field: NDArray,
        err_msg: Optional[str] = None,
    ) -> bool:

        err_msg = err_msg[:128]

        _cfms_diag_send_data_5d_cdouble = self.clibFMS.cFMS_diag_send_data_5d_cdouble

        diag_field_id_c, diag_field_id_t = setscalar_Cint32(diag_field_id)
        field_shape_p, field_shape_t = setarray_Cint32(field_shape)
        field_p, field_t = setarray_Cdouble(field)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_diag_send_data_5d_cdouble.argtypes = [
            diag_field_id_t,
            field_shape_t,
            field_t,
            err_msg_t,
        ]
        _cfms_diag_send_data_5d_cdouble.restype = ctypes.c_bool

        return _cfms_diag_send_data_5d_cdouble(
            diag_field_id_c,
            field_shape_p,
            field_p,
            err_msg_c,
        )

    def diag_send_data_5d_cfloat(
        self,
        diag_field_id: int,
        field_shape: NDArray,
        field: NDArray,
        err_msg: Optional[str] = None,
    ) -> bool:

        err_msg = err_msg[:128]

        _cfms_diag_send_data_5d_cfloat = self.clibFMS.cFMS_diag_send_data_5d_cfloat

        diag_field_id_c, diag_field_id_t = setscalar_Cint32(diag_field_id)
        field_shape_p, field_shape_t = setarray_Cint32(field_shape)
        field_p, field_t = setarray_Cfloat(field)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_diag_send_data_5d_cfloat.argtypes = [
            diag_field_id_t,
            field_shape_t,
            field_t,
            err_msg_t,
        ]
        _cfms_diag_send_data_5d_cfloat.restype = ctypes.c_bool

        return _cfms_diag_send_data_5d_cfloat(
            diag_field_id_c,
            field_shape_p,
            field_p,
            err_msg_c,
        )
