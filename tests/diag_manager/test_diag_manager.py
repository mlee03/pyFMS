import numpy as np

from pyfms import (
    pyFMS,
    pyFMS_mpp_domains,
    pyFMS_diag_manager,
    pyFMS_diag_axis_init,
    pyFMS_register_diag_field,
    pyFMS_send_data,
)


def test_send_data():

    NX = 8
    NY = 8
    NZ = 2
    domain_id = 0
    var3_shape = np.array([NX, NY, NZ], dtype=np.int32, order="C")
    var3 = np.empty(shape=NX*NY*NZ, dtype=np.float32, order="C")
    ijk = 0

    for i in range(NX):
        for j in range(NY):
            for k in range(NZ):
                ijk += 1
                var3[ijk] = i*100 + j*10 + k*1

    pyfms = pyFMS(clibFMS_path="./cFMS/libcFMS/.libs/libcFMS.so")
    mpp_domains = pyFMS_mpp_domains(clibFMS=pyfms.clibFMS)

    global_indices = np.array([0, NX-1, 0, NY-1], dtype=np.int32, order="C")
    layout = np.array([1,1], dtype=np.int32, order="C")
    io_layout = np.array([1,1], dtype=np.int32, order="C")

    mpp_domains.define_domains(
        domain_id=domain_id,
        global_indices=global_indices,
        layout=layout,
    )
    mpp_domains.define_io_domain(
        domain_id=domain_id,
        io_layout=io_layout,
    )

    """
    diag manager init
    """

    diag_model_subset = 2
    time_init = np.empty(shape=6, dtype=np.int32, order="C")
    calendar_type = 4
    err_msg = "None"

    diag_manager = pyFMS_diag_manager(clibFMS=pyfms.clibFMS)
    diag_manager.diag_init(
        diag_model_subset=diag_model_subset,
        time_init=time_init,
        calendar_type=calendar_type,
        err_msg=err_msg
    )

    mpp_domains.set_current_domain(domain_id=domain_id)

    diag_axis = pyFMS_diag_axis_init(clibFMS=pyfms.clibFMS)

    """
    diag axis init x
    """
    x = np.array([NX], dtype=np.float64, order="C")

    for i in range(NX):
        x[i] = i

    id_x = diag_axis.diag_axis_init_cdouble(
        name="x",
        naxis_data=NX,
        axis_data=x,
        units="point_E",
        cart_name="x",
        long_name="point_E",
        set_name="atm",
        direction=0,
        edges=0,
        aux="",
        req="",
        tile_count=0,
        domain_position=0
    )

    """
    diag axis init y
    """
    y = np.array([NY], dtype=np.float64, order="C")

    for j in range(NY):
        y[j] = j

    id_y = diag_axis.diag_axis_init_cdouble(
        name="y",
        naxis_data=NY,
        axis_data=y,
        units="point_N",
        cart_name="y",
        long_name="point_N",
        set_name="atm",
        direction=0,
        edges=0,
        aux="",
        req="",
        tile_count=0,
        domain_position=0,
    )

    """
    diag axis init z
    """

    z = np.array([NZ], dtype=np.float64, order="C")

    for k in range(NZ):
        z[k] = k

    id_z = diag_axis.diag_axis_init_cdouble(
        name="z",
        naxis_data=NZ,
        axis_data=z,
        units="point_Z",
        cart_name="z",
        long_name="point_Z",
        set_name="atm",
        direction=0,
        edges=0,
        aux="",
        req="",
        tile_count=0,
        domain_position=0,
        not_xy=True,
    )

    """
    register diag field var3
    """
    
    register = pyFMS_register_diag_field(clibFMS=pyfms.clibFMS)

    axes = np.array([id_x, id_y, id_z, 0, 0], dtype=np.int32, order="C")
    range = np.array([-1000., 1000.], dtype=np.float32, order="C")

    diag_manager.diag_set_field_init_time(
        year=2,
        month=1,
        day=1,
        hour=1,
        minute=1,
        second=1,
        tick=0,
    )

    id_var3 = register.register_diag_field_array_cfloat(
        module_name="atm_mod",
        field_name="var_3d",
        axes=axes,
        long_name="Var in a lon/lat domain",
        units="muntin",
        missing_value=-99.99,
        range=range,
        mask_variant=False,
        standard_name="",
        verbose=False,
        do_not_log=False,
        interp_method="",
        tile_count=0,
        area=0,
        volume=0,
        realm="",
        multiple_send_data=False,
    )

    diag_manager.diag_set_field_timestep(
        diag_field_id=id_var3,
        dseconds=60*60,
        ddays=0,
        dticks=0
    )

    """
    diag set time end
    """

    diag_manager.diag_set_time_end(
        year=2,
        month=1,
        day=2,
        hour=1,
        minute=1,
        second=1,
        tick=0,
    )

    """
    send data
    """

    data_sender = pyFMS_send_data(clibFMS=pyfms.clibFMS)

    data_sender.diag_send_data_3d_cfloat(
        diag_field_id=id_var3,
        field_shape=var3_shape,
        field=var3,
    )

    for itime in range(24):
        ijk = 0
        for i in range(NX):
            for j in range(NY):
                for k in range(NZ):
                    var3[ijk] = -1.0 * var3[ijk]
                    ijk += 1
        diag_manager.diag_advance_field_time(diag_field_id=id_var3)
        data_sender.diag_send_data_3d_cfloat(
            diag_field_id=id_var3,
            field_shape=var3_shape,
            field=var3,
        )
        diag_manager.diag_send_complete(diag_field_id=id_var3)

    diag_manager.diag_end()

    pyfms.pyfms_end()


    