#!/bin/bash

curr_dir=$PWD/cFMS
install_fms=$curr_dir/FMS/LIBFMS

netcdf_f_includes=$(nf-config --includedir)
netcdf_c_includes=$(nc-config --includedir)
netcdf_lib="`nf-config --flibs` `nc-config --libdir`"

cd $curr_dir/FMS
autoreconf -iv
export FCFLAGS="-g -fPIC -I$netcdf_f_includes" 
export CFLAGS="-fPIC -I$netcdf_c_includes"
export LDFLATS="-L$netcdf_lib"
./configure --enable-portable-kinds --prefix=$install_fms
make install

cd ..

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$install_fms/lib"
export FCFLAGS="$FCFLAGS -I$install_fms/include -fPIC"
export CFLAGS="$CFLAGS -I$install_fms/include -fPIC"
export LDFLAGS="$LDFLAGS -lFMS -L$install_fms/lib"

autoreconf -iv
./configure --with-yaml --prefix=$curr_dir/cgnuFMS
make
