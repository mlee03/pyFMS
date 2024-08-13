#!/usr/bin/env python3                                                                                                           

import ctypes as c
import numpy as np
import dataclasses


def setargs_Cint32(arg) :
    if arg == None :
        arg_t = c.POINTER(c.c_int)
    else :
        arg = [arg] if len(arg) == 0 else arg
        arg = np.ctypeslib.as_array( np.array(arg, dtype=np.int32) )
        arg_t = np.ctypeslib.ndpointer( dtype=c.c_int, shape=np.shape(arg), flags='FORTRAN')
    return arg, arg_t


def setargs_Cfloat(arg) :
    if arg == None :
        arg_t = c.POINTER(c.c_float32)
    else :
        arg = [arg] if len(arg) == 0 else arg
        arg = np.ctypeslib.as_array( np.array(arg, dtype=np.float32) )
        arg_t = np.ctypeslib.ndpointer( dtype=c.c_float, shape=np.shape(arg), flags='FORTRAN')
    return arg, arg_t


def setargs_Cdouble(arg) :
    if arg == None :
        arg_t = c.POINTER(c.c_double)
    else :
        arg = [arg] if len(arg) == 0 else arg
        arg = np.ctypeslib.as_array( np.array(arg, dtype=np.floag64) )
        arg_t = np.ctypeslib.ndpointer( dtype=c.c_double, shape=np.shape(arg), flags='FORTRAN')
    return arg, arg_t

def setargs_Cchar(arg) :
    if arg == None :
        arg_t = c.POINTER(c.c_char_p)
    else :
        arg = c.byref( c.c_char_p( arg.encode('ascii') ) )
        arg_t = c.POINTER(c.c_char_p)
    return arg, arg_t


def setargs_Cbool(arg) :
    if arg == None :
        arg_t = c.POINTER(c.c_bool)
    else :
        arg = [arg] if len(arg) == 0 else arg
        arg = np.ctypeslib.as_array( np.array(arg, dtype=np.bool) )
        arg_t = np.ctypeslib.ndpointer( dtype=c.c_bool, shape=np.shape(arg), flags='FORTRAN')
    return arg, arg_t


def setargs_size(arg, ndim) :
    if arg == None :
        argsize = [ c.byref(c.c_int(1)) for i in range(ndim) ]
        argsize_t = [ c.POINTER(c.c_int) for i in range(ndim) ]
    else :
        argsize = [ c.byref(c.c_int(isize)) for isize in np.shape(arg) ]
        argsize_t = [ c.POINTER(c.c_int) for i in range(ndim) ]
    return argsize, argsize_t
