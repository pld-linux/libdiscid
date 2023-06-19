Summary:	Library for creating MusicBrainz DiscIDs
Summary(pl.UTF-8):	Biblioteka do tworzenia identyfikatorów DiscID dla MusicBrainz
Name:		libdiscid
Version:	0.6.4
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.musicbrainz.org/pub/musicbrainz/libdiscid/%{name}-%{version}.tar.gz
# Source0-md5:	774afc1c6eddad9c6db91efd35111d1b
URL:		http://musicbrainz.org/doc/libdiscid
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine		__cxx

%description
libdiscid is a C library for creating MusicBrainz DiscIDs from audio
CDs. It reads a CD's table of contents (TOC) and generates an
identifier which can be used to lookup the CD at MusicBrainz.
Additionally, it provides a submission URL for adding the DiscID to
the database.

%description -l pl.UTF-8
libdiscid to biblioteka C do tworzenia identyfikatorów DiscID dla
MusicBrainz z płyt CD Audio. Odczytuje tablicę zawartości płyty (TOC)
i generuje identyfikator, który można wykorzystywać do wyszukiwania
płyty w bazie MusicBrainz. Ponadto podaje URL do dodawania DiscID do
bazy danych.

%package devel
Summary:	Header files for discid library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki discid
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for discid library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki discid.

%package static
Summary:	Static discid library
Summary(pl.UTF-8):	Statyczna biblioteka discid
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static discid library.

%description static -l pl.UTF-8
Statyczna biblioteka discid.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no external dependencies, obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libdiscid.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libdiscid.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdiscid.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdiscid.so
%{_includedir}/discid
%{_pkgconfigdir}/libdiscid.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libdiscid.a
