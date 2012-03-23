Summary:	Download utility with resuming and segmented downloading
Name:		aria2
Version:	1.14.2
Release:	2
License:	GPLv2+
Group:		Networking/File transfer
URL:		http://aria2.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/aria2/stable/%{name}-%{version}/%{name}-%{version}.tar.xz
Patch0:		aria2-1.14.0-flush-output-after-printing-progress.patch
BuildRequires:	bison
Buildrequires:	libxml2-devel
BuildRequires:	gnutls-devel >= 3.0
BuildRequires:	c-ares-devel
BuildRequires:	sqlite3-devel
BuildRequires:	cppunit-devel
BuildRequires:	libgcrypt-devel
Requires:	rootcerts
#we need 1.7.0 to have ares_library_init available
Requires:	c-ares >= 1.7.0
Provides:	webfetch
# aria2 uses functions not available in older zlib versions, so add a conflict
# to avoid any possible issues caused by this during upgrades
Conflicts:	zlib1 < 1.2.5

%description
Aria2 has segmented downloading engine in its core. It can download one 
file from multiple URLs or multiple connections from one URL. This results
in very high speed downloading, very much faster than ordinary browsers.
This engine is implemented with a single-thread model.
It can also download BitTorrent files and supports Metalink version 3.0.

%prep
%setup -q
%patch0 -p1 -b .flush~

%build
export CFLAGS="%{optflags} -Os"
export CXXFLAGS="$CFLAGS"

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
%ifnarch %{ix86}
%check
make check
%endif

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README NEWS
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/ru/man1/aria2c.1.*
