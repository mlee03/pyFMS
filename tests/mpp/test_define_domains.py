import ctypes as ct
import os

import numpy as np
import numpy.typing as npt
from mpi4py import MPI

from pyfms import Domain, NestDomain, pyFMS, pyFMS_mpp, pyFMS_mpp_domains


def any(n: int, array: npt.NDArray, value: int) -> bool:
    for i in range(n):
        if value == array[i]:
            return True
    return False


def test_define_domains():
    fcomm = MPI.COMM_WORLD.py2f()

    NX = 96
    NY = 96
    NX_FINE = 48
    NY_FINE = 48
    X_REFINE = 2
    Y_REFINE = 2
    COARSE_NPES = 4
    FINE_NPES = 4

    ndomain = 2
    nnest_domain = 2
    domain_id = 1
    nest_domain_id = 1

    domain = Domain()
    nest_domain = NestDomain()

    coarse_global_indices = np.array([0, NX - 1, 0, NY - 1], dtype=np.int32)
    coarse_npes = COARSE_NPES
    coarse_pelist = np.empty(shape=COARSE_NPES, dtype=np.int32, order="F")
    coarse_tile_id = 0
    coarse_whalo = 2
    coarse_ehalo = 2
    coarse_shalo = 2
    coarse_nhalo = 2
    coarse_xflags = 3
    coarse_yflags = 2
    is_mosaic = False

    fine_global_indices = np.array([0, NX_FINE - 1, 0, NY_FINE - 1], dtype=np.int32)
    fine_npes = FINE_NPES
    fine_pelist = np.empty(shape=FINE_NPES, dtype=np.int32, order="F")
    fine_tile_id = 1
    fine_whalo = 2
    fine_ehalo = 2
    fine_shalo = 2
    fine_nhalo = 2

    # pyfms = pyFMS(clibFMS_path="./cFMS/libcFMS/.libs/libcFMS.so", ndomain=ndomain, nnest_domain=nnest_domain)
    # pyfms = pyFMS(clibFMS_path="./cFMS/libcFMS/.libs/libcFMS.so")
    pyfms = pyFMS(
        localcomm=fcomm,
        clibFMS_path="./cFMS/libcFMS/.libs/libcFMS.so",
        alt_input_nml_path="input.nml",
        ndomain=ndomain,
        nnest_domain=nnest_domain,
    )
    mpp = pyFMS_mpp(clibFMS=pyfms.clibFMS)

    assert isinstance(pyfms, pyFMS)

    # get global pelist

    npes = mpp.npes()
    global_pelist = np.empty(shape=npes, dtype=np.int32, order="F")
    pyfms.set_pelist_npes(npes_in=npes)
    commID, name_current = mpp.get_current_pelist(pelist=global_pelist)

    # set coarse domain as tile=0

    for i in range(coarse_npes):
        coarse_pelist[i] = global_pelist[i]
    name_coarse = "test coarse pelist"
    pyfms.set_pelist_npes(npes_in=coarse_npes)
    commID = mpp.declare_pelist(pelist=coarse_pelist, name=name_coarse)

    if any(coarse_npes, coarse_pelist, mpp.pe()):
        pyfms.set_pelist_npes(coarse_npes)
        # mpp.set_current_pelist(pelist=coarse_pelist)
        # name = "test coarse domain"
        # domain.maskmap = np.full(shape=(2,4), fill_value=True, dtype=np.bool_)

        # xextent = np.zeros(shape=2, dtype=np.int32)
        # yextent = np.zeros(shape=2, dtype=np.int32)
        # is_mosaic = False

        # domain.domain_id = domain_id
        # domain.name = name
        # domain.pelist = coarse_pelist
        # domain.global_indices = coarse_global_indices
        # domain.whalo = coarse_whalo
        # domain.ehalo = coarse_ehalo
        # domain.shalo = coarse_shalo
        # domain.nhalo = coarse_nhalo
        # domain.tile_id = coarse_tile_id
        # domain.xflags = coarse_xflags
        # domain.yflags = coarse_yflags
        # domain.xextent = xextent
        # domain.yextent = yextent
        # domain.is_mosaic = is_mosaic
        # domain.layout = np.empty(shape=2, dtype=np.int32)
        # ndivs = coarse_npes

        # mpp_domains = pyFMS_mpp_domains(clibFMS=pyfms.clibFMS)

        # mpp_domains.define_layout(global_indices=coarse_global_indices, ndivs=ndivs, layout=domain.layout)

        # #TODO: Need to implement both
        # mpp_domains.define_domains_easy(domain)
        # domain.null()

        # mpp.set_current_pelist()

    # set fine domain as tile=1

    # name_fine = "test fine pelist"
    # for i in range(fine_npes):
    #     fine_pelist[i] = global_pelist[COARSE_NPES+i]
    # pyfms.set_pelist_npes(fine_npes)
    # mpp.declare_pelist(pelist=fine_pelist, name=name_fine)

    # if any(FINE_NPES, fine_pelist, mpp.pe()):
    #     pyfms.set_pelist_npes(fine_npes)
    #     mpp.set_current_pelist(pelist=fine_pelist)

    #     name = "test fine domain"
    #     domain.name = name
    #     domain.global_indices = fine_global_indices
    #     domain.tile_id = fine_tile_id
    #     domain.whalo = fine_whalo
    #     domain.ehalo = fine_ehalo
    #     domain.shalo = fine_shalo
    #     domain.nhalo = fine_nhalo
    #     domain.domain_id = domain_id
    #     domain.layout = np.empty(shape=2, dtype=np.int32)
    #     ndivs = FINE_NPES

    #     mpp_domains.define_layout(global_indices=fine_global_indices, ndivs=ndivs, layout=domain.layout)

    #     # TODO: Need to implement both
    #     mpp_domains.define_domains_easy(domain)
    #     domain.null()

    # mpp.set_current_pelist()

    # if not mpp_domains.domain_is_initialized:
    #     mpp.pyfms_error(FATAL, "domain is not initialized")

    # set nest domain

    # nest_domain.name = "test nest domain"
    # nest_domain.num_nest = 1
    # nest_domain.ntiles = 2
    # nest_domain.nest_level = 2
    # nest_domain.istart_coarse = 24
    # nest_domain.icount_coarse = 24
    # nest_domain.jstart_coarse = 24
    # nest_domain.jcount_coarse = 24
    # nest_domain.npes_nest_tile = np.array([COARSE_NPES, FINE_NPES], dtype=np.int32)
    # nest_domain.x_refine = X_REFINE
    # nest_domain.y_refine = Y_REFINE
    # nest_domain.tile_fine = fine_tile_id
    # nest_domain.tile_coarse = coarse_tile_id
    # nest_domain.nest_domain_id = nest_domain_id
    # nest_domain.domain_id = domain_id

    # mpp_domains.define_nest_domains_easy(nest_domain)
    # nest_domain.null()

    # mpp.set_current_pelist()
    pyfms.pyfms_end()


if __name__ == "__main__":
    test_define_domains()
