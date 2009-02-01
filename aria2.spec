%define snapdate 20090201

Summary: 	Download utility with resuming and segmented downloading
Name: 		aria2
Version: 	1.2.0
Release:	%mkrel 0.20090201.1
License: 	GPLv2+
Group: 		Networking/File transfer
Source0: 	http://downloads.sourceforge.net/aria2/%name-%{version}b+%{snapdate}.tar.bz2
URL: 		http://aria2.sourceforge.net/
Buildrequires:  libxml2-devel openssl-devel c-ares-devel
BuildRequires:	sqlite3-devel cppunit-devel
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
Aria2 has segmented downloading engine in its core. It can download one 
file from multiple URLs or multiple connections from one URL. This results
in very high speed downloading, very much faster than ordinary browsers.
This engine is implemented with a single-thread model.
It can also download BitTorrent files and supports Metalink version 3.0.

%prep
%setup -q -n%{name}-%{version}b+%{snapdate}

%build
%configure2_5x --without-gnutls
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
