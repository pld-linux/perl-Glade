%include	/usr/lib/rpm/macros.perl
%define		pdir	Glade
%define		pnam	Perl
Summary:	Perl module to generate Gtk-Perl apps from a Glade file
Summary(pl):	Modu³ Perla generuj±cy aplikacje Gtk-Perl na bazie pliku Glade
Name:		perl-Glade
Version:	0.61
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	13159e67d1a91bf912b4ffea2975cd1a
URL:		http://www.gtkperl.org/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	perl-devel >= 5.005_03-10
BuildRequires:	rpm-perlprov
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-gtk
BuildRequires:	perl-gnome
BuildRequires:	perl-Unicode-String

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glade-Perl will read a Glade-Interface XML file, build the UI and/or
write the perl source to create the UI later and handle signals. It
also creates an 'App' and a 'Subclass' that you can edit.

Glade-Perl can generate AUTOLOAD type OO code with subclasses or even
Libglade apps.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorarch}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}
%{_mandir}/man*/*
%{_bindir}/glade2perl
