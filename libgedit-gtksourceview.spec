%global api_ver		300
%global major		1

%define libname		%mklibname gedit-gtksourceview %{api_ver} %{major}
%define girname		%mklibname gedit-gtksourceview-gir %{api_ver}
%define devname		%mklibname gedit-gtksourceview %{api_ver} -d

Name:		libgedit-gtksourceview
Version:	299.2.1
Release:	1
Summary:	Gedit source code editing widget
Group:		Graphical desktop/GNOME
License:	LGPLv2+
URL:		https://github.com/gedit-technology/libgedit-gtksourceview
Source0:	https://gedit-technology.net/tarballs/libgedit-gtksourceview/libgedit-gtksourceview-%{version}.tar.xz

BuildRequires:	meson
BuildRequires:	gettext
BuildRequires:	gi-docgen
BuildRequires:	itstool
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(libpcre2-8)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(pangoft2)
BuildRequires:	pkgconfig(sysprof-capture-4)
BuildRequires:	pkgconfig(vapigen)
#
Requires:	glib2.0-common%{?_isa}

%description
libgedit-gtksourceview is a library that extends GtkTextView, the
standard GTK widget for multiline text editing. This library adds
support for syntax highlighting, undo/redo, file loading and saving,
search and replace, a completion system, printing, displaying line
numbers, and other features typical of a source code editor.

This package contains version %{api_ver} of libgedit-gtksourceview.

%package -n %{libname}
Summary:	Gedit source code editing widget library
Group:		Editors
Requires:	%{name} >= %{version}-%{release}
Obsoletes:	%{_lib}libgedit-gtksourceview300_0 < 299.0.4-2

%description	-n %{libname}
libgedit-gtksourceview is a library that extends GtkTextView, the
standard GTK widget for multiline text editing. This library adds
support for syntax highlighting, undo/redo, file loading and saving,
search and replace, a completion system, printing, displaying line
numbers, and other features typical of a source code editor.

%package	-n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{_lib}libgedit-gtksourceview-gir300 < 299.0.4-2

%description	-n %{girname}
GObject Introspection interface description for %{name}.

%package	-n %{devname}
Summary:	Development files for %{name}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	gedit-gtksourceview-devel = %{version}-%{release}
Obsoletes:	%{_lib}libgedit-gtksourceview300-devel < 299.0.4-2

%description	-n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang libgedit-gtksourceview-%{api_ver}

%files -f libgedit-gtksourceview-%{api_ver}.lang
%license COPYING
%doc HACKING NEWS
%{_datadir}/libgedit-gtksourceview-%{api_ver}/

%files -n %{girname}
%license COPYING
%{_libdir}/girepository-1.0/GtkSource-%{api_ver}.typelib

%files -n %{libname}
%license COPYING
%doc HACKING NEWS 
%{_libdir}/libgedit-gtksourceview-%{api_ver}.so.%{major}{,.*}

%files -n %{devname}
%{_docdir}/libgedit-gtksourceview
%{_datadir}/gtk-doc/html/libgedit-gtksourceview-%{api_ver}/
%{_includedir}/libgedit-gtksourceview-%{api_ver}/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libgedit-gtksourceview-%{api_ver}.so
%{_datadir}/gir-1.0/GtkSource-%{api_ver}.gir
