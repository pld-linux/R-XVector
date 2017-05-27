%define		packname	XVector

Summary:	Representation and manpulation of external sequences
Name:		R-%{packname}
Version:	0.2.0
Release:	2
License:	Artistic 2.0
Group:		Applications/Math
Source0:	http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	d5c6799b09b67f1fa5942ed6d60e5452
URL:		http://www.bioconductor.org/packages/release/bioc/html/XVector.html
BuildRequires:	R
BuildRequires:	R-BiocGenerics
BuildRequires:	R-IRanges-devel >= 1.19.36
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-BiocGenerics
Requires:	R-IRanges >= 1.19.36
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Memory efficient S4 classes for storing sequences "externally"
(behind an R external pointer, or on disk).

%package        devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -c -n %{packname}

%build
# circular dep on R-Rsamtools
#{_bindir}/R CMD build %{packname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/html/
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/unitTests/
%{_libdir}/R/library/%{packname}/libs/

%files devel
%defattr(644,root,root,755)
%{_libdir}/R/library/%{packname}/include
