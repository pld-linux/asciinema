Summary:	Command line recorder for asciinema.org service
Name:		asciinema
Version:	0.9.7
Release:	1
License:	MIT
Group:		Applications/Networking
Source0:	https://pypi.python.org/packages/source/a/asciinema/%{name}-%{version}.tar.gz
# Source0-md5:	df9cde430210db8f054e78e163914ca5
URL:		http://asciinema.org/docs
BuildRequires:	rpm-pythonprov
Requires:	python-distribute
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command line client for asciinema.org service.

%prep
%setup -q

# Remove bundled egg-info
%{__rm} -r %{name}.egg-info

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/asciinema
%{py_sitescriptdir}/asciinema
%{py_sitescriptdir}/asciinema-%{version}-py*.egg-info
