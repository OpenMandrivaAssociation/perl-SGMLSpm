Summary:     	Perl library for parsing the output of nsgmls
Name:        	perl-SGMLSpm
Version:     	1.1
Epoch:		1
Release:     	1
Group:       	Publishing
License:   	GPLv2
Url:         	http://search.cpan.org/dist/SGMLSpm/
Source0:	http://search.cpan.org/CPAN/authors/id/R/RA/RAAB/SGMLSpm-%{version}.tar.gz
BuildArch:	noarch
Requires:    	openjade >= 1.2.1
Requires:	perl

%description
Perl programs can use the SGMLSpm module to help convert SGML, HTML or XML
documents into new formats.

%prep
%setup -q -n SGMLSpm-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%install
%make_install

%files 
%doc BUGS COPYING ChangeLog DOC/ README TODO elisp
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man3/*
