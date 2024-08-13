function ARRAY_SORT_(n, array)

  integer(c_int), intent(in) :: n
  real(SPACE_), intent(in) :: array(n)
  integer(c_int) :: ARRAY_SORT_

  integer :: m

  m = n
  ARRAY_SORT_ = array_type(m,array=array)

end function ARRAY_SORT_