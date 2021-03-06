%define		pdir	Glade
%define		pnam	Perl
Summary:	Perl module to generate Gtk-Perl apps from a Glade file
Summary(pl.UTF-8):	Moduł Perla generujący aplikacje Gtk-Perl na bazie pliku Glade
Name:		perl-Glade
Version:	0.61
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	13159e67d1a91bf912b4ffea2975cd1a
URL:		http://www.gtkperl.org/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-gnome
BuildRequires:	perl-gtk
BuildRequires:	perl-Unicode-String
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glade-Perl will read a Glade-Interface XML file, build the UI and/or
write the perl source to create the UI later and handle signals. It
also creates an 'App' and a 'Subclass' that you can edit.

Glade-Perl can generate AUTOLOAD type OO code with subclasses or even
Libglade apps.

%description -l pl.UTF-8
Glade-Perl czyta plik XML z opisem interfejsu Glade, tworzy UI i/lub
zapisuje perlowe źródła później tworzące UI i obsługujące sygnały.
Tworzy także 'App' i 'Subclass', które można modyfikować.

Glade-Perl może generować kod obiektowy typu AUTOLOAD z podklasami lub
nawet aplikacjami Libglade.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}
%{_mandir}/man*/*
%attr(755,root,root) %{_bindir}/glade2perl
