module py_mpp_mod

  use mpp_domains_mod
  use mpp_mod
  use fms_string_utils_mod
  use iso_c_binding

  implicit none

  public :: test
  public :: py_mpp_init
  public :: py_get_domain
  public :: py_mpp_define_layout2d
  public :: py_mpp_define_domains2D
  public :: py_mpp_get_layout2D
  public :: py_mpp_get_domain_name
  
  type(domain2D), public :: Domain

contains

  !> retrieve Domain
  function py_get_domain()
    type(domain2D) :: py_get_domain
    py_get_domain = Domain
  end function py_get_domain


  subroutine py_mpp_init(flags, localcomm, test_level, alt_input_nml_path_ptr)

    implicit none
    integer, intent(in), optional :: flags
    integer, intent(in), optional :: localcomm
    integer, intent(in), optional :: test_level
    type(c_ptr), intent(in), optional :: alt_input_nml_path_ptr

    character(100) :: alt_input_nml_path = 'input.nml'
    
    if(present(alt_input_nml_path_ptr)) alt_input_nml_path = fms_c2f_string(alt_input_nml_path_ptr)
    call mpp_init( flags=flags, localcomm=localcomm, test_level=test_level, alt_input_nml_path=alt_input_nml_path)
    
  end subroutine py_mpp_init
  
  !> call mpp_define_layout2d
  subroutine py_mpp_define_layout2d(global_indices, ndivs, layout)

    !!DIR$ ATTRIBUTES C ALIAS:'py_define_layout2d'::py_define_layout2d
    
    implicit none
    integer, intent(in), dimension(4) :: global_indices
    integer, intent(in) :: ndivs
    integer, intent(out), dimension(2) :: layout

    call mpp_define_layout(global_indices, ndivs, layout)

  end subroutine py_mpp_define_layout2d 

  !> call mpp_define_domain
  subroutine py_mpp_define_domains2D(global_indices, layout, &
       n_pelist, n_xextent, n_yextent, n1_maskmap, n2_maskmap, n_memory_size, &
       pelist, xflags, yflags, xhalo, yhalo, xextent, yextent, maskmap, name_ptr, symmetry, &
       memory_size, whalo, ehalo, shalo, nhalo, is_mosaic, tile_count, tile_id, &
       complete, x_cyclic_offset, y_cyclic_offset)

    implicit none

    integer, intent(in) :: global_indices(4) 
    integer, intent(in) :: layout(2)
    integer, intent(in) :: n_pelist
    integer, intent(in) :: n_xextent, n_yextent
    integer, intent(in) :: n1_maskmap, n2_maskmap
    integer, intent(in) :: n_memory_size    
    integer, intent(in), optional :: pelist(n_pelist) 
    integer, intent(in), optional :: xflags, yflags
    integer, intent(in), optional :: xhalo, yhalo
    integer, intent(in), optional :: xextent(n_xextent), yextent(n_yextent)
    logical, intent(in), optional :: maskmap(n1_maskmap,n2_maskmap)
    type(c_ptr), intent(in), optional :: name_ptr
    logical, intent(in), optional :: symmetry
    logical, intent(in), optional :: is_mosaic
    integer, intent(in), optional :: memory_size(n_memory_size)
    integer, intent(in), optional :: whalo, ehalo, shalo, nhalo
    integer, intent(in), optional :: tile_count
    integer, intent(in), optional :: tile_id
    logical, intent(in), optional :: complete
    integer, intent(in), optional :: x_cyclic_offset
    integer, intent(in), optional :: y_cyclic_offset

    character(len=20) :: name
    
    call mpp_init()
    call mpp_domains_init()

    if(present(name_ptr)) name = fms_c2f_string(name_ptr)
    
    call mpp_define_domains( global_indices, layout, Domain, pelist, xflags, yflags,    &
         xhalo, yhalo, xextent, yextent, maskmap, name, symmetry,  memory_size,         &
         whalo, ehalo, shalo, nhalo, is_mosaic, tile_count, tile_id, complete, x_cyclic_offset, y_cyclic_offset )

  end subroutine py_mpp_define_domains2D

  !> get layout
  subroutine py_mpp_get_layout2D(layout) 

    integer, intent(inout) :: layout(2)

    call mpp_get_layout(Domain, layout)

  end subroutine py_mpp_get_layout2D

  !> get domain name
  subroutine py_mpp_get_domain_name(name_ptr)

    implicit none
    type(c_ptr), intent(inout) :: name_ptr
    character(100) :: name

    name = fms_c2f_string(name_ptr)    
    name = mpp_get_domain_name(Domain)
    !call fms_f2c_string(name_ptr, name)

  end subroutine py_mpp_get_domain_name

  
  subroutine test(arg1, arg2, arg3)

    implicit none
    integer, intent(inout) :: arg1
    integer, intent(inout) :: arg2(2)
    integer, intent(inout), optional :: arg3

    arg1 = 100
    arg2 = (/-100,100/)

    write(*,*) 'FORTRAN', arg3
    if(present(arg3)) write(*,*) 'arg3 is here'

    !test = mpp_domain.__py_mpp_domain_mod_MOD_test
    !test.argtypes = [ POINTER(c_int), np.ctypeslib.ndpointer(dtype=c_int, shape=(2,), flags="FORTRAN"), POINTER(c_int)]
    !test.restype = None
    
    !arg1 = c_int(-100)
    !arg2 = np.ctypeslib.as_array( np.array([1,1], dtype=np.int32) )
    !arg3 = None #c_int(1)                                                                                               
    !test(byref(arg1), arg2, None)
    
    !print(arg1)
    !print(arg2)
    !print(arg3)
    
  end subroutine test
  
end module py_mpp_mod
