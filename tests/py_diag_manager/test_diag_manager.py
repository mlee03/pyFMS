import numpy as np
import pyfms

def test_send_data():

    NX = 8
    NY = 8
    NZ = 2

    domain_id = 0
    calendar_type = pyfms.fms.NOLEAP

    DIAG_ALL = pyfms.diag_manager.DIAG_ALL
    
    var2_shape = [NX, NY]
    var2 = np.empty(shape=var2_shape, dtype=np.float32)
    
    var3_shape = [NX, NY, NZ]
    var3 = np.empty(shape=var3_shape, dtype=np.float32)

    for i in range(NX):
        for j in range(NY):
            for k in range(NZ):
                var3[i][j][k] = i * 100 + j * 10 + k * 1

    for i in range(NX):
        for j in range(NY):
            var2[i][j] = i * 10.0 + j * 1.0

    pyfms.fms.init()
    
    global_indices = [0, (NX - 1), 0, (NY - 1)]
    layout = [1, 1]
    io_layout = [1, 1]

    pyfms.mpp_domains.define_domains(
        domain_id=domain_id,
        global_indices=global_indices,
        layout=layout,
    )
    pyfms.mpp_domains.define_io_domain(
        domain_id=domain_id,
        io_layout=io_layout,
    )

    """
    diag manager init
    """

    pyfms.diag_manager.init(diag_model_subset=DIAG_ALL)

    pyfms.mpp_domains.set_current_domain(domain_id=domain_id)

    """
    diag axis init x
    """
    x = np.arange(NX, dtype=np.float64)

    id_x = pyfms.diag_manager.axis_init(
        name="x",
        axis_data=x,
        units="point_E",
        cart_name="x",
        long_name="point_E",
        set_name="atm",
    )

    """
    diag axis init y
    """
    y = np.arange(NY, dtype=np.float64)

    id_y = pyfms.diag_manager.axis_init(
        name="y",
        axis_data=y,
        units="point_N",
        cart_name="y",
        long_name="point_N",
        set_name="atm",
    )

    """
    diag axis init z
    """

    z = np.arange(NZ, dtype=np.float64)

    id_z = pyfms.diag_manager.axis_init(
        name="z",
        axis_data=z,
        units="point_Z",
        cart_name="z",
        long_name="point_Z",
        set_name="atm",
        not_xy=True,
    )

    """
    register diag field var3
    """

    axes_3d = [id_x, id_y, id_z]
    range_3d = [-1000.0, 1000.0]

    pyfms.diag_manager.set_field_init_time(
        year=2,
        month=1,
        day=1,
        hour=1,
        minute=1,
        second=1,
    )

    id_var3 = pyfms.diag_manager.register_field_array(
        module_name="atm_mod",
        field_name="var_3d",
        datatype=np.float32,
        axes=axes_3d,
        long_name="Var in a lon/lat domain",
        units="muntin",
        missing_value=-99.99,
        range_data=range_3d,
    )
    

    pyfms.diag_manager.set_field_timestep(
        diag_field_id=id_var3, dseconds=60 * 60, ddays=0, dticks=0
    )

    """
    register diag_field var 2
    """

    axes_2d = [id_x, id_y]
    range_2d = [-1000.0, 1000.0]

    pyfms.diag_manager.set_field_init_time(
        year=2,
        month=1,
        day=1,
        hour=1,
        minute=1,
        second=1,
    )

    id_var2 = pyfms.diag_manager.register_field_array(
        module_name="atm_mod",
        field_name="var_2d",
        datatype=np.float32,
        axes=axes_2d,
        long_name="Var in a lon/lat domain",
        units="muntin",
        missing_value=-99.99,
        range_data=range_2d,
    )

    pyfms.diag_manager.set_field_timestep(
        diag_field_id=id_var2,
        dseconds=60 * 60,
        ddays=0,
        dticks=0,
    )

    """
    diag set time end
    """

    pyfms.diag_manager.set_time_end(
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

    pyfms.diag_manager.send_data(
        diag_field_id=id_var3,
        field_shape=var3_shape,
        field=var3,
    )

    ntime = 24
    for itime in range(ntime):

        var3 = -var3

        pyfms.diag_manager.advance_field_time(diag_field_id=id_var3)
        pyfms.diag_manager.send_data(
            diag_field_id=id_var3,
            field_shape=var3_shape,
            field=var3,
        )
        pyfms.diag_manager.send_complete(diag_field_id=id_var3)

        var2 = -var2

        pyfms.diag_manager.advance_field_time(diag_field_id=id_var2)
        pyfms.diag_manager.send_data(
            diag_field_id=id_var2,
            field_shape=var2_shape,
            field=var2,
        )
        pyfms.diag_manager.send_complete(diag_field_id=id_var2)

    pyfms.diag_manager.end()
    pyfms.fms.end()


if __name__ == "__main__":
    test_send_data()
