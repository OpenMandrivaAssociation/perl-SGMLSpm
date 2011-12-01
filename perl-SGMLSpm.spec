Name:        	perl-SGMLSpm
Version:     	1.03ii
Release:     	%mkrel 14
Group:       	Publishing
Summary:     	Perl library for parsing the output of nsgmls
License:   	GPL
URL:         	http://www.uottawa.ca/~dmeggins
Requires:    	jade >= 1.2.1
Requires:	perl
Buildroot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
Source0:	ftp://cpan.perl.org/pub/perl/CPAN/modules/by-module/SGMLS/SGMLSpm-%{version}.tar.bz2

%description
Perl programs can use the SGMLSpm module to help convert SGML, HTML or XML
documents into new formats.

%prep
%setup -q -n SGMLSpm
find -type d | xargs chmod a+rx
find -type f | xargs chmod a+r

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{perl_vendorlib}
make install_system BINDIR=%{buildroot}%{_bindir} PERL5DIR=%{buildroot}%{perl_vendorlib}

%clean
rm -rf %{buildroot} 

%files 
%defattr (-,root,root)  
%doc BUGS COPYING ChangeLog DOC/ README TODO elisp
%{_bindir}/*
%{perl_vendorlib}/*

