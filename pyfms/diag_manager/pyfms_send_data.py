import ctypes
from typing import Optional

from numpy.typing import NDArray

from pyfms.pyfms_data_handling import (
    set_Cchar,
    set_multipointer,
    setarray_Cint32,
    setscalar_Cint32,
)


class pyFMS_send_data:

    def __init__(self, clibFMS: ctypes.CDLL = None):
        self.clibFMS = clibFMS

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
        field_p, field_t = set_multipointer(arg=field, num_ptr=2)
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
        field_p, field_t = set_multipointer(arg=field, num_ptr=2)
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
        field_p, field_t = set_multipointer(arg=field, num_ptr=2)
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
        field_p, field_t = set_multipointer(arg=field, num_ptr=3)
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
        field_p, field_t = set_multipointer(arg=field, num_ptr=3)
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
        field_p, field_t = set_multipointer(arg=field, num_ptr=3)
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
        field_p, field_t = set_multipointer(arg=field, num_ptr=4)
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
        field_p, field_t = set_multipointer(arg=field, num_ptr=4)
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
        field_p, field_t = set_multipointer(arg=field, num_ptr=4)
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
        field_p, field_t = set_multipointer(arg=field, num_ptr=5)
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
        field_p, field_t = set_multipointer(arg=field, num_ptr=5)
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
        field_p, field_t = set_multipointer(arg=field, num_ptr=5)
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
