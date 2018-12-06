#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Socket6
Version  : 0.29
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/U/UM/UMEMOTO/Socket6-0.29.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/U/UM/UMEMOTO/Socket6-0.29.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-socket-inet6-perl/libio-socket-inet6-perl_2.72-2.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Socket6-lib = %{version}-%{release}
Requires: perl-Socket6-license = %{version}-%{release}
BuildRequires : buildreq-cpan

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
Requires: perl-Socket6-lib = %{version}-%{release}
Provides: perl-Socket6-devel = %{version}-%{release}

%description dev
dev components for the perl-Socket6 package.


%package lib
Summary: lib components for the perl-Socket6 package.
Group: Libraries
Requires: perl-Socket6-license = %{version}-%{release}

%description lib
lib components for the perl-Socket6 package.


%package license
Summary: license components for the perl-Socket6 package.
Group: Default

%description license
license components for the perl-Socket6 package.


%prep
%setup -q -n Socket6-0.29
cd ..
%setup -q -T -D -n Socket6-0.29 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Socket6-0.29/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Socket6
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Socket6/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Socket6.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Socket6.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Socket6/Socket6.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Socket6/deblicense_copyright
