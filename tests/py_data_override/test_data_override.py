import os
import numpy as np
import pytest
import pyfms

@pytest.mark.parallel
def test_data_override():

    pyfms = pyfms.pyFMS()
    mpp = pyfms.pyFMS_mpp(cFMS=pyfms.cFMS)
    mpp_domains = pyfms.pyFMS_mpp_domains(cFMS=pyfms.cFMS)

    ocn_domain_id = 0
    nx = 360
    ny = 180
    nz = 5
    ehalo = 2
    whalo = 2
    shalo = 2
    nhalo = 2

    global_indices = np.array([0, nx - 1, 0, ny - 1], dtype=np.int32, order="C")
    layout = np.array([2, 3], dtype=np.int32, order="C")

    mpp_domains.define_domains(
        global_indices=global_indices,
        layout=layout,
        ehalo=ehalo,
        whalo=whalo,
        shalo=shalo,
        nhalo=nhalo,
        domain_id=ocn_domain_id,
    )

    compute_dict = mpp_domains.get_compute_domain2(domain_id=ocn_domain_id)
    xsize = compute_dict["xsize"]
    ysize = compute_dict["ysize"]

    data_override = pyfms.pyDataOverride(pyfms.cFMS)
    data_override.init(ocn_domain_id=ocn_domain_id)
    data_override.set_time(
        year=1, month=1, day=3, hour=0, minute=0, second=0, tick=0
    )

    data = data_override.override_scalar(
        gridname="OCN", fieldname="runoff_scalar", data_type=np.float64
    )
    assert data == 2.0

    data = data_override.override(
        gridname="OCN",
        fieldname="runoff_2d",
        data_shape=(xsize, ysize),
        data_type=np.float64,
    )
    assert np.all(data == 200.0)

    data = data_override.data_override(
        gridname="OCN",
        fieldname="runoff_3d",
        data_shape=(xsize, ysize, nz),
        data_type=np.float64,
    )
    answers = np.array([200 + z + 1 for z in range(nz)] * xsize * ysize).reshape(
        xsize, ysize, nz
    )
    assert np.all(data == answers)

    pyfms.pyfms_end()
    assert data == 1.0


@pytest.mark.remove
def test_remove_files():
    os.removedir("INPUT")
    os.remove("input.nml")
    os.remove("data_table.yaml")
    assert not os.path.exists("INPUT")
    assert not os.isfile("input.nml")
    assert not os.isfile("data_table.yaml")
