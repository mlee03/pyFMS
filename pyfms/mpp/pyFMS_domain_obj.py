from dataclasses import dataclass
from typing import Optional, Tuple

import numpy as np
from numpy.typing import NDArray


@dataclass
class Domain:
    global_indices: Optional[NDArray[np.int32]] = None
    layout: Optional[Tuple[int, ...]] = None
    domain_id: Optional[int] = None
    pelist: Optional[NDArray[np.int32]] = None
    xflags: Optional[int] = None
    yflags: Optional[int] = None
    xextent: Optional[NDArray[np.int32]] = None
    yextent: Optional[NDArray[np.int32]] = None
    maskmap: Optional[NDArray[np.bool_]] = None
    name: Optional[str] = None
    symmetry: Optional[bool] = None
    memory_size: Optional[NDArray[np.int32]] = None
    whalo: Optional[int] = None
    ehalo: Optional[int] = None
    shalo: Optional[int] = None
    nhalo: Optional[int] = None
    is_mosaic: Optional[bool] = None
    tile_count: Optional[int] = None
    tile_id: Optional[int] = None
    complete: Optional[bool] = None
    x_cyclic_offset: Optional[int] = None
    y_cyclic_offset: Optional[int] = None


@dataclass
class NestDomain:
    num_nest: Optional[int] = None
    ntiles: Optional[int] = None
    nest_level: Optional[NDArray[np.int32]] = None
    tile_fine: Optional[NDArray[np.int32]] = None
    tile_coarse: Optional[NDArray[np.int32]] = None
    istart_coarse: Optional[NDArray[np.int32]] = None
    icount_coarse: Optional[NDArray[np.int32]] = None
    jstart_coarse: Optional[NDArray[np.int32]] = None
    jcount_coarse: Optional[NDArray[np.int32]] = None
    npes_nest_tile: Optional[NDArray[np.int32]] = None
    x_refine: Optional[NDArray[np.int32]] = None
    y_refine: Optional[NDArray[np.int32]] = None
    nest_domain_id: Optional[int] = None
    domain_id: Optional[int] = None
    extra_halo: Optional[int] = None
    name: Optional[str] = None
