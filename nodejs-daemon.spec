%define		pkg	daemon
Summary:	Add-on for creating *nix daemons
Name:		nodejs-%{pkg}
Version:	0.5.1
Release:	2
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/indexzero/daemon.node
Source0:	http://registry.npmjs.org/daemon/-/%{pkg}-%{version}.tgz
# Source0-md5:	31730d0308efdc9435440e1880e82b9d
BuildRequires:	libstdc++-devel
BuildRequires:	nodejs-devel
BuildRequires:	rpmbuild(macros) >= 1.634
# due library being versioned
%requires_eq	nodejs
Requires:	nodejs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# redefine for arch specific
%define		nodejs_libdir	%{_libdir}/node

%description
A C++ add-on for Node.js to enable simple daemons in JavaScript plus
some useful wrappers in JavaScript.

%prep
%setup -qc
mv package/* .

cat > install <<EOF
#!/bin/sh
exit 0
EOF

%build
node-waf configure build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr lib package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

version=$(node -v)
install -p build/Release/daemon.node $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}/lib/daemon.$version.node
install -p install $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%dir %{nodejs_libdir}/%{pkg}
%{nodejs_libdir}/%{pkg}/package.json
%dir %{nodejs_libdir}/%{pkg}/lib
%{nodejs_libdir}/%{pkg}/lib/daemon.js
%attr(755,root,root) %{nodejs_libdir}/%{pkg}/lib/daemon.v*.node
%attr(755,root,root) %{nodejs_libdir}/%{pkg}/install

%{_examplesdir}/%{name}-%{version}
