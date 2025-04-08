import ctypes
import os
from pyfms import pyDataOverride
from pyfms import pyFMS

class cFMS():

    __cfms_path: str = os.path.dirname(__file__) + "/../cFMS/cLIBFMS/lib/libcFMS.so"
    __cfms: ctypes.CDLL = ctypes.CDLL(__cfms_path)
    __initialized = False

    @classmethod
    def init(cls):
        if cls.__initialized: pass
        
        pyDataOverride.setlib(cls.__cfms_path, cls.__cfms)
        pyFMS.setlib(cls.__cfms_path, cls.__cfms)
        cls.__initialized = True    
        
    @classmethod
    def changelib(cls, cfms_path):
        cls.__cfms_path = cfms_path
        cls.__cfms = ctypes.CDLL(cls.__cfms_path)
        pyDataOverride.setlib(cls.__cfms_path, cls.__cfms)
        pyFMS.setlib(cls.__cfms_path, cls.__cfms)
        cls.__initialized = True

    def is_initialized(cls):
        return cls.__initialized
        
    @classmethod
    def getlib(cls):
        return cls.__cfms_path, cls.__cfms
