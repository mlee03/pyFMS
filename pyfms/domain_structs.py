import dataclasses
import numpy as np
import numpy.typing as npt
from typing import List

@dataclasses.dataclass
class pyDomainStruct:
    global_indices: List[int] = None
    layout: List[int] = None
    domain_id: int = None
    pelist: List[int] = None
    xflags: int = None
    yflags: int = None
    xhalo: int = None
    yhalo: int = None
    xextent: int = None
    yextent: int = None
    maskmap: npt.NDArray[int] = None
    name: str = None
    symmetry: bool = None
    memory_size: List[int] = None
    whalo: int = None
    ehalo: int = None
    shalo: int = None
    nhalo: int = None
    is_mosaic: bool = None
    tile_count: int = None
    tile_id: int = None
    complete: bool = None
    x_cyclic_offset: int = None
    y_cyclic_offset: int = None

@dataclasses.dataclass
class pyNestDomainStruct:
    num_nest: int = None
    ntiles: int = None
    nest_level: int = None
    tile_fine: int = None
    tile_coarse: int = None
    istart_coarse: int = None
    icount_coarse: int = None
    jstart_coarse: int = None
    jcount_coarse: int = None
    npes_nest_tile: int = None
    x_refine: int = None
    y_refine: int = None
    nest_domain_id: int = None
    domain_id: int = None
    extra_halo: int = None
    name: str = None
