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
    xhalo: Optional[int] = None
    yhalo: Optional[int] = None
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

    def null(self):
        self.global_indices = None
        self.layout = None
        self.domain_id = None
        self.pelist = None
        self.xflags = None
        self.yflags = None
        self.xhalo = None
        self.yhalo = None
        self.xextent = None
        self.yextent = None
        self.maskmap = None
        self.name = None
        self.symmetry = None
        self.memory_size = None
        self.whalo = None
        self.ehalo = None
        self.shalo = None
        self.nhalo = None
        self.is_mosaic = None
        self.tile_count = None
        self.tile_id = None
        self.complete = None
        self.x_cyclic_offset = None
        self.y_cyclic_offset = None


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

    def null(self):
        self.num_nest = None
        self.ntiles = None
        self.nest_level = None
        self.tile_fine = None
        self.tile_coarse = None
        self.istart_coarse = None
        self.icount_coarse = None
        self.jstart_coarse = None
        self.jcount_coarse = None
        self.npes_nest_tile = None
        self.x_refine = None
        self.y_refine = None
        self.nest_domain_id = None
        self.domain_id = None
        self.extra_halo = None
        self.name = None
