#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Socket6
Version  : 0.29
Release  : 31
URL      : https://cpan.metacpan.org/authors/id/U/UM/UMEMOTO/Socket6-0.29.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/U/UM/UMEMOTO/Socket6-0.29.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-socket-inet6-perl/libio-socket-inet6-perl_2.72-2.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Socket6-license = %{version}-%{release}
Requires: perl-Socket6-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Socket6
1. Abstract
This module supports getaddrinfo() and getnameinfo() to intend to
enable protocol independent programing.
If your environment supports IPv6, IPv6 related defines such as
AF_INET6 are included.

%package dev
Summary: dev components for the perl-Socket6 package.
Group: Development
Provides: perl-Socket6-devel = %{version}-%{release}
Requires: perl-Socket6 = %{version}-%{release}

%description dev
dev components for the perl-Socket6 package.


%package license
Summary: license components for the perl-Socket6 package.
Group: Default

%description license
license components for the perl-Socket6 package.


%package perl
Summary: perl components for the perl-Socket6 package.
Group: Default
Requires: perl-Socket6 = %{version}-%{release}

%description perl
perl components for the perl-Socket6 package.


%prep
%setup -q -n Socket6-0.29
cd %{_builddir}
tar xf %{_sourcedir}/libio-socket-inet6-perl_2.72-2.debian.tar.xz
cd %{_builddir}/Socket6-0.29
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Socket6-0.29/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Socket6
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Socket6/77c9a481e6b50f1c0997b69f7a44b5fa63673a28 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Socket6.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Socket6/77c9a481e6b50f1c0997b69f7a44b5fa63673a28

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
