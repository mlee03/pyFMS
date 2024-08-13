import ctypes as ct
import numpy as np

def setarg_i4(arg) :
    if arg == None :
        arg_t = ct.POINTER(ct.c_int)
    else :
        arg = [arg] if len(arg) == 0 else arg
        arg = np.ctypeslib.as_array( np.array(arg, dtype=ct.c_int) )
        arg_t = np.ctypeslib.ndpointer( dtype=ct.c_int, shape=np.shape(arg), flags='FORTRAN')
    return arg, arg_t

def setarg_r4(arg) :
    if arg == None :
        arg_t = ct.POINTER(ct.c_float)
    else :
        arg = [arg] if len(arg) == 0 else arg
        arg = np.ctypeslib.as_array( np.array(arg, dtype=ct.c_float) )
        arg_t = np.ctypeslib.ndpointer( dtype=ct.c_float, shape=np.shape(arg), flags='FORTRAN')
    return arg, arg_t

def setarg_r8(arg) :
    if arg == None :
        arg_t = ct.POINTER(ct.c_double)
    else :
        arg = [arg] if len(arg) == 0 else arg
        arg = np.ctypeslib.as_array( np.array(arg, dtype=ct.c_double) )
        arg_t = np.ctypeslib.ndpointer( dtype=ct.c_double, shape=np.shape(arg), flags='FORTRAN')
    return arg, arg_t

def setarg_c(arg) :
    if arg == None :
        arg_t = ct.POINTER(c.c_char_p)
    else :
        arg = ct.byref( c.c_char_p( arg.encode('ascii') ) )
        arg_t = ct.POINTER(ct.c_char_p)
    return arg, arg_t

def setarg_bool(arg) :
    if arg == None :
        arg_t = ct.POINTER(ct.c_bool)
    else :
        arg = [arg] if len(arg) == 0 else arg
        arg = np.ctypeslib.as_array( np.array(arg, dtype=ct.c_bool) )
        arg_t = np.ctypeslib.ndpointer( dtype=ct.c_bool, shape=np.shape(arg), flags='FORTRAN')
    return arg, arg_t


def setarg_size(arg, ndim) :
    if arg == None :
        argsize = [ ct.byref(ct.c_int(1)) for i in range(ndim) ]
        argsize_t = [ ct.POINTER(ct.c_int) for i in range(ndim) ]
    else :
        argsize = [ ct.byref(ct.c_int(isize)) for isize in np.shape(arg) ]
        argsize_t = [ ct.POINTER(ct.c_int) for i in range(ndim) ]
    return argsize, argsize_t