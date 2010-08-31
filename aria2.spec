Summary:	Download utility with resuming and segmented downloading
Name:		aria2
Version:	1.10.2
Release:	%mkrel 1
License:	GPLv2+
Group:		Networking/File transfer
URL:		http://aria2.sourceforge.net/
Source0:	http://downloads.sourceforge.net/aria2/%name-%{version}.tar.xz
BuildRequires:	bison
Buildrequires:	libxml2-devel
BuildRequires:	gnutls-devel
BuildRequires:	c-ares-devel
BuildRequires:	sqlite3-devel
BuildRequires:	cppunit-devel
Requires:	rootcerts
#we need 1.7.0 to have ares_library_init available
Requires:	c-ares >= 1.7.0
Provides:	webfetch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Aria2 has segmented downloading engine in its core. It can download one 
file from multiple URLs or multiple connections from one URL. This results
in very high speed downloading, very much faster than ordinary browsers.
This engine is implemented with a single-thread model.
It can also download BitTorrent files and supports Metalink version 3.0.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -Os"
export CXXFLAGS=$CFLAGS

%configure2_5x \
	--with-ca-bundle="%{_sysconfdir}/pki/tls/cert.pem" \
	--enable-bittorrent \
	--enable-metalink \
	--enable-epoll \
	--enable-threads=posix \
	--disable-rpath \
	--with-gnutls \
	--without-openssl \
	--with-sqlite3 \
	--with-libxml2 \
	--without-libexpat \
	--with-libcares \
	--with-libz

%make

# (tpg) disable checks on x86, on x86_64 all of them passes without any failures
%ifnarch x86
%check
make check
%endif

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS README NEWS
%doc %{_docdir}/%{name}/*
%{_bindir}/*
%{_mandir}/man1/*
