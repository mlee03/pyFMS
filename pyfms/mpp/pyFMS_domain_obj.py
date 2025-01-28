from dataclasses import dataclass
from typing import List, Optional, Tuple
import numpy as np
from numpy.typing import NDArray

@dataclass
class Domain:
    global_indices: Optional[List[int]] = None
    layout: Optional[Tuple[int, ...]] = None
    domain_id: Optional[int] = None
    pelist: Optional[List[int]] = None
    xflags: Optional[int] = None
    yflags: Optional[int] = None
    xextent: Optional[List] = None
    yextent: Optional[List] = None
    maskmap: Optional[NDArray[np.int32]] = None
