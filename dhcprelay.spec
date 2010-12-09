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


