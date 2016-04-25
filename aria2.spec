Summary:	Download utility with resuming and segmented downloading
Name:		aria2
Version:	1.22.0
Release:	1
License:	GPLv2+
Group:		Networking/File transfer
Url:		http://aria2.sourceforge.net/
Source0:	http://downloads.sourceforge.net/aria2/%{name}-%{version}.tar.xz


BuildRequires:	bison
BuildRequires:	pkgconfig(cppunit)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libcares)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libuv)
BuildRequires:	pkgconfig(sqlite3)
Requires:	rootcerts
Provides:	webfetch

%description
Aria2 has segmented downloading engine in its core. It can download one 
file from multiple URLs or multiple connections from one URL. This results
in very high speed downloading, very much faster than ordinary browsers.
This engine is implemented with a single-thread model.
It can also download BitTorrent files and supports Metalink version 3.0.

%prep
%setup -q

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
	--with-sqlite3 \
	--with-libxml2 \
	--without-libexpat \
	--with-libcares \
	--with-libz

%make

# (tpg) disable checks on x86, on x86_64 all of them passes without any failures
%ifnarch %{ix86}
%check
make check
%endif

%install
%makeinstall_std

%find_lang %{name} --all-name --with-man

%files -f %{name}.lang
%doc AUTHORS README NEWS
%{_bindir}/*
%{_mandir}/man1/*
