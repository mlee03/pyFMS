import os

import numpy as np

from pyfms import pyFMS, pyFMS_diag_manager, pyFMS_mpp_domains


def test_send_data():

    NX = 8
    NY = 8
    NZ = 2

    input_file = "input.nml"
    diag_table = "diag_table.yaml"

    input_text = """
&diag_manager_nml
    use_modern_diag = .true.
/"""

    diag_text = """
title: test_diag_manager
base_date: 2 1 1 1 1 1

diag_files:
- file_name: test_send_data
  freq: 1 hours
  time_units: hours
  unlimdim: time
  varlist:
  - module: atm_mod
    var_name: var_3d
    reduction: average
    kind: r4
    output_name: var3_avg
  - module: atm_mod
    var_name: var_2d
    reduction: average
    kind: r4
    output_name: var2_avg
    """

    with open(input_file, "w") as file1:
        file1.write(input_text)
    with open(diag_table, "w") as file2:
        file2.write(diag_text)

    domain_id = 0
    calendar_type = 4

    var2_shape = np.array([NX, NY], dtype=np.int32, order="C")
    var2 = np.empty(shape=NX * NY, dtype=np.float32, order="C")

    var3_shape = np.array([NX, NY, NZ], dtype=np.int32, order="C")
    var3 = np.empty(shape=NX * NY * NZ, dtype=np.float32, order="C")

    ijk = 0
    for i in range(NX):
        for j in range(NY):
            for k in range(NZ):
                var3[ijk] = i * 100 + j * 10 + k * 1
                ijk += 1

    ij = 0
    for i in range(NX):
        for j in range(NY):
            var2[ij] = i * 10.0 + j * 1.0
            ij += 1

    pyfms = pyFMS(calendar_type=calendar_type)
    mpp_domains = pyFMS_mpp_domains(cFMS=pyfms.cFMS)

    global_indices = np.array([0, NX - 1, 0, NY - 1], dtype=np.int32, order="C")
    layout = np.array([1, 1], dtype=np.int32, order="C")
    io_layout = np.array([1, 1], dtype=np.int32, order="C")

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
    err_msg = "None"

    diag_manager = pyFMS_diag_manager(clibFMS=pyfms.clibFMS)
    diag_manager.diag_init(
        diag_model_subset=diag_model_subset,
        calendar_type=calendar_type,
        err_msg=err_msg,
    )

    mpp_domains.set_current_domain(domain_id=domain_id)

    """
    diag axis init x
    """
    x = np.empty(shape=NX, dtype=np.float64, order="C")

    for i in range(NX):
        x[i] = i

    id_x = diag_manager.diag_axis_init_cdouble(
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
        domain_position=0,
    )

    """
    diag axis init y
    """
    y = np.empty(shape=NY, dtype=np.float64, order="C")

    for j in range(NY):
        y[j] = j

    id_y = diag_manager.diag_axis_init_cdouble(
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

    z = np.empty(shape=NZ, dtype=np.float64, order="C")

    for k in range(NZ):
        z[k] = k

    id_z = diag_manager.diag_axis_init_cdouble(
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

    axes_3d = np.array([id_x, id_y, id_z, 0, 0], dtype=np.int32, order="C")
    range_3d = np.array([-1000.0, 1000.0], dtype=np.float32, order="C")

    diag_manager.diag_set_field_init_time(
        year=2,
        month=1,
        day=1,
        hour=1,
        minute=1,
        second=1,
    )

    id_var3 = diag_manager.register_diag_field_array_cfloat(
        module_name="atm_mod",
        field_name="var_3d",
        axes=axes_3d,
        long_name="Var in a lon/lat domain",
        units="muntin",
        missing_value=-99.99,
        range=range_3d,
    )

    diag_manager.diag_set_field_timestep(
        diag_field_id=id_var3, dseconds=60 * 60, ddays=0, dticks=0
    )

    """
    register diag_field var 2
    """

    axes_2d = np.array([id_x, id_y, 0, 0, 0], dtype=np.int32, order="C")
    range_2d = np.array([-1000.0, 1000.0], dtype=np.float32, order="C")

    diag_manager.diag_set_field_init_time(
        year=2,
        month=1,
        day=1,
        hour=1,
        minute=1,
        second=1,
    )

    id_var2 = diag_manager.register_diag_field_array_cfloat(
        module_name="atm_mod",
        field_name="var_2d",
        axes=axes_2d,
        long_name="Var in a lon/lat domain",
        units="muntin",
        missing_value=-99.99,
        range=range_2d,
    )

    diag_manager.diag_set_field_timestep(
        diag_field_id=id_var2,
        dseconds=60 * 60,
        ddays=0,
        dticks=0,
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

    diag_manager.diag_send_data_3d_cfloat(
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
        diag_manager.diag_send_data_3d_cfloat(
            diag_field_id=id_var3,
            field_shape=var3_shape,
            field=var3,
        )
        diag_manager.diag_send_complete(diag_field_id=id_var3)

        ij = 0
        for i in range(NX):
            for j in range(NY):
                var2[ij] = -1.0 * var2[ij]
                ij += 1
        diag_manager.diag_advance_field_time(diag_field_id=id_var2)
        diag_manager.diag_send_data_2d_cfloat(
            diag_field_id=id_var2,
            field_shape=var2_shape,
            field=var2,
        )
        diag_manager.diag_send_complete(diag_field_id=id_var2)

    diag_manager.diag_end()

    pyfms.pyfms_end()

    os.remove(input_file)
    os.remove(diag_table)


if __name__ == "__main__":
    test_send_data()
