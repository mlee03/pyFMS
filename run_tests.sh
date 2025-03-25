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

mpirun -n 8 python -m pytest tests/py_mpp/test_define_domains.py
if [ $? -ne 0 ] ; then
    echo "test_pympp/test_define_domains error" ;
    exit 1
fi

mpirun -n 4 python -m pytest tests/py_mpp/test_getset_domains.py
if [ $? -ne 0 ] ; then
    echo "test_pympp/test_getset_domains error" ;
    exit 1
fi

pytest tests/horiz_interp
if [ $? -ne 0 ] ; then
    echo "test_horiz_interp error" ;
    exit 1
fi

mpirun -n 6 python -m pytest tests/py_data_override
if [ $? -ne 0 ] ; then
    echo "test_data_override error" ;
    exit 1
fi
