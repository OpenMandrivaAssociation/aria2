Summary: 	Download utility with resuming and segmented downloading
Name: 		aria2
Version: 	0.15.3
Release:	%mkrel 0.20080918.2
License: 	GPLv2+
Group: 		Networking/File transfer
Source0: 	aria2c-r729.tar.lzma
Patch0:		aria2c-AdaptiveURISelector.patch
Patch1:		aria2c-fix-build-on-x86_64.patch
URL: 		http://aria2.sourceforge.net/
Buildrequires:  libxml2-devel openssl-devel c-ares-devel
BuildRequires:	libgcrypt-devel gnutls-devel cppunit-devel
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
Aria2 has segmented downloading engine in its core. It can download one 
file from multiple URLs or multiple connections from one URL. This results
in very high speed downloading, very much faster than ordinary browsers.
This engine is implemented with a single-thread model.
It can also download BitTorrent files and supports Metalink version 3.0.

%prep
%setup -q -n%{name}c
%patch0 -b .adaptive
%patch1

%build
%configure2_5x --without-gnutls
%make 

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_datadir}/locale/locale.alias
rm -fr %{buildroot}%{_datadir}/doc

%find_lang aria2c

%clean
rm -rf %{buildroot}

%files -f aria2c.lang
%defattr(-, root, root)
%doc ChangeLog README* TODO *.html
%{_bindir}/*
%{_mandir}/man1/*
