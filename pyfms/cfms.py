import ctypes
import os
import pyfms

class cFMS():

    __libpath: str = os.path.dirname(__file__) + "/../cFMS/cLIBFMS/lib/libcFMS.so"
    __lib: ctypes.CDLL = ctypes.CDLL(__libpath)

    @classmethod
    def init(cls):
        pyfms.data_override.setlib(cls.libpath, cls.lib)
        pyfms.fms.setlib(cls.libpath, cls.lib)
        pyfms.diag_manager.setlib(cls.libpath, cls.lib)
        pyfms.grid_utils.setlib(cls.libpath, cls.lib)
        pyfms.horiz_interp.setlib(cls.libpath, cls.lib)
        pyfms.mpp.setlib(cls.libpath, cls.lib)
        pyfms.mpp_domains.setlib(cls.libpath, cls.lib)
        
    @classmethod
    def changelib(cls, libpath):
        cls.__libpath = libpath
        cls.__lib = ctypes.CDLL(cls.__libpath)
        cls.init()
        
    @classmethod
    @property
    def lib(cls):
        return cls.__lib

    @classmethod
    @property
    def libpath(cls):
        return cls.__libpath
