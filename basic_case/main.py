import ctypes as ct
import numpy as np
import dataclasses

lib_file = './test.so'

lib = ct.cdll.LoadLibrary(lib_file)

def setarg_r4(arg) :
    if np.all(arg) == None :
        arg_t = ct.POINTER(ct.c_float)
    else :
        arg = [arg] if len(arg) == 0 else arg
        arg = np.ctypeslib.as_array( np.array(arg, dtype=ct.c_float) )
        arg_t = np.ctypeslib.ndpointer( dtype=ct.c_float, shape=np.shape(arg), flags='FORTRAN')
    return arg, arg_t

def setarg_r8(arg) :
    if np.all(arg) == None :
        arg_t = ct.POINTER(ct.c_double)
    else :
        arg = [arg] if len(arg) == 0 else arg
        arg = np.ctypeslib.as_array( np.array(arg, dtype=ct.c_double) )
        arg_t = np.ctypeslib.ndpointer( dtype=ct.c_double, shape=np.shape(arg), flags='FORTRAN')
    return arg, arg_t

def setarg_size(arg, ndim) :
    if np.all(arg) == None :
        argsize = [ ct.byref(ct.c_int(1)) for i in range(ndim) ]
        argsize_t = [ ct.POINTER(ct.c_int) for i in range(ndim) ]
    else :
        argsize = [ ct.byref(ct.c_int(isize)) for isize in np.shape(arg) ]
        argsize_t = [ ct.POINTER(ct.c_int) for i in range(ndim) ]
    return argsize, argsize_t

def array_sorter(array):

    _array_sort_r4 = getattr(lib, "__test_MOD_array_sort_r4")
    _array_sort_r8 = getattr(lib, "__test_MOD_array_sort_r8")

    if (np.all(array.dtype) == ct.c_float):
        array, array_t = setarg_r4(array)
        n, n_t = setarg_size(array,1)
        _array_sort_r4.argtypes = [ *n_t, array_t ]
        _array_sort_r4.restype = ct.c_int
        return _array_sort_r4(*n, array)
    # elif (np.all(array.dtype) == ct.c_double):
    #     array, array_t = setarg_r8(array)
    #     n, n_t = setarg_size(array,1)
    #     _array_sort_r8.argtypes = [ *n_t, array_t ]
    #     _array_sort_r8.restype = ct.c_int
    #     return _array_sort_r8(*n, array=array)
    # else:
    #     print("array of unknown data type")
    #     return 0


arr = np.array([3,4],dtype=ct.c_float)

print(arr)

out = array_sorter(arr)
print(out)

