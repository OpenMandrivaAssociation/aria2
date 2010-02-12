Summary: 	Download utility with resuming and segmented downloading
Name: 		aria2
Version: 	1.8.2
Release:	%mkrel 2
License: 	GPLv2+
Group: 		Networking/File transfer
Source0: 	http://downloads.sourceforge.net/aria2/%name-%{version}.tar.xz
URL: 		http://aria2.sourceforge.net/
Buildrequires:  libxml2-devel gnutls-devel c-ares-devel
BuildRequires:	sqlite3-devel cppunit-devel
Requires:	rootcerts
#we need 1.7.0 to have ares_library_init available
Requires:	c-ares >= 1.7.0
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
Aria2 has segmented downloading engine in its core. It can download one 
file from multiple URLs or multiple connections from one URL. This results
in very high speed downloading, very much faster than ordinary browsers.
This engine is implemented with a single-thread model.
It can also download BitTorrent files and supports Metalink version 3.0.

%prep
%setup -q -n%{name}-%{version}

%build
%configure2_5x --with-ca-bundle="/etc/pki/tls/cert.pem"
%make 

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_datadir}/locale/locale.alias
rm -fr %{buildroot}%{_datadir}/doc

%find_lang aria2

%check
%make check

%clean
rm -rf %{buildroot}

%files -f aria2.lang
%defattr(-, root, root)
%doc ChangeLog README* *.html
%{_bindir}/*
%{_mandir}/man1/*
