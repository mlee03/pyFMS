module pyFMS_diag_manager_mod

    use libFMS
    use iso_c_binding

    implicit none

    public :: pyFMS_diag_axis_init
    public :: pyFMS_register_diag_field
    public :: pyFMS_register_static_field
    public :: pyFMS_send_data
    public :: pyFMS_diag_grid_init
    public :: pyFMS_diag_field_add_attribute

    type(domain1D), public :: Domain1
    type(domain2D), public :: Domain2
    type(domainUG), public :: DomainUG

    interface pyFMS_diag_axis_init
      module procedure pyFMS_diag_axis_init_c_float
      module procedure pyFMS_diag_axis_init_c_double
    end interface pyFMS_diag_axis_init

    interface pyFMS_send_data_0d
      module procedure pyFMS_send_data_0d_c_float
      module procedure pyFMS_send_data_0d_c_double
    end interface pyFMS_send_data_0d

    interface pyFMS_send_data_1d
      module procedure pyFMS_send_data_1d_c_float
      module procedure pyFMS_send_data_1d_c_double
    end interface pyFMS_send_data_1d

    interface pyFMS_send_data_2d
      module procedure pyFMS_send_data_2d_c_float
      module procedure pyFMS_send_data_2d_c_double
    end interface pyFMS_send_data_2d

    interface pyFMS_send_data_3d
      module procedure pyFMS_send_data_3d_c_float
      module procedure pyFMS_send_data_3d_c_double
    end interface pyFMS_send_data_3d

    interface pyFMS_send_data_4d
      module procedure pyFMS_send_data_4d_c_float
      module procedure pyFMS_send_data_4d_c_double
    end interface pyFMS_send_data_4d

    interface pyFMS_diag_grid_init
      module procedure pyFMS_diag_grid_init_c_float
      module procedure pyFMS_diag_grid_init_c_double
    end interface pyFMS_diag_grid_init

    interface pyFMS_diag_field_add_attribute_scalar
      module procedure pyFMS_diag_field_add_attribute_scalar_c_float
      module procedure pyFMS_diag_field_add_attribute_scalar_c_double
    end interface pyFMS_diag_field_add_attribute_scalar

    interface pyFMS_diag_field_add_attribute_array
      module procedure pyFMS_diag_field_add_attribute_array_c_float
      module procedure pyFMS_diag_field_add_attribute_array_c_double
    end interface pyFMS_diag_field_add_attribute_array



    contains

      function pyFMS_register_diag_field(module_name_ptr, field_name_ptr, n, axes)

        type(c_ptr), intent(in) :: module_name_ptr
        type(c_ptr), intent(in) :: field_name_ptr
        type(c_int), intent(in), optional :: n
        type(c_int), intent(in), optional :: axes(n)
        type(c_int) :: pyFMS_register_diag_field

        character(len=20) :: module_name
        character(len=20) :: field_name

        module_name = fms_c2f_string(module_name_ptr)
        field_name = fms_c2f_string(field_name_ptr)

        if (present(axes)) then
          pyFMS_register_diag_field = register_diag_field(module_name, field_name, axes)
        else
          pyFMS_register_diag_field = register_diag_field(module_name, field_name)
        end if

      end function pyFMS_register_diag_field

      function pyFMS_register_static_field(module_name_ptr, field_name_ptr, n, axes)

        type(c_ptr), intent(in) :: module_name_ptr
        type(c_ptr), intent(in) :: field_name_ptr
        type(c_int64_t), intent(in) :: n
        type(c_int64_t), intent(in) :: axes(n)
        type(c_int) :: pyFMS_register_static_field

        character(len=20) :: module_name
        character(len=20) :: field_name

        module_name = fms_c2f_string(module_name_ptr)
        field_name = fms_c2f_string(field_name_ptr)

        pyFMS_register_diag_field = register_static_field(module_name, field_name, axes)

      end function pyFMS_register_static_field

#include "include/pyFMS_diag_manager.fh"

end module pyFMS_diag_manager_mod