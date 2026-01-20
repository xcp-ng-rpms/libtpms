%global package_speccommit eb8a97c21541f319e86f827c87aa141df178ccb9
%global usver 0.9.6
%global xsver 3
%global xsrel %{xsver}%{?xscount}%{?xshash}
%global package_srccommit v0.9.6

Summary: Library providing Trusted Platform Module (TPM) functionality
Name:           libtpms
Version:        0.9.6
Release:        %{?xsrel}.1%{?dist}
License:        BSD
Group:          Development/Libraries
Url:            http://sourceforge.net/projects/ibmswtpm
Source0: libtpms-0.9.6.tar.gz
Patch0: 0001-tpm2-Initialize-variable-reported-by-Coverity-false-.patch
Patch1: 0002-tpm2-Initialize-variable-reported-by-Coverity-false-.patch
Patch2: 0003-tpm2-Initialize-variable-reported-by-Coverity-false-.patch
Patch3: 0004-tpm2-Require-TPM_NV_DISK-to-avoid-case-of-tpm_stata_.patch
Patch4: 0005-nvfile-Free-allocated-memory-on-failure.patch
Patch5: 0006-tpm2-Assign-result-of-OsslToTpmBn-to-OK.patch
Patch6: 0007-tpm2-Expect-TPM_SUCCESS-from-tpm_io_getlocality-call.patch
Patch7: 0008-man-Update-description-of-tpm_io_getlocality-callbac.patch
Patch8: 0009-tpm2-Access-entrysize-variable-only-if-it-was-read-f.patch
Patch9: 0010-tpm2-Do-not-access-variable-if-it-could-not-be-read-.patch
Patch10: 0001-tpm2-Check-size-of-TPM2B_NAME-buffer-before-reading-.patch
Patch11: tpm2-Fix-potential-out-of-bound-access-abort-due-to-.patch

BuildRequires:  openssl-devel
BuildRequires:  pkgconfig gawk sed
BuildRequires:  automake autoconf libtool bash coreutils gcc-c++
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
* Tue Jan 20 2026 Philippe Coval <philippe.coval@vates.tech> - 0.9.6-3.1
- Rebuild for openssl-3

* Fri Jun 13 2025 Ross Lagerwall <ross.lagerwall@citrix.com> - 0.9.6-3
- CA-412377: Fix potential OOB access (CVE-2025-49133)

* Mon Mar 10 2025 Deli Zhang <deli.zhang@cloud.com> - 0.9.6-2
- CP-53516: Rebuild with OpenSSL 3 for XS8

* Wed Mar 01 2023 Ross Lagerwall <ross.lagerwall@citrix.com> - 0.9.6-1
- Update libtpms to v0.9.6 to fix CVE-2023-1017 & -1018
- Backport static analysis fixes

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
