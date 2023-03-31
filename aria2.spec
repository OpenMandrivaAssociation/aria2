# (tpg) optimize it a bit
%global optflags %{optflags} -Oz --rtlib=compiler-rt

Summary:	Download utility with resuming and segmented downloading
Name:		aria2
Version:	1.36.0
Release:	4
License:	GPLv2+
Group:		Networking/File transfer
Url:		http://aria2.sourceforge.net/
Source0:	https://github.com/aria2/aria2/releases/download/release-%{version}/aria2-%{version}.tar.xz
BuildRequires:	bison
BuildRequires:	pkgconfig(gmp)
BuildRequires:	pkgconfig(libnsl)
BuildRequires:	pkgconfig(libssh2)
BuildRequires:	pkgconfig(cppunit)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(libcares)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(libuv)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(zlib)
Requires:	rootcerts
Provides:	webfetch

%description
Aria2 has segmented downloading engine in its core. It can download one 
file from multiple URLs or multiple connections from one URL. This results
in very high speed downloading, very much faster than ordinary browsers.
This engine is implemented with a single-thread model.
It can also download BitTorrent files and supports Metalink version 3.0.

%package doc
Summary:	Documentation for %{name}
Group:		Networking/File transfer
BuildArch:	noarch

%description doc
This package contains the documentation for %{name}.

%prep
%autosetup -p1

%build
%configure \
	--with-ca-bundle="%{_sysconfdir}/pki/tls/cert.pem" \
	--enable-bittorrent \
	--enable-metalink \
	--enable-epoll \
	--with-libuv \
	--enable-threads=posix \
	--with-gnutls \
	--without-openssl \
	--without-libnettle \
	--with-libgcrypt \
	--with-sqlite3 \
	--without-libxml2 \
	--with-libexpat \
	--with-libcares \
	--with-libz

%make_build

%install
%make_install

%find_lang %{name} --all-name --with-man

%files -f %{name}.lang
%{_bindir}/*
%doc %{_mandir}/man1/*

%files doc
%doc %{_docdir}/%{name}
