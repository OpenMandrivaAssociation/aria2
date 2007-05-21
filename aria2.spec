%define name	aria2
%define version	0.10.2+1
%define release	%mkrel 1
%define group	Networking/File transfer

%define	section	Internet/File Transfer
%define	title	Aria2 is a download utility with resuming and segmented downloading

%define Summary	Aria2 is a download utility with resuming and segmented downloading

Summary: 	%{Summary}
Name: 		%{name}
Version: 	%{version}
Release:	%{release}
License: 	GPL
Group: 		%{group}
Source: 	%{name}-%{version}.tar.bz2
URL: 		http://aria2.sourceforge.net/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires:  %{mklibname xml2}-devel

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
%configure

%make 

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -fr %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc ChangeLog INSTALL README TODO 
%{_bindir}/*
%{_prefix}/share/*


