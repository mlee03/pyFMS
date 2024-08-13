import ctypes as ct
import numpy as np
import dataclasses

import libFMS
import pyFMS_mpp
import pyFMS_typing as fmstype




def diag_axis_init(
    name: str,
    array_data: np.ndarray,
    units: str,
    cart_name: str,
    lib: ct.CDLL,    
) -> ct.c_int:
    
    name, name_t = fmstype.setarg_c(name)
    dim = len(array_data.shape)
    dim, dim_t = fmstype.setarg_i4(dim)
    units, units_t = fmstype.setarg_c(units)
    cart_name, cart_name_t = fmstype.setarg_c(cart_name)

    if (np.all(array_data.dtype) == ct.c_float):
        array_data, array_data_t = fmstype.setarg_r4(array_data)
        _pyFMS_diag_axis_init = getattr(lib, "__pyFMS_diag_manager_mod_MOD_pyFMS_diag_axis_init_r4")
        _pyFMS_diag_axis_init.argtypes = [ name_t, dim_t, array_data_t, units_t, cart_name_t ]
        _pyFMS_diag_axis_init.restype = ct.c_int
        return _pyFMS_diag_axis_init(name, dim, array_data, units, cart_name)
    elif (np.all(array_data.dtype) == ct.c_double):
        array_data, array_data_t = fmstype.setarg_r8(array_data)
        _pyFMS_diag_axis_init = getattr(lib, "__pyFMS_diag_manager_mod_MOD_pyFMS_diag_axis_init_r8")
        _pyFMS_diag_axis_init.argtypes = [ name_t, dim_t, array_data_t, units_t, cart_name_t ]
        _pyFMS_diag_axis_init.restype = ct.c_int
        return _pyFMS_diag_axis_init(name, dim, array_data, units, cart_name)
    else:
        print("pyFMS_diag_manager::diag_axis_init array_data type unknown")




