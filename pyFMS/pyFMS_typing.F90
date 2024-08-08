module pyFMS_typing
    
    use mpp_domains_mod

    public :: pyFMS_get_domain1D
    public :: pyFMS_get_domain2D
    public :: pyFMS_get_domainUG

    type(domain1D), public :: Domain1D
    type(domain2D), public :: Domain2D
    type(domainUG), public :: DomainUG

    contains

      !> retrieve 1D domain
      function pyFMS_get_domain1D()
        type(domain1D) :: pyFMS_get_domain1D
        pyFMS_get_domain1D = Domain1D
      end function pyFMS_get_domain1D

      !> retrieve 2D domain
      function pyFMS_get_domain2D()
        type(domain2D) :: pyFMS_get_domain2D
        pyFMS_get_domain2D = Domain2D
      end function pyFMS_get_domain2D

      !> retrieve UG domain
      function pyFMS_get_domainUG()
        type(domainUG) :: pyFMS_get_domainUG
        pyFMS_get_domainUG = DomainUG
      end function pyFMS_get_domainUG

end module pyFMS_typing