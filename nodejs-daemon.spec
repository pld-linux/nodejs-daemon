%define		pkg	daemon
Summary:	Add-on for creating *nix daemons
Name:		nodejs-%{pkg}
Version:	1.1.0
Release:	3
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/daemon/-/%{pkg}-%{version}.tgz
# Source0-md5:	58e1b7b90b453eb610dd4c85de800e5d
URL:		https://github.com/indexzero/daemon.node
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs >= 0.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Turn a node script into a daemon.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr index.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%dir %{nodejs_libdir}/%{pkg}
%{nodejs_libdir}/%{pkg}/package.json
%{nodejs_libdir}/%{pkg}/index.js
%{_examplesdir}/%{name}-%{version}
