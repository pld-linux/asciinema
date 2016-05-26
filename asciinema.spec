Summary:	Command line client (terminal recorder) for asciinema.org service
Name:		asciinema
Version:	1.2.0
Release:	1
License:	MIT
Group:		Applications/Networking
Source0:	https://github.com/asciinema/asciinema/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f61680ca17328ed43b61a24b1c267e29
URL:		http://asciinema.org/docs
BuildRequires:	golang >= 1.3.1
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages 0
%define		gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%define		gopath		%{_libdir}/golang
%define		import_path	github.com/asciinema/asciinema

%description
Asciinema is a free and open source solution for recording the
terminal sessions and sharing them on the web.

%prep
%setup -q

%build
# set up temporary build gopath, and put our directory there
install -d _build/src/%{import_path}
ln -s $(pwd)/* _build/src/%{import_path}

export GOPATH=$(pwd)/_build:%{gopath}
LDFLAGS="-s -linkmode external"
%gobuild -o "bin/%{name}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p bin/asciinema $RPM_BUILD_ROOT%{_bindir}/asciinema
cp -p -p man/asciinema.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/asciinema
%{_mandir}/man1/asciinema.1*
