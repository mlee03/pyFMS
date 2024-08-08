#!/usr/bin/env python3

import numpy
from libFMS import libFMS
import ctypes

library_file='./pyFMS/pyfms.so'

libfms = libFMS(library_file = library_file)
libfms.init()
libfms.mpp.init(alt_input_nml_path='./input/input.nml')
libfms.mpp.define_domains2d([1,1,1,1],[1,1], name='test_domain')

print( libfms.mpp.get_layout2d() )
