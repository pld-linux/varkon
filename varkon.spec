Summary:	VARKON - a free CAD system.
Summary(pl):	VARKON - ogolnodostepny program typu CAD.
Name:		varkon
Version:	1.17C
Release:	1
Copyright:	GNU/LGPL
Group:		Application/Engineering/CAD
Group(pl):	Aplikacje/Inzynierskie/CAD
Source0:	http://www.microform.se/pub/linux/%{name}_sources_%{version}.tar.gz
Source1:	http://www.microform.se/v_man.zip
Source2:	http://www.microform.se/m_man.zip
#BuildRequires:	
#Requires:	
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
URL:		http://www.microform.se/index.htm

%define	_prefix	/usr

%description
VARKON - a free CAD system and high level development tool for Engineering.

Documentation included!

%description -l pl
VARKON jest _SYSTEMEM_ typu CAD. Pozwalajacemu dzieki specjalnemu jezykowi
MBS na prowadzenie zaawansowanych prac i dostosowanie programu do 
specjalistycznych celow.

Pakiet zawiera dokumentacje!

%prep
%setup -q

#%patch

%build
./configure --prefix=%{_prefix}
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(,,)
