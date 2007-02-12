Summary:	VARKON - a free CAD system
Summary(pl.UTF-8):   VARKON - ogolnodostępny program typu CAD
Name:		varkon
Version:	1.17D
Release:	1
License:	GPL
Group:		Applications/Engineering
#Source0Download: http://www.tech.oru.se/cad/varkon/sources.htm
Source0:	http://www.tech.oru.se/cad/varkon/pub/linux/%{name}_sources_%{version}.tar.gz
# Source0-md5:	4a7e4573cc525b9e39428df6f97c036f
Source1:	http://www.tech.oru.se/cad/varkon/v_man.zip
# Source1-md5:	9bb474690c3c778fb361f2e487737ae3
Source2:	http://www.tech.oru.se/cad/varkon/m_man.zip
# Source2-md5:	95471415f387326ea105ea068a6bb175
Source3:	%{name}-run
Patch0:		%{name}-make.patch
URL:		http://www.tech.oru.se/cad/varkon/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	unzip
Requires:	OpenGL
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
%setup -q -n %{name}_%{version}
%patch0 -p1

mkdir man
cd man
unzip -q %{SOURCE1}
unzip -n -q %{SOURCE2}

%build
CC="%{__cc}"
OPTFLAGS="%{rpmcflags} -I/usr/X11R6/include"
LDFLAGS="%{rpmldflags}"
VARKON_ROOT="`pwd`"
export CC OPTFLAGS LDFLAGS VARKON_ROOT
cd sources
./make_varkon

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/varkon}

install %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/varkon
cp -pr bin cnf erm lib man mdf $RPM_BUILD_ROOT%{_libdir}/varkon

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
