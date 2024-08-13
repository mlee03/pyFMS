module test2
    implicit none

    public :: array_type

    contains

      integer function array_type(t, array)
        integer, intent(in) :: t
        class(*), dimension(:), intent(in) :: array
        ! integer, dimension(:), intent(in), optional :: array_i
        ! real, dimension(:), intent(in), optional :: array_r

        integer :: t2
        ! if (present(array_i)) then
        !   t2 = 1
        !   array_type = t2
        ! elseif (present(array_r)) then
        !   t2 = 2
        !   array_type = t2
        ! else
        !   print *, t
        ! end if
        array_type = t2

      end function array_type
      
end module test2