%define		srcname		Varkon
Summary:	VARKON - a free CAD system
Summary(pl.UTF-8):	VARKON - ogolnodostępny program typu CAD
Name:		varkon
Version:	1.19D
Release:	1
License:	GPL
Group:		Applications/Engineering
Source0:	http://dl.sourceforge.net/varkon/%{srcname}_sources_%{version}.tar.gz
# Source0-md5:	1bbdf0c1b29393aa3bbaaccda43b21bc
Source1:	%{name}-run
Patch0:		%{name}-make.patch
Patch1:		%{name}-h_addr.patch
URL:		http://www.tech.oru.se/cad/varkon/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	zlib-devel
Requires:	OpenGL
Requires:	libjpeg
Requires:	libtiff
Requires:	xorg-lib-libX11
Requires:	xorg-lib-libXext
Requires:	xorg-lib-libXpm
Requires:	xorg-lib-libXxf86vm
Requires:	zlib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
# /usr/lib/varkon used in varkon-run
%define		_libdir		%{_prefix}/lib

%description
VARKON - a free CAD system and high level development tool for
Engineering.

Documentation included.

%description -l pl.UTF-8
VARKON jest _SYSTEMEM_ typu CAD, pozwalającym dzięki specjalnemu
językowi MBS na prowadzenie zaawansowanych prac i dostosowanie
programu do specjalistycznych celów.

Pakiet zawiera dokumentację.

%prep
%setup -q -n %{srcname}_%{version}
%patch0 -p1
%patch1 -p1

%build
CC="%{__cc}"
OPTFLAGS="%{rpmcflags} -I/usr/X11R6/include"
LDFLAGS="%{rpmldflags}"
VARKON_ROOT=$(pwd)
export CC OPTFLAGS LDFLAGS VARKON_ROOT
cd sources
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/varkon}
install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/varkon
cp -a bin cnf erm lib man mdf $RPM_BUILD_ROOT%{_libdir}/varkon

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/varkon
%dir %{_libdir}/varkon
%dir %{_libdir}/varkon/bin
%attr(755,root,root) %{_libdir}/varkon/bin/*
%dir %{_libdir}/varkon/cnf
%{_libdir}/varkon/cnf/fnt
%{_libdir}/varkon/cnf/snd
%{_libdir}/varkon/cnf/icons
%dir %{_libdir}/varkon/cnf/ini
%{_libdir}/varkon/cnf/ini/english
%lang(sv) %{_libdir}/varkon/cnf/ini/swedish
%{_libdir}/varkon/cnf/plt
%{_libdir}/varkon/cnf/tol
%{_libdir}/varkon/erm
%{_libdir}/varkon/lib
%{_libdir}/varkon/man
%docdir %{_libdir}/varkon/man
%dir %{_libdir}/varkon/mdf
%{_libdir}/varkon/mdf/english
%lang(sv) %{_libdir}/varkon/mdf/swedish
