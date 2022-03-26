%define		module		asciinema
%define		egg_name	asciinema
%define		pypi_name	asciinema
Summary:	Command line client (terminal recorder) for asciinema.org service
Name:		asciinema
Version:	1.4.0
Release:	7
License:	GPL v3
Group:		Applications/Networking
#Source0:	https://github.com/asciinema/asciinema/archive/v%{version}/%{name}-%{version}.tar.gz
Source0:	https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	507ec769e1e9f8d5146b8c32c5ed54ac
URL:		http://asciinema.org/docs
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python3-setuptools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Asciinema is a free and open source solution for recording the
terminal sessions and sharing them on the web.

%prep
%setup -q

# Remove bundled egg-info
%{__rm} -r %{egg_name}.egg-info

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/asciinema
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
