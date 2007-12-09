Summary: 	Download utility with resuming and segmented downloading
Name: 		aria2
Version: 	0.12.0
Release:	%mkrel 1
License: 	GPLv2+
Group: 		Networking/File transfer
Source0: 	http://nchc.dl.sourceforge.net/sourceforge/aria2/%{name}-%{version}.tar.bz2
URL: 		http://aria2.sourceforge.net/
Buildrequires:  libxml2-devel openssl-devel c-ares-devel
BuildRequires:	libgcrypt-devel gnutls-devel cppunit-devel

%description
Aria2 has segmented downloading engine in its core. It can download one 
file from multiple URLs or multiple connections from one URL. This results
in very high speed downloading, very much faster than ordinary browsers.
This engine is implemented with a single-thread model.
It can also download BitTorrent files and supports Metalink version 3.0.

%prep
%setup -q

%build
%configure2_5x --without-gnutls
%make 

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang aria2c

%clean
rm -rf %{buildroot}

%files -f aria2c.lang
%defattr(-, root, root)
%doc ChangeLog README TODO 
%{_bindir}/*
%{_mandir}/man1/*
