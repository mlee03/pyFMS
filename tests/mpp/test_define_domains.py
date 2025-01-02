import pytest

from pyfms import (
    pyFMS,
    pyFMS_mpp,
    pyFMS_mpp_domains,
)

NX = 96
NY = 96
NX_FINE = 48
NY_FINE = 48
LAYOUT_X = 2
LAYOUT_Y = 2
X_REFINE = 2
Y_REFINE = 2
COARSE_NPES = 4
FINE_NPES = 4

clibFMS_path = ""

def test_pyfms_define_domains():
    
    global_pelist = []
    ndomain = 2
    domain_id = 1
    nnest_domain = 2
    nest_domain_id = 1

    pyDomain = FMSDomain()
    nestdomain = FMSNestDomain()

    coarse_global_indices = [0, NX-1, 0, NY-1]
    coarse_npes = COARSE_NPES
    coarse_pelist = []
    coarse_tile_id = 0
    coarse_whalo = 2
    coarse_ehalo = 2
    coarse_shalo = 2
    coarse_nhalo = 2

    fine_global_indices = [0, NX_FINE-1, 0, NYFINE-1]
    fine_npes = FINE_NPES
    fine_pelist = []
    fine_tile_id = 1
    fine_whalo = 2
    fine_ehalo = 2
    fine_shalo = 2
    fine_nhalo = 2

    fms = pyFMS(
        clibFMS_path=clibFMS_path,
        alt_input_nml_path=None,
        localcomm = None,
        ndomain = ndomain,
        nnest_domain = nnest_domain,
    )

    mpp = pyFMS_mpp(clibFMS=fms.clibFMS)

    # get global pelist
    npes = mpp.pyfms_npes()[i]
    global_pelist = []
    mpp.pyfms_set_current_pelist(npes)
    mpp.pyfms_get_current_pelist(global_pelist)

    # set coarse domain as tile=0
    for i in range(coarse_npes):
        coarse_pelist.append(global_pelist[i])

    name_coarse = "test_coarse_pelist"
    fms.pyfms_set_pelist_npes(coarse_npes)
    mpp.pyfms_declare_pelist(pelist=coarse_pelist, name_c=name_coarse)
