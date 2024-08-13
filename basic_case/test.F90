module test

use test2

use iso_c_binding

public :: array_sort

interface array_sort
  module procedure array_sort_r4, array_sort_r8
end interface array_sort

contains

#include "test.fh"

end module test