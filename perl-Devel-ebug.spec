#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	ebug
Summary:	Devel::ebug - A simple, extensible Perl debugger
Summary(pl.UTF-8):	Devel::ebug - prosty, rozszerzalny debugger dla Perla
Name:		perl-Devel-ebug
Version:	0.52
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	057c4a72c959bdd9f87da3f9372a4ff1
URL:		http://search.cpan.org/dist/Devel-ebug/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Proc-Background
BuildRequires:	perl-String-Koremutake
BuildRequires:	perl-Test-Expect
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A debugger is a computer program that is used to debug other
programs. Devel::ebug is a simple, extensible Perl debugger with a
clean API. Using this module, you may easily write a Perl debugger to
debug your programs. Alternatively, it comes with an interactive
debugger, ebug.

%description -l pl.UTF-8
Debugger to program służący do śledzenia innych programów. Devel::ebug
to prosty, rozszerzalny debugger dla Perla z czystym API. Przy użyciu
tego modułu można łatwo napisać debugger perlowy do śledzenia własnych
programów. Ewentualnie użyć interaktywnego debuggera ebug
dostarczonego z pakietem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Devel/*.pm
%{perl_vendorlib}/Devel/ebug
%{_mandir}/man[13]/*
