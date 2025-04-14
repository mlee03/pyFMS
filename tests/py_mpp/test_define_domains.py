import os

import numpy as np
import pytest

import pyfms


@pytest.mark.create
def test_create_input_nml():
    inputnml = open("input.nml", "w")
    inputnml.close()
    os.path.isfile("input.nml")


@pytest.mark.parallel
def test_define_domains():

    ndomain = 2
    nnest_domain = 2
    domain_id = 0
    nest_domain_id = 0

    nx = 96
    ny = 96    
    coarse_global_indices = [0, nx - 1, 0, ny - 1]
    coarse_npes = 4
    coarse_pelist = list(range(coarse_npes))    
    coarse_tile_id = 0

    nx_fine = 48
    ny_fine = 48
    fine_global_indices = [0, nx_fine - 1, 0, ny_fine - 1]
    fine_npes = 4
    fine_pelist = list(range(fine_npes))
    fine_tile_id = 1
    
    pyfms.fms.init(ndomain=ndomain, nnest_domain=nnest_domain)

    """get global pelist"""

    pyfms.mpp.set_pelist_npes(npes_in=pyfms.mpp.npes())
    global_pelist = pyfms.mpp.get_current_pelist()

    """set coarse domain as tile=0"""

    coarse_pelist = global_pelist[:coarse_npes]
    pyfms.mpp.set_pelist_npes(npes_in=coarse_npes)
    pyfms.mpp.declare_pelist(pelist=coarse_pelist, name="test coarse pelist")

    if pyfms.mpp.pe() in coarse_pelist:
        pyfms.mpp.set_pelist_npes(coarse_npes)
        pyfms.mpp.set_current_pelist(coarse_pelist)
        
        layout = pyfms.mpp_domains.define_layout(
            global_indices=coarse_global_indices,
            ndivs=coarse_npes,
        )
        
        pyfms.mpp_domains.define_domains(
            global_indices=coarse_global_indices,
            layout=layout,
            domain_id=domain_id,
            pelist=coarse_pelist,
            xflags=pyfms.mpp_domains.WEST,
            yflags=pyfms.mpp_domains.SOUTH,
            xextent=[nx/2]*4,
            yextent=[ny/2]*4,
            maskmap=None, #[[True,True],[True,True]],
            name="test coarse domain",
            symmetry=False,
            whalo=2,
            ehalo=2,
            shalo=2,
            nhalo=2,
            is_mosaic=False,
            tile_id=coarse_tile_id,
        )

    pyfms.mpp.set_current_pelist()    

    """set fine domain as tile=1"""

    fine_pelist = global_pelist[coarse_npes:coarse_npes+fine_npes]
    pyfms.mpp.set_pelist_npes(fine_npes)
    pyfms.mpp.declare_pelist(pelist=fine_pelist, name="test fine pelist")

    if pyfms.mpp.pe() in fine_pelist:
        pyfms.mpp.set_pelist_npes(fine_npes)
        pyfms.mpp.set_current_pelist(pelist=fine_pelist)

        layout = pyfms.mpp_domains.define_layout(
            global_indices=fine_global_indices,
            ndivs=fine_npes,
        )

        pyfms.mpp_domains.define_domains(
            global_indices=fine_global_indices,
            layout=layout,
            domain_id=domain_id,
            pelist=fine_pelist,
            name="test fine domain",
            symmetry=False,
            whalo=2,
            ehalo=2,
            shalo=2,
            nhalo=2,
            is_mosaic=False,
            tile_id=fine_tile_id,
        )
    assert pyfms.mpp_domains.domain_is_initialized(domain_id)        

    pyfms.mpp.set_current_pelist()

    """set nest domain"""
    
    pyfms.mpp_domains.define_nest_domains(
        num_nest=1,
        ntiles=2,
        nest_level=[1],
        tile_fine=[fine_tile_id],
        tile_coarse=[coarse_tile_id],
        istart_coarse=[24],
        icount_coarse=[24],
        jstart_coarse=[24],
        jcount_coarse=[24],
        npes_nest_tile=[coarse_npes, fine_npes],
        x_refine=[2],
        y_refine=[2],
        nest_domain_id=nest_domain_id,
        domain_id=domain_id,
        name="test nest domain",
    )

    pyfms.mpp.set_current_pelist()
    
    pyfms.fms.end()


@pytest.mark.remove
def test_remove_input_nml():
    os.remove("input.nml")
    assert not os.path.isfile("input.nml")


if __name__ == "__main__":
    test_define_domains()
