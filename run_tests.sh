#!/bin/bash

pytest tests/test_build.py
if [ $? -ne 0 ] ; then
    echo "test_build error" ;
    exit 1
fi

pytest tests/test_pyfms.py
if [ $? -ne 0 ] ; then
    echo "test_pyfms error" ;
    exit 1
fi

mpirun -n 8 python -m pytest tests/py_mpp
if [ $? -ne 0 ] ; then
    echo "test_pympp error" ;
    exit 1
fi

pytest tests/horiz_interp
if [ $? -ne 0 ] ; then
    echo "test_horiz_interp error" ;
    exit 1
fi
