Summary: 	Aria2 is a download utility with resuming and segmented downloading
Name: 		aria2
Version: 	0.11.2
Release:	%mkrel 2
License: 	GPL
Group: 		Networking/File transfer
Source: 	http://nchc.dl.sourceforge.net/sourceforge/aria2/%{name}-%{version}.tar.bz2
URL: 		http://aria2.sourceforge.net/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires:  libxml2-devel gnutls-devel

%description
Aria2 has segmented downloading engine in its core. It can download one 
file from multiple URLs or multiple connections from one URL. This results
in very high speed downloading, very much faster than ordinary browsers.
As of 0.3.0 release, It can also download BitTorrent files.
We implemented this engine in single-thread model.
The architecture is very clean and easy to extend.
It also supports Metalink version 3.0.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x

%make 

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang aria2c

%clean
rm -fr %{buildroot}

%files -f aria2c.lang
%defattr(-, root, root)
%doc ChangeLog INSTALL README TODO 
%{_bindir}/*
%{_mandir}/man1/*
