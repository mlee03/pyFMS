import ctypes

import numpy as np
from numpy.typing import NDArray
from typing import Any

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


class diag_manager():

    __libpath: str = None
    __lib: ctypes.CDLL = None

    DIAG_ALL: int = None
    DIAG_OCEAN: int = None
    DIAG_OTHER: int = None
    
    @classmethod
    def setlib(cls, libpath, lib):
        cls.__libpath = libpath
        cls.__lib = lib

    @classmethod
    @property
    def lib(cls):
        return cls.__lib

    @classmethod
    @property
    def libpath(cls):
        return cls.__libpath

    @classmethod
    def init(
        cls,
        diag_model_subset: int = None,
        time_init: NDArray = None,
    ) -> str:
        err_msg = " "

        cls.DIAG_OTHER = ctypes.c_int.in_dll(cls.lib, "DIAG_OTHER")
        cls.DIAG_OCEAN = ctypes.c_int.in_dll(cls.lib, "DIAG_OCEAN")
        cls.DIAG_ALL = ctypes.c_int.in_dll(cls.lib,"DIAG_ALL")
        
        _cfms_diag_init = cls.lib.cFMS_diag_init

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

    @classmethod    
    def end(cls):
        _cfms_diag_end = cls.lib.cFMS_diag_end
        _cfms_diag_end.restype = None
        _cfms_diag_end()

    @classmethod
    def send_complete(
        cls,
        diag_field_id: int,
    ) -> str:

        err_msg = " "

        _cfms_diag_send_complete = cls.lib.cFMS_diag_send_complete

        diag_field_id_c, diag_field_id_t = setscalar_Cint32(diag_field_id)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        _cfms_diag_send_complete.argtypes = [diag_field_id_t, err_msg_t]
        _cfms_diag_send_complete.restype = None

        _cfms_diag_send_complete(diag_field_id_c, err_msg_c)

        return err_msg_c.value.decode("utf-8")

    @classmethod
    def set_field_init_time(
        cls,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int = None,
        tick: int = None,
    ) -> str:

        err_msg = " "

        _cfms_diag_set_field_init_time = cls.lib.cFMS_diag_set_field_init_time

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

    @classmethod
    def set_field_timestep(
        cls,
        diag_field_id: int,
        dseconds: int,
        ddays: int = None,
        dticks: int = None,
    ) -> str:

        err_msg = " "

        _cfms_diag_set_field_timestep = cls.lib.cFMS_diag_set_field_timestep

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

    @classmethod
    def advance_field_time(
        cls,
        diag_field_id: int,
    ):
        _cfms_diag_advance_field_time = cls.lib.cFMS_diag_advance_field_time

        diag_field_id_c, diag_field_id_t = setscalar_Cint32(diag_field_id)

        _cfms_diag_advance_field_time.argtypes = [diag_field_id_t]
        _cfms_diag_advance_field_time.restype = None

        _cfms_diag_advance_field_time(diag_field_id_c)

    @classmethod
    def set_time_end(
        cls,
        year: int = None,
        month: int = None,
        day: int = None,
        hour: int = None,
        minute: int = None,
        second: int = None,
        tick: int = None,
        err_msg: str = None,
    ):
        if err_msg is not None:
            err_msg = err_msg[:128]

        _cfms_set_time_end = cls.lib.cFMS_diag_set_time_end

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

    @classmethod
    def axis_init(
        cls,
        name: str,
        axis_data: NDArray,
        units: str,
        cart_name: str,
        long_name: str = None,
        set_name: str = None,
        direction: int = None,
        edges: int = None,
        aux: str = None,
        req: str = None,
        tile_count: int = None,
        domain_position: int = None,
        not_xy: bool = None,
    ) -> int:

        long_name = long_name[:64]
        set_name = set_name[:64]

        name_c, name_t = set_Cchar(name)
        naxis_data_c, naxis_data_t = setscalar_Cint32(axis_data.size)
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

        if axis_data.dtype == np.float64:
            _cfms_diag_axis_init_ = cls.lib.cFMS_diag_axis_init_cdouble
            axis_data_p, axis_data_t = setarray_Cdouble(axis_data)
        elif axis_data.dtype == np.float32:
            _cfms_diag_axis_init_ = cls.lib.cFMS_diag_axis_init_cfloat
            axis_data_p, axis_data_t = setarray_Cfloat(axis_data)
        else:
            raise RuntimeError("diag_axis_init datatype not supported")

        _cfms_diag_axis_init_.argtypes = [
            name_t,
            naxis_data_t,
            axis_data_t,
            units_t,
            cart_name_t,
            long_name_t,
            direction_t,
            set_name_t,
            edges_t,
            aux_t,
            req_t,
            tile_count_t,
            domain_position_t,
            not_xy_t,
        ]
        _cfms_diag_axis_init_.restype = ctypes.c_int

        return _cfms_diag_axis_init_(
            name_c,
            naxis_data_c,
            axis_data_p,
            units_c,
            cart_name_c,
            long_name_c,
            direction_c,
            set_name_c,
            edges_c,
            aux_c,
            req_c,
            tile_count_c,
            domain_position_c,
            not_xy_c,
        )

    @classmethod
    def register_field_array(
        cls,
        module_name: str,
        field_name: str,
        datatype,
        axes: list[int] = None,
        long_name: str = None,
        units: str = None,
        missing_value: int = None,
        range_data: list[np.int32|np.int64|np.float32|np.float64] = None,
        mask_variant: bool = None,
        standard_name: str = None,
        verbose: bool = None,
        do_not_log: bool = None,
        interp_method: str = None,
        tile_count: int = None,
        area: int = None,
        volume: int = None,
        realm: str = None,
        multiple_send_data: bool = None,
    ) -> int:

        err_msg = " "

        module_name = module_name[:64]
        field_name = field_name[:64]
        if long_name is not None:
            long_name = long_name[:64]
        if units is not None:
            units = units[:64]
        if standard_name is not None:
            standard_name = standard_name[:64]
        if interp_method is not None:
            interp_method = interp_method[:64]
        if realm is not None:
            realm = realm[:64]

        if axes is not None:
            axes_arr = axes
            while len(axes_arr) < 5:
                axes_arr.append(0)
            axes_arr = np.array(axes_arr, dtype=np.int32)

        if range_data is not None:
            range_data_arr = np.array(range_data, dtype=datatype)
                
        module_name_c, module_name_t = set_Cchar(module_name)
        field_name_c, field_name_t = set_Cchar(field_name)
        axes_p, axes_t = setarray_Cint32(axes_arr)
        long_name_c, long_name_t = set_Cchar(long_name)
        units_c, units_t = set_Cchar(units)
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

        if datatype == np.int32:
            _cfms_register_diag_field_array_ = (
                cls.lib.cFMS_register_diag_field_array_cint
            )
            range_data_p, range_data_t = setarray_Cint32(range_data_arr)
            missing_value_c, missing_value_t = setscalar_Cint32(missing_value)
        elif datatype == np.float64:
            _cfms_register_diag_field_array_ = (
                cls.lib.cFMS_register_diag_field_array_cdouble
            )
            range_data_p, range_data_t = setarray_Cdouble(range_data_arr)
            missing_value_c, missing_value_t = setscalar_Cdouble(missing_value)
        elif datatype == np.float32:
            _cfms_register_diag_field_array_ = (
                cls.lib.cFMS_register_diag_field_array_cfloat
            )
            range_data_p, range_data_t = setarray_Cfloat(range_data_arr)
            missing_value_c, missing_value_t = setscalar_Cfloat(missing_value)
        else:
            raise RuntimeError(
                "register diag field array range_data datatype not supported"
            )

        _cfms_register_diag_field_array_.argtypes = [
            module_name_t,
            field_name_t,
            axes_t,
            long_name_t,
            units_t,
            missing_value_t,
            range_data_t,
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
        _cfms_register_diag_field_array_.restype = ctypes.c_int

        return _cfms_register_diag_field_array_(
            module_name_c,
            field_name_c,
            axes_p,
            long_name_c,
            units_c,
            missing_value_c,
            range_data_p,
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

    @classmethod
    def register_field_scalar(
        cls,
        module_name: str,
        field_name: str,
        datatype,
        long_name: str = None,
        units: str = None,
        standard_name: str = None,
        missing_value: int = None,
        range_data: NDArray = None,
        do_not_log: bool = None,
        area: int = None,
        volume: int = None,
        realm: str = None,
        multiple_send_data: bool = None,
    ) -> int:

        err_msg = " "

        module_name = module_name[:64]
        field_name = field_name[:64]
        if long_name is not None:
            long_name = long_name[:64]
        if units is not None:
            units = units[:64]
        if standard_name is not None:
            standard_name = standard_name[:64]
        if realm is not None:
            realm = realm[:64]

        module_name_c, module_name_t = set_Cchar(module_name)
        field_name_c, field_name_t = set_Cchar(field_name)
        long_name_c, long_name_t = set_Cchar(long_name)
        units_c, units_t = set_Cchar(units)
        standard_name_c, standard_name_t = set_Cchar(standard_name)
        do_not_log_c, do_not_log_t = setscalar_Cbool(do_not_log)
        err_msg_c, err_msg_t = set_Cchar(err_msg)
        area_c, area_t = setscalar_Cint32(area)
        volume_c, volume_t = setscalar_Cint32(volume)
        realm_c, realm_t = set_Cchar(realm)
        multiple_send_data_c, multiple_send_data_t = setscalar_Cbool(multiple_send_data)

        if datatype == np.int32:
            _cfms_register_diag_field_scalar_ = (
                cls.lib.cFMS_register_diag_field_array_cint
            )
            range_data_p, range_data_t = setarray_Cint32(range_data)
            missing_value_c, missing_value_t = setscalar_Cint32(missing_value)
        elif datatype == np.float64:
            _cfms_register_diag_field_scalar_ = (
                cls.lib.cFMS_register_diag_field_array_cdouble
            )
            range_data_p, range_data_t = setarray_Cdouble(range_data)
            missing_value_c, missing_value_t = setscalar_Cdouble(missing_value)
        elif datatype == np.float32:
            _cfms_register_diag_field_scalar_ = (
                cls.lib.cFMS_register_diag_field_array_cfloat
            )
            range_data_p, range_data_t = setarray_Cfloat(range_data)
            missing_value_c, missing_value_t = setscalar_Cfloat(missing_value)
        else:
            raise RuntimeError(
                "register diag field array range_data datatype not supported"
            )

        _cfms_register_diag_field_scalar_.argtypes = [
            module_name_t,
            field_name_t,
            long_name_t,
            units_t,
            standard_name_t,
            missing_value_t,
            range_data_t,
            do_not_log_t,
            err_msg_t,
            area_t,
            volume_t,
            realm_t,
            multiple_send_data_t,
        ]
        _cfms_register_diag_field_scalar_.restype = ctypes.c_int

        return _cfms_register_diag_field_scalar_(
            module_name_c,
            field_name_c,
            long_name_c,
            units_c,
            standard_name_c,
            missing_value_c,
            range_data_p,
            do_not_log_c,
            err_msg_c,
            area_c,
            volume_c,
            realm_c,
            multiple_send_data_c,
        )

    @classmethod
    def send_data(
        cls,
        diag_field_id: int,
        field_shape: list[int],
        field: NDArray,
    ) -> bool:

        err_msg = " "

        diag_field_id_c, diag_field_id_t = setscalar_Cint32(diag_field_id)
        field_shape_arr = np.array(field_shape, dtype=np.int32)
        field_shape_p, field_shape_t = setarray_Cint32(field_shape_arr)
        err_msg_c, err_msg_t = set_Cchar(err_msg)

        if field_shape_arr.size == 2:
            if field.dtype == np.int32:
                _cfms_diag_send_data_ = cls.lib.cFMS_diag_send_data_2d_cint
                field_p, field_t = setarray_Cint32(field)
            elif field.dtype == np.float64:
                _cfms_diag_send_data_ = cls.lib.cFMS_diag_send_data_2d_cdouble
                field_p, field_t = setarray_Cdouble(field)
            elif field.dtype == np.float32:
                _cfms_diag_send_data_ = cls.lib.cFMS_diag_send_data_2d_cfloat
                field_p, field_t = setarray_Cfloat(field)
            else:
                raise RuntimeError(f"diag_send_data {field.dtype} unsupported")
        elif field_shape_arr.size == 3:
            if field.dtype == np.int32:
                _cfms_diag_send_data_ = cls.lib.cFMS_diag_send_data_3d_cint
                field_p, field_t = setarray_Cint32(field)
            elif field.dtype == np.float64:
                _cfms_diag_send_data_ = cls.lib.cFMS_diag_send_data_3d_cdouble
                field_p, field_t = setarray_Cdouble(field)
            elif field.dtype == np.float32:
                _cfms_diag_send_data_ = cls.lib.cFMS_diag_send_data_3d_cfloat
                field_p, field_t = setarray_Cfloat(field)
            else:
                raise RuntimeError(f"diag_send_data {field.dtype} unsupported")
        elif field_shape_arr.size == 4:
            if field.dtype == np.int32:
                _cfms_diag_send_data_ = cls.lib.cFMS_diag_send_data_4d_cint
                field_p, field_t = setarray_Cint32(field)
            elif field.dtype == np.float64:
                _cfms_diag_send_data_ = cls.lib.cFMS_diag_send_data_4d_cdouble
                field_p, field_t = setarray_Cdouble(field)
            elif field.dtype == np.float32:
                _cfms_diag_send_data_ = cls.lib.cFMS_diag_send_data_4d_cfloat
                field_p, field_t = setarray_Cfloat(field)
            else:
                raise RuntimeError(f"diag_send_data {field.dtype} unsupported")
        elif field_shape_arr.size == 5:
            if field.dtype == np.int32:
                _cfms_diag_send_data_ = cls.lib.cFMS_diag_send_data_5d_cint
                field_p, field_t = setarray_Cint32(field)
            elif field.dtype == np.float64:
                _cfms_diag_send_data_ = cls.lib.cFMS_diag_send_data_5d_cdouble
                field_p, field_t = setarray_Cdouble(field)
            elif field.dtype == np.float32:
                _cfms_diag_send_data_ = cls.lib.cFMS_diag_send_data_5d_cfloat
                field_p, field_t = setarray_Cfloat(field)
            else:
                raise RuntimeError(f"diag_send_data {field.dtype} unsupported")
        else:
            raise RuntimeError(
                f"diag_send_data {field_shape_arr.size} dimensions unsupported"
            )

        _cfms_diag_send_data_.argtypes = [
            diag_field_id_t,
            field_shape_t,
            field_t,
            err_msg_t,
        ]
        _cfms_diag_send_data_.restype = ctypes.c_bool

        return _cfms_diag_send_data_(
            diag_field_id_c,
            field_shape_p,
            field_p,
            err_msg_c,
        )
