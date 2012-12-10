Summary:	A dhcp relay to implement dhcp over ipsec
Name:		dhcprelay
Version:	0.3.2b
Release:	%mkrel 5
License:	GPL
Group:		System/Servers
URL:		http://www.strongsec.com/freeswan/dhcprelay/
Source0:	http://www.strongsec.com/freeswan/dhcprelay/dhcprelay-%{version}.tar.bz2
BuildRequires:	gmp-devel
Requires(preun):rpm-helper
Requires(post):	rpm-helper	
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
This DHCP-Relay forwards any DHCP packet out of a list of given ipsec devices
to the DHCP server of a network and returns the response. If no DHCP server is
given the packets are sent by broadcast.

%prep

%setup -q 

%build
%configure
%make

%install
rm -rf %{buildroot}
#%makeinstall_std

install -d %{buildroot}{%{_sysconfdir},/etc/rc.d/init.d,/usr/sbin}
install -m 755 src/dhcprelay %{buildroot}/usr/sbin 
install -m 755 init.d/dhcprelay %{buildroot}/etc/rc.d/init.d
install -m 644 etc/dhcprelay.conf %{buildroot}/etc

%post
%_post_service dhcprelay

%preun
%_preun_service dhcprelay

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,755)
%doc AUTHORS README INSTALL COPYING ChangeLog howto/*
%config(noreplace) %{_sysconfdir}/dhcprelay.conf
%{_initrddir}/dhcprelay
%{_sbindir}/dhcprelay




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.2b-5mdv2011.0
+ Revision: 617582
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.3.2b-4mdv2010.0
+ Revision: 427963
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.3.2b-3mdv2009.0
+ Revision: 244090
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.3.2b-1mdv2008.1
+ Revision: 136362
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Dec 12 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.2b-1mdv2007.0
+ Revision: 95897
- Import dhcprelay

* Tue Dec 12 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.2b-1mdv2007.1
- 0.3.2b
- fix deps
- use the %%mkrel macro

* Wed Oct 27 2004 Florin <florin@mandrakesoft.com> 0.3.1-1mdk
- first Mandrake release

