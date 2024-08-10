! -*-f90-*-
!***********************************************************************
!*                   GNU Lesser General Public License
!*
!* This file is part of the GFDL Flexible Modeling System (FMS).
!*
!* FMS is free software: you can redistribute it and/or modify it under
!* the terms of the GNU Lesser General Public License as published by
!* the Free Software Foundation, either version 3 of the License, or (at
!* your option) any later version.
!*
!* FMS is distributed in the hope that it will be useful, but WITHOUT
!* ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
!* FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
!* for more details.
!*
!* You should have received a copy of the GNU Lesser General Public
!* License along with FMS.  If not, see <http://www.gnu.org/licenses/>.
!***********************************************************************

!> @file
!> @brief Various routines handling domains in @ref mpp_domains_mod

!> @addtogroup pyfms_diag_manager_mod
!> @{
function PYFMS_DIAG_AXIS_INIT_(name_ptr, dim, array_data, & 
  units_ptr, cart_name_ptr)

  type(c_ptr), intent(in) :: name_ptr
  real(FMS_KIND_), intent(in) :: dim
  real(FMS_KIND_), intent(in), optional :: array_data(dim)
  type(c_ptr), intent(in) :: units_ptr
  type(c_ptr), intent(in) :: cart_name_ptr
  type(c_int64_t) :: PYFMS_DIAG_AXIS_INIT_

  character(len=20) :: name
  character(len=20) :: units
  character(len=20) :: cart_name

  name = fms_c2f_string(name_ptr)
  units = fms_c2f_string(units_ptr)
  cart_name = fms_c2f_string(cart_name_ptr)

  PYFMS_DIAG_AXIS_INIT_ = diag_axis_init(name, array_data, units, cart_name)

end function PYFMS_DIAG_AXIS_INIT_

!############################################################################

function PYFMS_SEND_DATA_0D_(diag_field_id, field)

  type(c_int64_t), intent(in) :: diag_field_id
  real(FMS_KIND_), intent(in) :: field
  type(c_bool) :: PYFMS_SEND_DATA_0D_

  PYFMS_SEND_DATA_0D_ = send_data(diag_field_id, field)

end function PYFMS_SEND_DATA_0D_

!############################################################################

function PYFMS_SEND_DATA_1D_(diag_field_id, n, field)

  type(c_int64_t), intent(in) :: diag_field_id
  type(c_int64_t), intent(in) :: n
  real(FMS_KIND_), intent(in) :: field(n)
  type(c_bool) :: PYFMS_SEND_DATA_1D_

  PYFMS_SEND_DATA_1D_ = send_data(diag_field_id, field)

end function PYFMS_SEND_DATA_1D_

!############################################################################

function PYFMS_SEND_DATA_2D_(diag_field_id, n, m, field)

  type(c_int64_t), intent(in) :: diag_field_id
  type(c_int64_t), intent(in) :: n
  type(c_int64_t), intent(in) :: m
  real(FMS_KIND_), intent(in) :: field(n,m)
  type(c_bool) :: PYFMS_SEND_DATA_2D_

  PYFMS_SEND_DATA_2D_ = send_data(diag_field_id, field)

end function PYFMS_SEND_DATA_2D_

!############################################################################

function PYFMS_SEND_DATA_3D_(diag_field_id, n, m, l, field)

  type(c_int64_t), intent(in) :: diag_field_id
  type(c_int64_t), intent(in) :: n
  type(c_int64_t), intent(in) :: m
  type(c_int64_t), intent(in) :: l
  real(FMS_KIND_), intent(in) :: field(n,m,l)
  type(c_bool) :: PYFMS_SEND_DATA_3D_

  PYFMS_SEND_DATA_3D_ = send_data(diag_field_id, field)

end function PYFMS_SEND_DATA_3D_

!############################################################################

function PYFMS_SEND_DATA_4D_(diag_field_id, n, m, l, k, field)

  type(c_int64_t), intent(in) :: diag_field_id
  type(c_int64_t), intent(in) :: n
  type(c_int64_t), intent(in) :: m
  type(c_int64_t), intent(in) :: l
  type(c_int64_t), intent(in) :: k
  real(FMS_KIND_), intent(in) :: field(n,m,l,k)
  type(c_bool) :: PYFMS_SEND_DATA_4D_

  PYFMS_SEND_DATA_4D_ = send_data(diag_field_id, field)

end function PYFMS_SEND_DATA_4D_

!############################################################################

subroutine PYFMS_DIAG_GRID_INIT_(domain, glo_lat, glo_lon, aglo_lat, aglo_lon, dim_glo, dim_aglo)
        
  Domain
  type(c_int64_t), intent(in) :: dim_glo, dim_aglo
  real(FMS_KIND_), intent(in) :: glo_lat(dim_glo,dim_glo)
  real(FMS_KIND_), intent(in) :: glo_lon(dim_glo,dim_aglo)
  real(FMS_KIND_), intent(in) :: aglo_lat(dim_aglo,dim_aglo)
  real(FMS_KIND_), intent(in) :: aglo_lon(dim_aglo,dim_aglo)

  call diag_grid_init(Domain, glo_lat, glo_lon, aglo_lat, aglo_lon)

end subroutine PYFMS_DIAG_GRID_INIT_

!############################################################################

subroutine PYFMS_DIAG_FIELD_ADD_ATTRIBUTE_SCALAR_(diag_field_id, att_name_ptr, att_value)

  type(c_int64_t), intent(in) :: diag_field_id
  type(c_ptr) :: att_name_ptr
  real(FMS_KIND_), intent(in) :: att_value

  character(len=20) :: att_name
  att_name = fms_c2f_string(att_name_ptr)

  call diag_field_add_attribute(diag_field_id, att_name, att_value)

end subroutine PYFMS_DIAG_FIELD_ADD_ATTRIBUTE_SCALAR_

!############################################################################

subroutine PYFMS_DIAG_FIELD_ADD_ATTRIBUTE_ARRAY_(diag_field_id, att_name_ptr, n, att_value)

  type(c_int64_t), intent(in) :: diag_field_id
  type(c_ptr) :: att_name_ptr
  type(c_int64_t) :: n
  real(FMS_KIND_), intent(in) :: att_value(n)

  character(len=20) :: att_name
  att_name = fms_c2f_string(att_name_ptr)

  call diag_field_add_attribute(diag_field_id, att_name, att_value)

end subroutine PYFMS_DIAG_FIELD_ADD_ATTRIBUTE_ARRAY_
!> @}