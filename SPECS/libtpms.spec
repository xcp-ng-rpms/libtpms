%global package_speccommit 951b2cc5b986544da7243030a7c38476e76dee27
%global usver 0.9.5
%global xsver 1
%global xsrel %{xsver}%{?xscount}%{?xshash}
%global package_srccommit v0.9.5

Summary: Library providing Trusted Platform Module (TPM) functionality
Name:           libtpms
Version:        0.9.5
Release:        %{?xsrel}%{?dist}
License:        BSD
Group:          Development/Libraries
Url:            http://sourceforge.net/projects/ibmswtpm
Source0: libtpms-0.9.5.tar.gz

BuildRequires:  openssl-devel
BuildRequires:  pkgconfig gawk sed
BuildRequires:  automake autoconf libtool bash coreutils gcc-c++
# XCP-ng: add epel-rpm-macros for %%ldconfig_scriptlets
BuildRequires:  epel-rpm-macros
%{?_cov_buildrequires}

%description
A library providing TPM functionality for VMs. Targeted for integration
into Qemu.

%package        devel
Summary:        Include files for libtpms
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description   devel
Libtpms header files and documentation.

%files
%{_libdir}/lib*.so.*
%doc LICENSE README CHANGES

%files devel
%{_libdir}/%{name}.so
%dir %{_includedir}/%{name}
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}/*.h
%{_mandir}/man3/*

%prep
%autosetup -p1
%{?_cov_prepare}

%build
NOCONFIGURE=1 sh autogen.sh
%configure --disable-static --with-tpm2 --without-tpm1 --with-openssl
%{?_cov_wrap} make %{?_smp_mflags}

%check
make check

%install
make DESTDIR="%{buildroot}" install
find %{buildroot} -type f -name '*.la' | xargs rm -f -- || :
%{?_cov_install}

%ldconfig_scriptlets

%{?_cov_results_package}

%changelog
* Wed Aug 17 2022 Ross Lagerwall <ross.lagerwall@citrix.com> - 0.9.5-1
- Update libtpms to v0.9.5 to fix a couple of Coverity issues

* Mon May 23 2022 Ross Lagerwall <ross.lagerwall@citrix.com> - 0.9.4-2
- Disable TPM 1.2 support

* Fri May 13 2022 Ross Lagerwall <ross.lagerwall@citrix.com> - 0.9.4-1
- Update libtpms to v0.9.4

* Fri Feb 18 2022 Igor Druzhinin <igor.druzhinin@citrix.com> - 0.9.1-2
- Enable static analysis

* Fri Jan 07 2022 Igor Druzhinin <igor.druzhinin@citrix.com> - 0.9.1-1
- Update libtpms to v0.9.1

* Fri Jul 31 2020 Stefan Berger <stefanb@linux.ibm.com> - 0.7.3-1
- Follow stable-0.7.0 branch to v0.7.3
