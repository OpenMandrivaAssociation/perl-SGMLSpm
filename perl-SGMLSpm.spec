Summary:     	Perl library for parsing the output of nsgmls
Name:        	perl-SGMLSpm
Version:     	1.03ii
Release:     	27
Group:       	Publishing
License:   	GPLv2
Url:         	http://www.uottawa.ca/~dmeggins
Source0:	ftp://cpan.perl.org/pub/perl/CPAN/modules/by-module/SGMLS/SGMLSpm-%{version}.tar.bz2
BuildArch:	noarch
Requires:    	openjade >= 1.2.1
Requires:	perl

%description
Perl programs can use the SGMLSpm module to help convert SGML, HTML or XML
documents into new formats.

%prep
%setup -q -n SGMLSpm
find -type d | xargs chmod a+rx
find -type f | xargs chmod a+r

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{perl_vendorlib}
make install_system BINDIR=%{buildroot}%{_bindir} PERL5DIR=%{buildroot}%{perl_vendorlib}

%files 
%doc BUGS COPYING ChangeLog DOC/ README TODO elisp
%{_bindir}/*
%{perl_vendorlib}/*

