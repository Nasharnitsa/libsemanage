Summary:	An interface for SELinux management
Summary(pl):	Interfejs do zarządzania SELinuksem
Name:		libsemanage
Version:	1.2
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.nsa.gov/selinux/archives/%{name}-%{version}.tgz
# Source0-md5:	83c6ab2b45cd35d148615fda3b04ba03
Patch0:		%{name}-printf_format.patch
URL:		http://www.nsa.gov/selinux/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libsepol-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An interface for SELinux management.

%description -l pl
Interfejs do zarządzania SELinuksem.

%package devel
Summary:	Header files for libsemanage library
Summary(pl):	Pliki nagłówkowe biblioteki libsemanage
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files for libsemanage library.

%description devel -l pl
Ten pakiet zawiera pliki nagłówkowe biblioteki libsemanage.

%package static
Summary:	Static version of libsemanage library
Summary(pl):	Statyczna wersja biblioteki libsemanage
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libsemanage library.

%description static -l pl
Statyczna wersja biblioteki libsemanage.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

#%post	-p /sbin/ldconfig
#%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
#%attr(755,root,root) %{_libdir}/libsemanage.so.*
%{_datadir}/semod

%files devel
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/libsemanage.so
%{_includedir}/semanage

%files static
%defattr(644,root,root,755)
%{_libdir}/libsemanage.a
