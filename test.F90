module test
    implicit none

    public :: array_sort

    contains
      integer function array_sort(n, array_i, array_r)
        implicit none
        integer, intent(in) :: n
        integer, dimension(:), intent(in), optional :: array_i
        real, dimension(:), intent(in), optional :: array_r
        
        character(len=20) :: t
        integer :: m

        m = n

        if (present(array_i)) then
            t = 'integer'
            array_sort = array_type(0,array_i=array_i)
            print *, t
        elseif (present(array_r)) then
            t = 'real'
            array_sort = array_type(0,array_r=array_r)
            print *, t
        else
            print *, "No array"
            array_sort = m
        end if

      end function array_sort

      integer function array_type(t, array_i, array_r)
        integer, intent(in) :: t
        integer, dimension(:), intent(in), optional :: array_i
        real, dimension(:), intent(in), optional :: array_r

        integer :: t2
        t2 = t
        if (present(array_i)) then
            t2 = 1
            array_type = t2
        elseif (present(array_r)) then
            t2 = 2
            array_type = t2
        else
            print *, t
        end if

      end function array_type

end module test