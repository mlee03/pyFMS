import numpy as np
import numpy.typing as npt
from mpi4py import MPI
from pyfms import(
    pyFMS,
    pyFMS_mpp,
    pyFMS_mpp_domains, 
    Domain, 
    NestDomain,
)

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
    global_indices = np.array([0,3,0,3], dtype=np.int32)
    whalo = 2
    ehalo = 2
    shalo = 2
    nhalo = 2
    name = "test domain"

    pyfms = pyFMS(clibFMS_path="./cFMS/libcFMS/.libs/libcFMS.so")
    mpp_domains = pyFMS_mpp_domains(clibFMS=pyfms.clibFMS)
    mpp = pyFMS_mpp(clibFMS=pyfms.clibFMS)

    # set domain

    domain.global_indices = global_indices
    domain.domain_id = domain_id
    domain.whalo = whalo
    domain.ehalo = ehalo
    domain.shalo = shalo
    domain.nhalo = nhalo
    domain.name = name

    domain.layout = np.empty(shape=2, dtype=np.int32)
    mpp_domains.define_layout(global_indices=global_indices, ndivs=ndiv, layout=domain.layout)

    mpp_domains.define_domains_easy(domain)
    if not mpp_domains.domain_is_initialized(domain_id):
        mpp.pyfms_error(FATAL, "error in setting domain")

    mpp.set_current_pelist()

    """
    flipping the domain:
    pe 0: isc=2, iec=3, jsc=2, jec=3 --> pe 3
    pe 1: isc=4, iec=5, jsc=2, jec=3 --> pe 2
    pe 2: isc=2, iec=3, jsc=4, jec=5 --> pe 1
    pe 3: isc=4, iec=5, jsc=4, jec=5 --> pe 0
    """

    isc = np.array([4,2,4,2], dtype=np.int32)
    iec = np.array([5,3,5,3], dtype=np.int32)
    jsc = np.array([4,4,2,2], dtype=np.int32)
    jec = np.array([5,5,3,3], dtype=np.int32)

    """
    pe 0: isd=0, ied=5, jsd=0, jed=5 --> pe 3
    pe 1: isd=2, ied=7, jsd=0, jed=5 --> pe 2
    pe 2: isd=0, ied=5, jsd=2, jed=7 --> pe 1
    pe 3: isd=2, ied=7, jsd=2, jed=7 --> pe 0
    """

    isd = np.array([2,0,2,0], dtype=np.int32)
    ied = np.array([7,5,7,5], dtype=np.int32)
    jsd = np.array([2,2,0,0], dtype=np.int32)
    jed = np.array([7,7,5,5], dtype=np.int32)

    pe = mpp.pe()
    tile_count = 0
    x_is_global = False
    y_is_global = False

    # set compute and data domains

    xsize = 2
    ysize = 2
    mpp_domains.set_compute_domain(
        domain_id=domain_id,
        xbegin=isc+pe,
        xend=iec+pe,
        ybegin=jsc+pe,
        yend=jec+pe,
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
        xbegin=isd+pe,
        xend=ied+pe,
        ybegin=jsd+pe,
        yend=jed+pe,
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
    
    is_check, ie_check, js_check, je_check, xsize_check, xmax_size_check, ysize_check, ymax_size_check, x_is_global_check, y_is_global_check, tile_count = mpp_domains.get_compute_domain(
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

    if is_check != isc[pe]:
        mpp.pyfms_error(FATAL, "isc has not been properly set")
    if ie_check != iec[pe]:
        mpp.pyfms_error(FATAL, "iec has not been properly set")
    if js_check != jsc[pe]:
        mpp.pyfms_error(FATAL, "jsc has not been properly set")
    if je_check != jec[pe]:
        mpp.pyfms_error(FATAL, "jec has not been properly set")
    if xsize_check != 2:
        mpp.pyfms_error(FATAL, "incorrect xsixe for compute domain")
    if ysize_check != 2:
        mpp.pyfms_error(FATAL, "incorrect ysize for compute domain")
    if xmax_size_check != 2:
        mpp.pyfms_error(FATAL, "incorrect xmax_size for compute domain")
    if ymax_size_check != 2:
        mpp.pyfms_error(FATAL, "incorrect ymax_size for compute domain")
    if x_is_global_check:
        mpp.pyfms_error(FATAL, "incorrect x_is_global for compute domain")
    if y_is_global_check:
        mpp.pyfms_error(FATAL, "incorrect y_is_global for compute domain")

    is_check, ie_check, js_check, je_check, xsize_check, xmax_size_check, ysize_check, ymax_size_check, x_is_global_check, y_is_global_check, tile_count = mpp_domains.get_data_domain(
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

    if is_check != isc[pe]:
        mpp.pyfms_error(FATAL, "isc has not been properly set")
    if ie_check != iec[pe]:
        mpp.pyfms_error(FATAL, "iec has not been properly set")
    if js_check != jsc[pe]:
        mpp.pyfms_error(FATAL, "jsc has not been properly set")
    if je_check != jec[pe]:
        mpp.pyfms_error(FATAL, "jec has not been properly set")
    if xsize_check != 2:
        mpp.pyfms_error(FATAL, "incorrect xsixe for data domain")
    if ysize_check != 2:
        mpp.pyfms_error(FATAL, "incorrect ysize for data domain")
    if xmax_size_check != 2:
        mpp.pyfms_error(FATAL, "incorrect xmax_size for data domain")
    if ymax_size_check != 2:
        mpp.pyfms_error(FATAL, "incorrect ymax_size for data domain")
    if x_is_global_check:
        mpp.pyfms_error(FATAL, "incorrect x_is_global for data domain")
    if y_is_global_check:
        mpp.pyfms_error(FATAL, "incorrect y_is_global for data domain")

    pyfms.pyfms_end()

if __name__ == "__main__":
    test_getset_domains()



