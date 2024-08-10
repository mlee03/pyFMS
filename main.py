import ctypes as ct
import numpy as np
import dataclasses

lib_file = './test.so'

lib = ct.cdll.LoadLibrary(lib_file)

def setarg_i4(arg) :
    if np.all(arg) == None :
        arg_t = ct.POINTER(ct.c_int)
    else :
        arg = [arg] if len(arg) == 0 else arg
        arg = np.ctypeslib.as_array( np.array(arg, dtype=np.int32) )
        arg_t = np.ctypeslib.ndpointer( dtype=ct.c_int, shape=np.shape(arg), flags='FORTRAN')
    return arg, arg_t

def setarg_i8(arg) :
    if np.all(arg) == None :
        arg_t = ct.POINTER(ct.c_int)
    else :
        arg = [arg] if len(arg) == 0 else arg
        arg = np.ctypeslib.as_array( np.array(arg, dtype=np.int64) )
        arg_t = np.ctypeslib.ndpointer( dtype=ct.c_int, shape=np.shape(arg), flags='FORTRAN')
    return arg, arg_t

def setarg_r4(arg) :
    if np.all(arg) == None :
        arg_t = ct.POINTER(ct.c_float32)
    else :
        arg = [arg] if len(arg) == 0 else arg
        arg = np.ctypeslib.as_array( np.array(arg, dtype=np.float32) )
        arg_t = np.ctypeslib.ndpointer( dtype=ct.c_float, shape=np.shape(arg), flags='FORTRAN')
    return arg, arg_t

def setarg_r8(arg) :
    if np.all(arg) == None :
        arg_t = ct.POINTER(ct.c_double)
    else :
        arg = [arg] if len(arg) == 0 else arg
        arg = np.ctypeslib.as_array( np.array(arg, dtype=np.float64) )
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

    _array_sort = getattr(lib, "__test_MOD_array_sort")

    if (np.all(array.dtype) == 'int32'):
        array, array_t = setarg_i4(array)
        n, n_t = setarg_size(array,1)
        _array_sort.argtypes = [ *n_t, array_t ]
        _array_sort.restype = ct.c_int
        return _array_sort(*n, array_i=array)
    elif (np.all(array.dtype) == 'int64'):
        array, array_t = setarg_i8(array)
        n, n_t = setarg_size(array,1)
        _array_sort.argtypes = [ *n_t, array_t ]
        _array_sort.restype = ct.c_int
        return _array_sort(*n, array_i=array)
    elif (np.all(array.dtype) == 'float32'):
        array, array_t = setarg_r4(array)
        n, n_t = setarg_size(array,1)
        _array_sort.argtypes = [ *n_t, array_t ]
        _array_sort.restype = ct.c_int
        return _array_sort(*n, array_r=array)
    elif (np.all(array.dtype) == 'float64'):
        array, array_t = setarg_r8(array)
        n, n_t = setarg_size(array,1)
        _array_sort.argtypes = [ *n_t, array_t ]
        _array_sort.restype = ct.c_int
        return _array_sort(*n, array_r=array)
    else:
        print("array of unknown data type")
        return 0


arr = np.array([3,4],dtype='int32')

out = array_sorter(arr)
print(out)