def send_data(
        diag_field_id: int,
        field,
        lib: ct.CDLL,
) -> ct.c_bool:
    
    diag_field_id, diag_field_id_t = fmstype.setarg_i4(diag_field_id)

    if not hasattr(field, "__len__"):
        if (np.all(field.dtype) == ct.c_float):
            field, field_t = fmstype.setarg_r4(field[0])
            _pyFMS_send_data = getattr(lib, "__pyFMS_diag_manager_mod_MOD_pyFMS_send_data_0d_r4")
            _pyFMS_send_data.argtypes = [ diag_field_id_t, field_t ]
            _pyFMS_send_data.restype = ct.c_bool
            return _pyFMS_send_data(diag_field_id, field)
        elif (np.all(field.dtype) == ct.c_double):
            field, field_t = fmstype.setarg_r8(field[0])
            _pyFMS_send_data = getattr(lib, "__pyFMS_diag_manager_mod_MOD_pyFMS_send_data_0d_r8")
            _pyFMS_send_data.argtypes = [ diag_field_id_t, field_t ]
            _pyFMS_send_data.restype = ct.c_bool
            return _pyFMS_send_data(diag_field_id, field)
        else:
            print("pyFMS_diag_manager::send_data_0d field data type unknown")
    elif len(field.shape) == 1:
        n = field.shape[0]
        n, n_t = fmstype.setarg_i4(n)
        if (np.all(field.dtype) == ct.c_float):
            field, field_t = fmstype.setarg_r4(field)
            _pyFMS_send_data = getattr(lib, "__pyFMS_diag_manager_mod_MOD_pyFMS_send_data_1d_r4")
            _pyFMS_send_data.argtypes = [ diag_field_id_t, n_t, field_t ]
            _pyFMS_send_data.restype = ct.c_bool
            return _pyFMS_send_data(diag_field_id, n, field)
        elif (np.all(field.dtype) == ct.c_double):
            field, field_t = fmstype.setarg_r8(field)
            _pyFMS_send_data = getattr(lib, "__pyFMS_diag_manager_mod_MOD_pyFMS_send_data_1d_r8")
            _pyFMS_send_data.argtypes = [ diag_field_id_t, n_t, field_t ]
            _pyFMS_send_data.restype = ct.c_bool
            return _pyFMS_send_data(diag_field_id, n, field)
        else:
            print("pyFMS_diag_manager::send_data_1d field data type unknown")
    elif len(field.shape) == 2:
        n = field.shape[0]
        m = field.shape[1]
        n, n_t = fmstype.setarg_i4(n)
        m, m_t = fmstype.setarg_i4(m)
        if (np.all(field.dtype) == ct.c_float):
            field, field_t = fmstype.setarg_r4(field)
            _pyFMS_send_data = getattr(lib, "__pyFMS_diag_manager_mod_MOD_pyFMS_send_data_2d_r4")
            _pyFMS_send_data.argtypes = [ diag_field_id_t, n_t, m_t, field_t ]
            _pyFMS_send_data.restype = ct.c_bool
            return _pyFMS_send_data(diag_field_id, n, m, field)
        elif (np.all(field.dtype) == ct.c_double):
            field, field_t = fmstype.setarg_r8(field)
            _pyFMS_send_data = getattr(lib, "__pyFMS_diag_manager_mod_MOD_pyFMS_send_data_2d_r8")
            _pyFMS_send_data.argtypes = [ diag_field_id_t, n_t, m_t, field_t ]
            _pyFMS_send_data.restype = ct.c_bool
            return _pyFMS_send_data(diag_field_id, n, m, field)
        else:
            print("pyFMS_diag_manager::send_data_2d field data type unknown")
    elif len(field.shape) == 3:
        n = field.shape[0]
        m = field.shape[1]
        l = field.shape[2]
        n, n_t = fmstype.setarg_i4(n)
        m, m_t = fmstype.setarg_i4(m)
        l, l_t = fmstype.setarg_i4(l)
        if (np.all(field.dtype) == ct.c_float):
            field, field_t = fmstype.setarg_r4(field)
            _pyFMS_send_data = getattr(lib, "__pyFMS_diag_manager_mod_MOD_pyFMS_send_data_3d_r4")
            _pyFMS_send_data.argtypes = [ diag_field_id_t, n_t, m_t, l_t, field_t ]
            _pyFMS_send_data.restype = ct.c_bool
            return _pyFMS_send_data(diag_field_id, n, m, l, field)
        elif (np.all(field.dtype) == ct.c_double):
            field, field_t = fmstype.setarg_r8(field)
            _pyFMS_send_data = getattr(lib, "__pyFMS_diag_manager_mod_MOD_pyFMS_send_data_3d_r8")
            _pyFMS_send_data.argtypes = [ diag_field_id_t, n_t, m_t, l_t, field_t ]
            _pyFMS_send_data.restype = ct.c_bool
            return _pyFMS_send_data(diag_field_id, n, m, l, field)
        else:
            print("pyFMS_diag_manager::send_data_3d field data type unknown")
    elif len(field.shape) == 4:
        n = field.shape[0]
        m = field.shape[1]
        l = field.shape[2]
        k = field.shape[3]
        n, n_t = fmstype.setarg_i4(n)
        m, m_t = fmstype.setarg_i4(m)
        l, l_t = fmstype.setarg_i4(l)
        k, k_t = fmstype.setarg_i4(k)
        if (np.all(field.dtype) == ct.c_float):
            field, field_t = fmstype.setarg_r4(field)
            _pyFMS_send_data = getattr(lib, "__pyFMS_diag_manager_mod_MOD_pyFMS_send_data_4d_r4")
            _pyFMS_send_data.argtypes = [ diag_field_id_t, n_t, m_t, l_t, k_t, field_t ]
            _pyFMS_send_data.restype = ct.c_bool
            return _pyFMS_send_data(diag_field_id, n, m, l, k, field)
        elif (np.all(field.dtype) == ct.c_double):
            field, field_t = fmstype.setarg_r8(field)
            _pyFMS_send_data = getattr(lib, "__pyFMS_diag_manager_mod_MOD_pyFMS_send_data_4d_r8")
            _pyFMS_send_data.argtypes = [ diag_field_id_t, n_t, m_t, l_t, k_t, field_t ]
            _pyFMS_send_data.restype = ct.c_bool
            return _pyFMS_send_data(diag_field_id, n, m, l, k, field)
        else:
            print("pyFMS_diag_manager::send_data_4d field data type unknown")
    else:
        print("pyFMS_diag_manager::send_data rank of field unknown")




