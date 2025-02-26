import numpy as np

from pyfms import Domain, pyFMS, pyFMS_mpp, pyFMS_mpp_domains


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
    domain = Domain()
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

    # set domain

    domain.global_indices = global_indices
    domain.domain_id = domain_id
    domain.whalo = whalo
    domain.ehalo = ehalo
    domain.shalo = shalo
    domain.nhalo = nhalo
    domain.name = name

    domain.layout = np.empty(shape=2, dtype=np.int32, order="C")
    mpp_domains.define_layout(
        global_indices=global_indices, ndivs=ndiv, layout=domain.layout
    )

    domain.tile_count, domain.tile_id = mpp_domains.define_domains(
        global_indices=domain.global_indices,
        layout=domain.layout,
        domain_id=domain.domain_id,
        pelist=domain.pelist,
        xflags=domain.xflags,
        yflags=domain.yflags,
        xhalo=domain.xhalo,
        yhalo=domain.yhalo,
        xextent=domain.xextent,
        yextent=domain.yextent,
        maskmap=domain.maskmap,
        name=domain.name,
        symmetry=domain.symmetry,
        memory_size=domain.memory_size,
        whalo=domain.whalo,
        ehalo=domain.ehalo,
        shalo=domain.shalo,
        nhalo=domain.nhalo,
        is_mosaic=domain.is_mosaic,
        tile_count=domain.tile_count,
        tile_id=domain.tile_id,
        complete=domain.complete,
        x_cyclic_offset=domain.x_cyclic_offset,
        y_cyclic_offset=domain.y_cyclic_offset,
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
    mpp_domains.set_compute_domain(
        domain_id=domain_id,
        xbegin=isc[pe],
        xend=iec[pe],
        ybegin=jsc[pe],
        yend=jec[pe],
        xsize=xsize,
        ysize=ysize,
        x_is_global=x_is_global,
        y_is_global=y_is_global,
        tile_count=tile_count,
        whalo=whalo,
        shalo=shalo,
    )

    xsize = 6
    ysize = 6
    mpp_domains.set_data_domain(
        domain_id=domain_id,
        xbegin=isd[pe],
        xend=ied[pe],
        ybegin=jsd[pe],
        yend=jed[pe],
        xsize=xsize,
        ysize=ysize,
        x_is_global=x_is_global,
        y_is_global=y_is_global,
        tile_count=tile_count,
        whalo=whalo,
        shalo=shalo,
    )

    # get domain

    is_check = 0
    ie_check = 0
    js_check = 0
    je_check = 0
    xsize_check = 0
    xmax_size_check = 0
    ysize_check = 0
    ymax_size_check = 0
    x_is_global_check = True
    y_is_global_check = True

    (
        is_check,
        ie_check,
        js_check,
        je_check,
        xsize_check,
        xmax_size_check,
        ysize_check,
        ymax_size_check,
        x_is_global_check,
        y_is_global_check,
        tile_count,
    ) = mpp_domains.get_compute_domain(
        domain_id=domain_id,
        xbegin=is_check,
        xend=ie_check,
        ybegin=js_check,
        yend=je_check,
        xsize=xsize_check,
        xmax_size=xmax_size_check,
        ysize=ysize_check,
        ymax_size=ymax_size_check,
        x_is_global=x_is_global_check,
        y_is_global=y_is_global_check,
        tile_count=tile_count,
        position=None,
        whalo=whalo,
        shalo=shalo,
    )

    assert is_check == isc[pe]
    assert ie_check == iec[pe]
    assert js_check == jsc[pe]
    assert je_check == jec[pe]
    assert xsize_check == 2
    assert ysize_check == 2
    assert xmax_size_check == 2
    assert ymax_size_check == 2
    assert x_is_global_check is False
    assert y_is_global_check is False

    (
        is_check,
        ie_check,
        js_check,
        je_check,
        xsize_check,
        xmax_size_check,
        ysize_check,
        ymax_size_check,
        x_is_global_check,
        y_is_global_check,
        tile_count,
    ) = mpp_domains.get_data_domain(
        domain_id=domain_id,
        xbegin=is_check,
        xend=ie_check,
        ybegin=js_check,
        yend=je_check,
        xsize=xsize_check,
        xmax_size=xmax_size_check,
        ysize=ysize_check,
        ymax_size=ymax_size_check,
        x_is_global=x_is_global_check,
        y_is_global=y_is_global_check,
        tile_count=tile_count,
        position=None,
        whalo=whalo,
        shalo=shalo,
    )

    assert is_check == isd[pe]
    assert ie_check == ied[pe]
    assert js_check == jsd[pe]
    assert je_check == jed[pe]
    assert xsize_check == 6
    assert ysize_check == 6
    assert xmax_size_check == 6
    assert ymax_size_check == 6

    pyfms.pyfms_end()


if __name__ == "__main__":
    test_getset_domains()
