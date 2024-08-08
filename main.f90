program main

    use test

    integer :: n
    integer :: k
    integer, dimension(2) :: array_it
    real, dimension(2) :: array_rt
    n = 2

    array_it = (/3,4/)
    array_rt = (/3.0,4.0/)

    k = array_sort(n=n, array_i=array_it)

    print *, k

end program main


    