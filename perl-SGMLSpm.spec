Name:        	perl-SGMLSpm
Version:     	1.03ii
Release:     	%mkrel 16
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



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.03ii-16mdv2012.0
+ Revision: 765642
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.03ii-15
+ Revision: 764154
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.03ii-14
+ Revision: 667303
- mass rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.03ii-13mdv2011.0
+ Revision: 426587
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.03ii-12mdv2009.1
+ Revision: 351747
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.03ii-11mdv2009.0
+ Revision: 224052
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.03ii-10mdv2008.1
+ Revision: 180548
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 1.03ii-9mdv2008.0
+ Revision: 23319
- rebuild


* Tue Mar 21 2006 Camille Begnis <camille@mandriva.com> 1.03ii-8mdk
- rebuild

* Tue Oct 26 2004 Camille Begnis <camille@mandrakesoft.com> 1.03ii-7mdk
- Rebuild

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.03ii-6mdk
- rebuild for new perl
- quiet setup
- rm -rf $RPM_BUILD_ROOT at the beginning of %%install

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.03ii-5mdk
- rebuild for new auto{prov,req}

