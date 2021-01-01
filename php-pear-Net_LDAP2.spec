%define		_class		Net
%define		_subclass	LDAP2
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	2.2.0
Release:	1
Summary:	OO interface for searching and manipulating LDAP-entries
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Net_LDAP2
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch

%description
%{upstream_name} is a clone of Perl's Net::LDAP object interface to
ldapservers. It does not contain all of Net::LDAP features (ldif
handling, schemas, etc), but has:
- a simple OO interface to connections, searches and entries
- support for TLS and ldap v3
- simple modification, deletion and creation of ldapentries

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/doc/*
%{_datadir}/pear/doc/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
%{_datadir}/pear/test/Net_LDAP2/tests/*


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.12-2mdv2012.0
+ Revision: 742155
- fix major breakage by careless packager

* Mon Nov 28 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.12-1
+ Revision: 735174
- new version

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.11-2
+ Revision: 679458
- mass rebuild

* Sat Feb 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.11-1
+ Revision: 636090
- update to new version 2.0.11

* Wed Aug 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.10-1mdv2011.0
+ Revision: 573125
- update to new version 2.0.10

* Sun Feb 21 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.9-1mdv2010.1
+ Revision: 508991
- update to new version 2.0.9

* Thu Jan 21 2010 Adam Williamson <awilliamson@mandriva.org> 2.0.7-2mdv2010.1
+ Revision: 494703
- no-change bump so I can upload to 2009.0 updates (stupid stupid bs bugs)

* Tue Dec 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.7-1mdv2010.1
+ Revision: 478813
- update to new version 2.0.7

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.6-2mdv2010.1
+ Revision: 469028
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Sun Aug 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.6-1mdv2010.0
+ Revision: 419924
- update to new version 2.0.6

* Sun Jul 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.5-1mdv2010.0
+ Revision: 400320
- update to new version 2.0.5

* Thu Jul 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.4-1mdv2010.0
+ Revision: 393770
- import php-pear-Net_LDAP2


* Thu Jul 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.4-1mdv2010.0
- first mdv release
