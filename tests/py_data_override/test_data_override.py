import os

import numpy as np
import pytest

from pyfms import pyDataOverride, pyFMS, pyFMS_mpp, pyFMS_mpp_domains


@pytest.mark.parallel
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
        year=1, month=1, day=2, hour=0, minute=0, second=0, tick=0
    )
    data = do.data_override_scalar(
        gridname="OCN", fieldname="runoff_scalar", data_type=np.float64
    )
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
