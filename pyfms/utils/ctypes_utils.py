import ctypes
import numpy as np
import numpy.typing as npt
from typing import Union

ctypelist = Union[type(ctypes.c_int),
                  type(ctypes.c_float),
                  type(ctypes.c_double),
                  type(ctypes.c_bool)]

nptypelist = Union[np.int32,
                   np.int64,
                   np.float32,
                   np.float64,
                   np.bool]

def setNone(arglist) -> None:
    arglist.append(None)
    return None

def setargs(arg: ctypelist|None,
            ctype: ctypelist,
            arglist: list) -> ctypelist|None:

    if arg is None: return setNone(arglist)
    
    arg_c = ctype(arg)
    arglist.append(arg_c)
    return arg_c


def setargs_str(arg: str|None,
                arglist: list) -> type(ctypes.c_char_p)|None:
    
    if arg is None: return setNone(arglist)

    arg_c = ctypes.c_char_p(arg.encode("utf-8"))
    arglist.append(arg_c)
    return arg_c

def setargs_arr(arg: npt.ArrayLike|None,
                nptype: nptypelist,
                arglist: list) -> npt.ArrayLike|None:

    if arg is None: return setNone(arglist)

    arglist.append(arg)
    return arg
        

def setargs_list(arg: list|None,
                 nptype: nptypelist,
                 arglist: list) -> npt.ArrayLike|None:
    
    if arg is None: return setNone(arglist)

    arg_c = np.array(arg, dtype=nptype)
    arglist.append(arg_c)
    return arg_c
        
    
def arraytype(arg: npt.ArrayLike|None,
              nptype: nptypelist) -> type(ctypes.POINTER)|type(np.ctypeslib.ndpointer):

    if arg is None: 
        return ctypes.POINTER(np.ctypeslib.as_ctypes_type(nptype))
                                          
    return np.ctypeslib.ndpointer(dtype=nptype,
                                  ndim=arg.ndim,
                                  shape=arg.shape,
                                  flags="C_CONTIGUOUS")
