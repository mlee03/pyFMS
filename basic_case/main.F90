program main

    ! use test

    ! use iso_c_binding

    ! integer :: n
    ! integer :: k
    ! real(c_float), dimension(2) :: array_rt
    ! n = 2

    ! array_it = (/3,4/)
    ! array_rt = (/3.0,4.0/)

    ! k = array_sort(n, array_rt)

    use test3_mod

    integer :: k
    type(tt) :: test_type

    k = 2

    test_type%begin = k
    test_type%end = k

    print *, test_type%begin

end program main


    