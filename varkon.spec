Summary:	VARKON - a free CAD system
Summary(pl):	VARKON - ogolnodostêpny program typu CAD
Name:		varkon
Version:	1.17C
Release:	2
License:	GPL
Group:		Applications/Engineering
Source0:	http://www.microform.se/pub/linux/%{name}_sources_%{version}.tar.gz
Source1:	http://www.microform.se/v_man.zip
Source2:	http://www.microform.se/m_man.zip
Source3:	%{name}-run
Patch0:		%{name}-make.patch
URL:		http://www.microform.se/index.htm
BuildRequires:	unzip
BuildRequires:	XFree86-devel
BuildRequires:	OpenGL-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
VARKON - a free CAD system and high level development tool for
Engineering.

Documentation included.

%description -l pl
VARKON jest _SYSTEMEM_ typu CAD, pozwalaj±cym dziêki specjalnemu
jêzykowi MBS na prowadzenie zaawansowanych prac i dostosowanie
programu do specjalistycznych celów.

Pakiet zawiera dokumentacjê.

%prep
%setup -q -n %{name}_%{version}
%patch -p1

mkdir man
(cd man
unzip -q %{SOURCE1}
unzip -n -q %{SOURCE2}
)

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
