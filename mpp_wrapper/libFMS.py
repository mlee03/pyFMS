#!/usr/bin/env python3

import ctypes as c
import numpy as np
import dataclasses
from mpp import MPP

@dataclasses.dataclass
class libFMS() :
    library_file : str = None
    loaded_library : c.CDLL = None

    mpp : MPP = None
    
    
    def init(self) :
        self.loaded_library = c.cdll.LoadLibrary(self.library_file)        
        self.mpp = MPP(self.loaded_library)
    
        
