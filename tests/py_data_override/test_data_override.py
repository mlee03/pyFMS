import numpy as np

from pyfms import pyDataOverride, pyFMS, pyFMS_mpp, pyFMS_mpp_domains


def test_data_override():

    pyfms = pyFMS()
    mpp = pyFMS_mpp(cFMS=pyfms.cFMS)
    mpp_domains = pyFMS_mpp_domains(cFMS=pyfms.cFMS)

    ocn_domain_id = 0
    nx = 360
    ny = 180
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

    do = pyDataOverride(pyfms.cFMS)
    do.data_override_init(ocn_domain_id=ocn_domain_id)
    do.data_override_set_time(
        year=1, month=1, day=3, hour=0, minute=0, second=0, tick=0
    )

    data = do.data_override_scalar(
        gridname="OCN", fieldname="runoff_scalar", data_type=np.float64
    )
    assert data == 2.0

    data = do.data_override_2d(
        gridname="OCN",
        fieldname="runoff_2d",
        data_shape=(xsize, ysize),
        data_type=np.float64,
    )

    assert np.all(data == 200.0)

    pyfms.pyfms_end()
