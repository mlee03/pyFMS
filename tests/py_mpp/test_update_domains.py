import os

import numpy as np
import pytest

from pyfms import mpp, mpp_domains, pyFMS


@pytest.mark.create
def test_create_input_nml():
    inputnml = open("input.nml", "w")
    inputnml.close()
    assert os.path.isfile("input.nml")


@pytest.mark.parallel
def test_update_domains():

    nx = 8
    ny = 8
    npes = 4
    whalo = 2
    ehalo = 2
    nhalo = 2
    shalo = 2
    domain_id = 0

    pyfms_obj = pyFMS(cFMS_path="./cFMS/libcFMS/.libs/libcFMS.so")
    mpp_obj = pyFMS_mpp(cFMS=pyfms_obj.cFMS)
    mpp_domains_obj = pyFMS_mpp_domains(cFMS=pyfms_obj.cFMS)

    global_indices = [0, (nx - 1), 0, (ny - 1)]
    cyclic_global_domain = mpp_domains_obj.CYCLIC_GLOBAL_DOMAIN

    layout = mpp_domains_obj.define_layout(global_indices=global_indices, ndivs=npes)

    domain = mpp_domains_obj.define_domains(global_indices=global_indices,
                                            global_indices=global_indices,
                                            layout=layout,
                                            whalo=whalo,
                                            ehalo=ehalo,
                                            shalo=shalo,
                                            nhalo=nhalo,
                                            xflags=cyclic_global_domain,
                                            yflags=cyclic_global_domain)

    answers = np.array(
        [
            [
                [88, 98, 28, 38, 48, 58, 68, 78],
                [89, 99, 29, 39, 49, 59, 69, 79],
                [82, 92, 22, 32, 42, 52, 62, 72],
                [83, 93, 23, 33, 43, 53, 63, 73],
                [84, 94, 24, 34, 44, 54, 64, 74],
                [85, 95, 25, 35, 45, 55, 65, 75],
                [86, 96, 26, 36, 46, 56, 66, 76],
                [87, 97, 27, 37, 47, 57, 67, 77],
            ],
            [
                [84, 94, 24, 34, 44, 54, 64, 74],
                [85, 95, 25, 35, 45, 55, 65, 75],
                [86, 96, 26, 36, 46, 56, 66, 76],
                [87, 97, 27, 37, 47, 57, 67, 77],
                [88, 98, 28, 38, 48, 58, 68, 78],
                [89, 99, 29, 39, 49, 59, 69, 79],
                [82, 92, 22, 32, 42, 52, 62, 72],
                [83, 93, 23, 33, 43, 53, 63, 73],
            ],
            [
                [48, 58, 68, 78, 88, 98, 28, 38],
                [49, 59, 69, 79, 89, 99, 29, 39],
                [42, 52, 62, 72, 82, 92, 22, 32],
                [43, 53, 63, 73, 83, 93, 23, 33],
                [44, 54, 64, 74, 84, 94, 24, 34],
                [45, 55, 65, 75, 85, 95, 25, 35],
                [46, 56, 66, 76, 86, 96, 26, 36],
                [47, 57, 67, 77, 87, 97, 27, 37],
            ],
            [
                [44, 54, 64, 74, 84, 94, 24, 34],
                [45, 55, 65, 75, 85, 95, 25, 35],
                [46, 56, 66, 76, 86, 96, 26, 36],
                [47, 57, 67, 77, 87, 97, 27, 37],
                [48, 58, 68, 78, 88, 98, 28, 38],
                [49, 59, 69, 79, 89, 99, 29, 39],
                [42, 52, 62, 72, 82, 92, 22, 32],
                [43, 53, 63, 73, 83, 93, 23, 33],
            ],
        ],
        dtype=np.float32,
    )


    compute = mpp_domains_obj.get_compute_domain(
        domain_id=domain.domain_id, whalo=whalo, shalo=shalo
    )
    data = mpp_domains_obj.get_data_domain(
        domain_id=domain.domain_id, whalo=whalo, shalo=shalo
    )
    
    isc = compute["xbegin"]
    iec = compute["xend"]
    jsc = compute["ybegin"]
    jec = compute["yend"]
    xsize_c = compute["xsize"]
    ysize_c = compute["ysize"]
    xsize_d = data["xsize"]
    ysize_d = data["ysize"]

    global_data = np.zeros(shape=(xsize_d, ysize_d), dtype=np.float32)
    for ix in range(whalo, nx):
        for iy in range(shalo, ny):
            global_data[ix][iy] = iy*10 + ix

    idata = np.zeros(shape=(xsize_d, ysize_d), dtype=np.float32)
    idata[isc:iec][isc:iec] = global_data[isc:iec][jsc:jec]

    mpp_domains.update_domains(
        field=idata,
        domain_id=domain_id,
        whalo=whalo,
        ehalo=ehalo,
        shalo=shalo,
        nhalo=nhalo,
    )

    assert np.array_equal(idata, answers[mpp.pe()])

    pyfms.pyfms_end()


@pytest.mark.remove
def test_remove_input_nml():
    os.remove("input.nml")
    assert not os.path.isfile("input.nml")


if __name__ == "__main__":
    test_update_domains()
