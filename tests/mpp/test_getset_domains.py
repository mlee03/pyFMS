import numpy as np

from pyfms import (
    pyFMS, 
    pyFMS_mpp, 
    pyFMS_mpp_domains, 
)
from pyfms.mpp.pyfms_pydomain import pyDomainData


def test_getset_domains():
    """
    global domain
          *     *     *     *
          *     *     *     *
    * * (2,5) (3,5) (4,5) (5,5) * *
    * * (2,4) (3,4) (4,4) (5,4) * *
    * * (2,3) (3,3) (4,3) (5,3) * *
    * * (2,2) (3,2) (4,2) (5,2) * *
          *     *     *     *
          *     *     *     *
    """
    domain_id = 0
    ndiv = 4
    global_indices = np.array([0, 3, 0, 3], dtype=np.int32, order="C")
    whalo = 2
    ehalo = 2
    shalo = 2
    nhalo = 2
    name = "test domain"

    pyfms = pyFMS(clibFMS_path="./cFMS/libcFMS/.libs/libcFMS.so")
    mpp = pyFMS_mpp(clibFMS=pyfms.clibFMS)
    mpp_domains = pyFMS_mpp_domains(clibFMS=pyfms.clibFMS)
    compute_domain_data = pyDomainData()
    data_domain_data = pyDomainData()

    # set domain

    layout = np.empty(shape=2, dtype=np.int32, order="C")
    mpp_domains.define_layout(global_indices=global_indices, ndivs=ndiv, layout=layout)

    mpp_domains.define_domains(
        global_indices=global_indices,
        layout=layout,
        domain_id=domain_id,
        name=name,
        whalo=whalo,
        ehalo=ehalo,
        shalo=shalo,
        nhalo=nhalo,
    )

    if not mpp_domains.domain_is_initialized(domain_id):
        mpp.pyfms_error(1, "error in setting domain")

    mpp.set_current_pelist()

    """
    flipping the domain:
    pe 0: isc=2, iec=3, jsc=2, jec=3 --> pe 3
    pe 1: isc=4, iec=5, jsc=2, jec=3 --> pe 2
    pe 2: isc=2, iec=3, jsc=4, jec=5 --> pe 1
    pe 3: isc=4, iec=5, jsc=4, jec=5 --> pe 0
    """

    isc = np.array([4, 2, 4, 2], dtype=np.int32, order="C")
    iec = np.array([5, 3, 5, 3], dtype=np.int32, order="C")
    jsc = np.array([4, 4, 2, 2], dtype=np.int32, order="C")
    jec = np.array([5, 5, 3, 3], dtype=np.int32, order="C")

    """
    pe 0: isd=0, ied=5, jsd=0, jed=5 --> pe 3
    pe 1: isd=2, ied=7, jsd=0, jed=5 --> pe 2
    pe 2: isd=0, ied=5, jsd=2, jed=7 --> pe 1
    pe 3: isd=2, ied=7, jsd=2, jed=7 --> pe 0
    """

    isd = np.array([2, 0, 2, 0], dtype=np.int32, order="C")
    ied = np.array([7, 5, 7, 5], dtype=np.int32, order="C")
    jsd = np.array([2, 2, 0, 0], dtype=np.int32, order="C")
    jed = np.array([7, 7, 5, 5], dtype=np.int32, order="C")

    pe = mpp.pe()
    tile_count = 0
    x_is_global = False
    y_is_global = False

    # set compute and data domains

    xsize = 2
    ysize = 2
    compute_domain_data.setup_set(
        xbegin = isc[pe],
        xend = iec[pe],
        ybegin = jsc[pe],
        yend = jec[pe],
        xsize = xsize,
        ysize = ysize,
        x_is_global = x_is_global,
        y_is_global = y_is_global,
        tile_count = tile_count,
    )
    mpp_domains.set_compute_domain(
        domain_id=domain_id,
        domain_data=compute_domain_data,
        whalo=whalo,
        shalo=shalo,
    )

    xsize = 6
    ysize = 6
    data_domain_data.setup_set(
        xbegin = isd[pe],
        xend = ied[pe],
        ybegin=jsd[pe],
        yend=jed[pe],
        xsize=xsize,
        ysize=ysize,
        x_is_global=x_is_global,
        y_is_global=y_is_global,
        tile_count=tile_count,
    )
    mpp_domains.set_data_domain(
        domain_id=domain_id,
        domain_data=data_domain_data,
        whalo=whalo,
        shalo=shalo,
    )

    # get domain

    blank_compute_domain = pyDomainData()
    blank_compute_domain.setup_get(
        xbegin=True,
        xend=True,
        ybegin=True,
        yend=True,
        xsize=True,
        ysize=True,
        xmax_size=True,
        ymax_size=True,
        x_is_global=True,
        y_is_global=True,
    )

    mpp_domains.get_compute_domain(
        domain_id=domain_id,
        domain_data=blank_compute_domain,
        position=None,
        whalo=whalo,
        shalo=shalo,
    )

    assert blank_compute_domain.xbegin.value == isc[pe]
    assert blank_compute_domain.xend.value == iec[pe]
    assert blank_compute_domain.ybegin.value == jsc[pe]
    assert blank_compute_domain.yend.value == jec[pe]
    assert blank_compute_domain.xsize.value == 2
    assert blank_compute_domain.ysize.value == 2
    assert blank_compute_domain.xmax_size.value == 2
    assert blank_compute_domain.ymax_size.value == 2
    assert blank_compute_domain.x_is_global.value is False
    assert blank_compute_domain.y_is_global.value is False

    blank_data_domain = pyDomainData()
    blank_data_domain.setup_get(
        xbegin=True,
        xend=True,
        ybegin=True,
        yend=True,
        xsize=True,
        ysize=True,
        xmax_size=True,
        ymax_size=True,
    )

    mpp_domains.get_data_domain(
        domain_id=domain_id,
        domain_data=blank_data_domain,
        position=None,
        whalo=whalo,
        shalo=shalo,
    )

    assert blank_data_domain.xbegin.value == isd[pe]
    assert blank_data_domain.xend.value == ied[pe]
    assert blank_data_domain.ybegin.value == jsd[pe]
    assert blank_data_domain.yend.value == jed[pe]
    assert blank_data_domain.xsize.value == 6
    assert blank_data_domain.ysize.value == 6
    assert blank_data_domain.xmax_size.value == 6
    assert blank_data_domain.ymax_size.value == 6

    pyfms.pyfms_end()


if __name__ == "__main__":
    test_getset_domains()
