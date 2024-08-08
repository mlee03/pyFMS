module pyFMS_diag_manager_mod

    use diag_axis_mod
    use diag_manager_mod
    use mpp_domains_mod
    use mpp_mod
    use fms_mod
    use fms_string_utils_mod
    use py_mpp_mod
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


    contains

      integer function pyFMS_diag_axis_init(name_ptr, array_data_r4, array_data_r8, & 
          array_data_i4, units_ptr, cart_name_ptr)

        type(c_ptr), intent(in) :: name_ptr
        real, dimension(:), intent(in), optional :: array_data_r4
        real, dimension(:), intent(in), optional :: array_data_r8
        integer, dimension(:), intent(in), optional :: array_data_i4
        type(c_ptr), intent(in) :: units_ptr
        type(c_ptr), intent(in) :: cart_name_ptr

        character(len=20) :: name
        character(len=20) :: units
        character(len=20) :: cart_name

        name = fms_c2f_string(name_ptr)
        units = fms_c2f_string(units_ptr)
        cart_name = fms_c2f_string(cart_name_ptr)

        if (present(array_data_i4)) then
          pyFMS_diag_axis_init = diag_axis_init(name, array_data_i4, units, cart_name)
        elseif (present(array_data_r4)) then
          pyFMS_diag_axis_init = diag_axis_init(name, array_data_r4, units, cart_name)
        elseif (present(array_data_r8)) then
          pyFMS_diag_axis_init = diag_axis_init(name, array_data_r8, units, cart_name)
        else
          call error_mesg('pyFMS_diag_manager::pyFMS_diag_axis_init array_data not defined', FATAL)
        end if

      end function pyFMS_diag_axis_init

      integer function pyFMS_register_diag_field(module_name_ptr, field_name_ptr, axes_in)
        
        implicit none

        type(c_ptr), intent(in) :: module_name_ptr
        type(c_ptr), intent(in) :: field_name_ptr
        integer, dimension(:), intent(in), optional :: axes_in

        character(len=20) :: module_name
        character(len=20) :: field_name

        module_name = fms_c2f_string(module_name_ptr)
        field_name = fms_c2f_string(field_name_ptr)

        if (present(axes_in)) then
          pyFMS_register_diag_field = register_diag_field(module_name, field_name, axes_in)
        else
          pyFMS_register_diag_field = register_diag_field(module_name, field_name)
        end if

      end function pyFMS_register_diag_field

      integer function pyFMS_register_static_field(module_name_ptr, field_name_ptr, axes_in)

        implicit none

        type(c_ptr), intent(in) :: module_name_ptr
        type(c_ptr), intent(in) :: field_name_ptr
        integer, dimension(:), intent(in) :: axes_in

        character(len=20) :: module_name
        character(len=20) :: field_name

        module_name = fms_c2f_string(module_name_ptr)
        field_name = fms_c2f_string(field_name_ptr)

        pyFMS_register_diag_field = register_static_field(module_name, field_name, axes_in)

      end function pyFMS_register_static_field

      logical function pyFMS_send_data(diag_field_id, dim, field_si, field_sr, field_1di, &
          field_1dr, field_2di, field_2dr, field_3di, field_3dr, field_4di, field_4dr)

        implicit none

        integer, intent(in) :: diag_field_id
        integer, intent(in) :: dim
        integer, intent(in), optional :: field_si
        real, intent(in), optional :: field_sr
        integer, dimension(:), intent(in), optional :: field_1di
        real, dimension(:), intent(in), optional :: field_1dr
        integer, dimension(:,:), intent(in), optional :: field_2di
        real, dimension(:,:), intent(in), optional :: field_2dr
        integer, dimension(:,:,:), intent(in), optional :: field_3di
        real, dimension(:,:,:), intent(in), optional :: field_3dr
        integer, dimension(:,:,:,:), intent(in), optional :: field_4di
        real, dimension(:,:,:,:), intent(in), optional :: field_4dr

        if (present(field_si)) then
          pyFMS_send_data(diag_field_id, field_si)
        elseif (present(field_sr)) then
          pyFMS_send_data(diag_field_id, field_sr)
        elseif (present(field_1di)) then
          pyFMS_send_data(diag_field_id, field_1di)
        elseif (present(field_1dr)) then
          pyFMS_send_data(diag_field_id, field_1dr)
        elseif (present(field_2di)) then
          pyFMS_send_data(diag_field_id, field_2di)
        elseif (present(field_2dr)) then
          pyFMS_send_data(diag_field_id, field_2dr)
        elseif (present(field_3di)) then
          pyFMS_send_data(diag_field_id, field_3di)
        elseif (present(field_3dr)) then
          pyFMS_send_data(diag_field_id, field_3dr)
        elseif (present(field_4di)) then
          pyFMS_send_data(diag_field_id, field_4di)
        elseif (present(field_4dr)) then
          pyFMS_send_data(diag_field_id, field_4dr)
        else
          call error_mesg('pyFMS_diag_manager::pyFMS_send_data field not defined', FATAL)
        end if

      end function pyFMS_send_data

      subroutine pyFMS_diag_grid_init(domain, glo_lat_r, glo_lat_i, glo_lon_r, glo_lon_i, &
          aglo_lat_r, aglo_lat_i, aglo_lon_r, aglo_lon_i, t)
        
        Domain
        real, dimension(:,:), intent(in), optional :: glo_lat_r
        integer, dimension(:,:), intent(in), optional :: glo_lat_i
        real, dimension(:,:), intent(in), optional :: glo_lon_r
        integer, dimension(:,:), intent(in), optional :: glo_lon_i
        real, dimension(:,:), intent(in), optional :: aglo_lat_r
        integer, dimension(:,:), intent(in), optional :: aglo_lat_i
        real, dimension(:,:), intent(in), optional :: aglo_lon_r
        integer, dimension(:,:), intent(in), optional :: aglo_lon_i
        character(len=*) :: t

        if (t .eq. 'real') then
          call diag_grid_init(Domain, glo_lat_r, glo_lon_r, aglo_lat_r, aglo_lon_r)
        elseif (t .eq. 'integer') then
          call diag_grid_init(Domain, glo_lat_i, glo_lon_i, aglo_lat_i, aglo_lon_i)
        else
          call error_mesg('pyFMS_diag_manager::pyFMS_diag_grid_init type unknowm', FATAL)
        end if

      end subroutine pyFMS_diag_grid_init

      subroutine pyFMS_diag_field_add_attribute(diag_field_id_in, att_name_ptr, att_value_sr, &
          att_value_si, att_value_sc_ptr, att_value_r1, att_value_i1)

        implicit none

        integer, intent(in) :: diag_field_id_in
        type(c_ptr) :: att_name_ptr
        real, intent(in), optional :: att_value_sr
        integer, intent(in), optional :: att_value_si
        type(c_ptr), optional :: att_value_sc_ptr
        real, dimension(:), intent(in), optional :: att_value_r1
        integer, dimension(:), intent(in), optional :: att_value_i1

        character(len=20) :: att_name_in
        att_name_in = fms_c2f_string(att_name_ptr)

        if (present(att_value_sr)) then
          call diag_field_add_attribute(diag_field_id_in, att_name_in, att_value_sr)
        elseif (present(att_value_si)) then
          call diag_field_add_attribute(diag_field_id_in, att_name_in, att_value_si)
        elseif (present(att_value_sc_ptr)) then
          character(len=20) :: att_value_sc
          att_value_sc = fms_c2f_string(att_value_sc_ptr)
          call diag_field_add_attribute(diag_field_id_in, att_name_in, att_value_sc)
        elseif (present(att_value_r1)) then
          call diag_field_add_attribute(diag_field_id_in, att_name_in, att_value_r1)
        elseif (present(att_value_i1)) then
          call diag_field_add_attribute(diag_field_id_in, att_name_in, att_value_i1)
        else
          call error_mesg('pyFMS_diag_manager::pyFMS_diag_field_add_attribute att_value not defined', FATAL)
        end if

      end subroutine pyFMS_diag_field_add_attribute

end module pyFMS_diag_manager_mod