def diag_field_add_attribute(
        diag_field_id: int,
        att_name: str,
        att_value,
        lib: ct.CDLL,
):
    diag_field_id, diag_field_id_t = fmstype.setarg_i4(diag_field_id)
    att_name, att_name_t = fmstype.setarg_c(att_name)
    n, n_t = fmstype.setarg_i4(n)

    if hasattr(att_value, "__len__"):
        if np.all(att_value.dtype == ct.c_float):
            att_value, att_value_t = fmstype.setarg_r4(att_value)
            _pyFMS_diag_field_add_attribute = getattr(lib, "__pyFMS_diag_manager_mod_MOD_pyFMS_diag_field_add_attribute_scalar_r4")
            _pyFMS_diag_field_add_attribute.argtypes = [ diag_field_id_t, att_name_t, att_value_t]
            _pyFMS_diag_field_add_attribute(diag_field_id, att_name, att_value)
        elif np.all(att_value.dtype == ct.c_double):
            att_value, att_value_t = fmstype.setarg_r4(att_value)
            _pyFMS_diag_field_add_attribute = getattr(lib, "__pyFMS_diag_manager_mod_MOD_pyFMS_diag_field_add_attribute_scalar_r8")
            _pyFMS_diag_field_add_attribute.argtypes = [ diag_field_id_t, att_name_t, att_value_t]
            _pyFMS_diag_field_add_attribute(diag_field_id, att_name, att_value)
        else:
            print("pyFMS_diag_manager::diag_field_add_attribute_scalar att_value type unknown")
    elif not hasattr(att_value, "__len__"):
        n = att_value.shape[0]
        n, n_t = fmstype.setarg_i4(n)
        if np.all(att_value.dtype == ct.c_float):
            att_value, att_value_t = fmstype.setarg_r4(att_value)
            _pyFMS_diag_field_add_attribute = getattr(lib, "__pyFMS_diag_manager_mod_MOD_pyFMS_diag_field_add_attribute_array_r4")
            _pyFMS_diag_field_add_attribute.argtypes = [ diag_field_id_t, att_name_t, n_t, att_value_t]
            _pyFMS_diag_field_add_attribute(diag_field_id, att_name, n, att_value)
        elif np.all(att_value.dtype == ct.c_double):
            att_value, att_value_t = fmstype.setarg_r4(att_value)
            _pyFMS_diag_field_add_attribute = getattr(lib, "__pyFMS_diag_manager_mod_MOD_pyFMS_diag_field_add_attribute_array_r8")
            _pyFMS_diag_field_add_attribute.argtypes = [ diag_field_id_t, att_name_t, n_t, att_value_t]
            _pyFMS_diag_field_add_attribute(diag_field_id, att_name, n, att_value)
        else:
            print("pyFMS_diag_manager::diag_field_add_attribute_array att_value type unknown")
    else:
        print("pyFMS_diag_manager::diag_field_add_attribute_array att_value type unknown")




def register_diag_field(
        module_name: str,
        field_name: str,
        lib: ct.CDLL,
        axes: np.ndarray = None,
) -> ct.c_int:
    
    module_name, module_name_t = fmstype.setarg_c(module_name)
    field_name, field_name_t = fmstype.setarg_c(field_name)

    if axes:
        n = axes.shape(0)
        n, n_t = fmstype.setarg_i4(n)
        axes, axes_t = fmstype.setarg_i4(axes)
        _pyFMS_register_diag_field = getattr(lib, "__pyFMS_mod_MOD_pyFMS_diag_field")
        _pyFMS_register_diag_field.argtypes = [ module_name_t, field_name_t, n_t, axes_t ]
        _pyFMS_register_diag_field.restype = ct.c_int
        return _pyFMS_register_diag_field(module_name, field_name, n, axes)
    else:
        _pyFMS_register_diag_field = getattr(lib, "__pyFMS_mod_MOD_pyFMS_diag_field")
        _pyFMS_register_diag_field.argtypes = [ module_name_t, field_name_t ]
        _pyFMS_register_diag_field.restype = ct.c_int
        return _pyFMS_register_diag_field(module_name, field_name, n)




def register_static_field(
        module_name: str,
        field_name: str,
        lib: ct.CDLL,
        axes: np.ndarray,
) -> ct.c_int:
    
    module_name, module_name_t = fmstype.setarg_c(module_name)
    field_name, field_name_t = fmstype.setarg_c(field_name)
    n = axes.shape(0)
    n, n_t = fmstype.setarg_i4(n)
    axes, axes_t = fmstype.setarg_i4(axes)
    _pyFMS_register_diag_field = getattr(lib, "__pyFMS_mod_MOD_pyFMS_diag_field")
    _pyFMS_register_diag_field.argtypes = [ module_name_t, field_name_t, n_t, axes_t ]
    _pyFMS_register_diag_field.restype = ct.c_int
    return _pyFMS_register_diag_field(module_name, field_name, n, axes)
    


        



    
