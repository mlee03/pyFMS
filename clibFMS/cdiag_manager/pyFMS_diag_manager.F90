module pyFMS_diag_manager_mod

    use fms_mod
    use diag_manager_mod
    use diag_grid_mod
    use diag_axis_mod
    use iso_c_binding

    implicit none

    public :: pyFMS_diag_axis_init
    public :: pyFMS_diag_field_add_attribute
    public :: pyFMS_diag_grid_init
    public :: pyFMS_register_diag_field
    public :: pyFMS_register_static_field
    public :: pyFMS_send_data

    ! type(domain1D), public :: Domain1
    ! type(domain2D), public :: Domain2
    ! type(domainUG), public :: DomainUG

    interface pyFMS_diag_axis_init
      module procedure pyFMS_diag_axis_init_c_float
      module procedure pyFMS_diag_axis_init_c_double
    end interface pyFMS_diag_axis_init

    interface pyFMS_diag_field_add_attribute
      module procedure pyFMS_diag_field_add_attribute_array
      module procedure pyFMS_diag_field_add_attribute_scalar
    end interface pyFMS_diag_field_add_attribute
    
    interface pyFMS_register_diag_field
    module procedure pyFMS_register_diag_field_array
      module procedure pyFMS_register_diag_field_scalar
    end interface pyFMS_register_diag_field

    interface pyFMS_diag_grid_init
      module procedure pyFMS_diag_grid_init_c_float
      module procedure pyFMS_diag_grid_init_c_double
    end interface pyFMS_diag_grid_init

    interface pyFMS_send_data
        module procedure pyFMS_send_data_0d_c_float
        module procedure pyFMS_send_data_0d_c_double
        module procedure pyFMS_send_data_1d_c_float
        module procedure pyFMS_send_data_1d_c_double
        module procedure pyFMS_send_data_2d_c_float
        module procedure pyFMS_send_data_2d_c_double
        module procedure pyFMS_send_data_3d_c_float
        module procedure pyFMS_send_data_3d_c_double
        module procedure pyFMS_send_data_4d_c_float
        module procedure pyFMS_send_data_4d_c_double
    end interface pyFMS_send_data

    contains

    subroutine pyFMS_diag_field_add_attribute_array(diag_field_id, att_name_ptr, n, att_value)

      integer(c_int), intent(in) :: diag_field_id
      type(c_ptr) :: att_name_ptr
      integer(c_int) :: n
      real(c_double), intent(in) :: att_value(n)
    
      character(len=20) :: att_name
      att_name = fms_c2f_string(att_name_ptr)
    
      call diag_field_add_attribute(diag_field_id, att_name, att_value)
    
    end subroutine pyFMS_diag_field_add_attribute_array

    subroutine pyFMS_diag_field_add_attribute_scalar(diag_field_id, att_name_ptr, att_value)

      integer(c_int), intent(in) :: diag_field_id
      type(c_ptr) :: att_name_ptr
      real(c_double), intent(in) :: att_value
    
      character(len=20) :: att_name
      att_name = fms_c2f_string(att_name_ptr)
    
      call diag_field_add_attribute(diag_field_id, att_name, att_value)
    
    end subroutine pyFMS_diag_field_add_attribute_scalar

    function pyFMS_register_diag_field_array(module_name_ptr, field_name_ptr, n, axes)

      type(c_ptr), intent(in) :: module_name_ptr
      type(c_ptr), intent(in) :: field_name_ptr
      integer(c_int), intent(in) :: n
      integer(c_int), intent(in) :: axes(n)
      integer(c_int) :: pyFMS_register_diag_field_array
    
      character(len=20) :: module_name
      character(len=20) :: field_name
    
      module_name = fms_c2f_string(module_name_ptr)
      field_name = fms_c2f_string(field_name_ptr)
    
      pyFMS_register_diag_field_array = register_diag_field(module_name, field_name, axes)
    
    end function pyFMS_register_diag_field_array
    
    function pyFMS_register_diag_field_scalar(module_name_ptr, field_name_ptr)
    
      type(c_ptr), intent(in) :: module_name_ptr
      type(c_ptr), intent(in) :: field_name_ptr
      integer(c_int) :: pyFMS_register_diag_field_scalar
    
      character(len=20) :: module_name
      character(len=20) :: field_name
    
      module_name = fms_c2f_string(module_name_ptr)
      field_name = fms_c2f_string(field_name_ptr)
    
      pyFMS_register_diag_field_scalar = register_diag_field(module_name, field_name)
    
    end function pyFMS_register_diag_field_scalar

    function pyFMS_register_static_field(module_name_ptr, field_name_ptr, n, axes)

      type(c_ptr), intent(in) :: module_name_ptr
      type(c_ptr), intent(in) :: field_name_ptr
      integer(c_int), intent(in) :: n
      integer(c_int), intent(in) :: axes(n)
      integer(c_int) :: pyFMS_register_static_field

      character(len=20) :: module_name
      character(len=20) :: field_name

      module_name = fms_c2f_string(module_name_ptr)
      field_name = fms_c2f_string(field_name_ptr)

      pyFMS_register_static_field = register_static_field(module_name, field_name, axes)

    end function pyFMS_register_static_field

#include "include/pyFMS_diag_manager.fh"

end module pyFMS_diag_manager_mod