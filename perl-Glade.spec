%include	/usr/lib/rpm/macros.perl
%define		pdir	Glade
%define		pnam	Perl
Summary:	-
Summary(cs):	-
Summary(da):	-
Summary(de):	-
Summary(es):	-
Summary(fr):	-
Summary(it):	-
Summary(ja):	-
Summary(no):	-
Summary(pl):	-
Summary(pt):	-
Summary(pt_BR):	-
Summary(ru):	-
Summary(sl):	-
Summary(sv):	-
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

%description -l pl

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
