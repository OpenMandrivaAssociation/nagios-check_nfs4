Name:		nagios-check_nfs4
Version:	0.2
Release:	5
Summary:	NFSv4 monitoring for clients and servers
License:	GPL
Group:		Networking/Other
URL:		https://www.nagiosexchange.org/cgi-bin/page.cgi?g=2070.html;d=1
Source:     check_nfs4.%{version}.pl
Requires:	nagios-plugins
BuildArch:  noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This plugin checks NFSv4 daemons status (client and server) including nfsd,
idmapd, mountd and svcgssd.
It also displays information about performances and errors. 

%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/nagios/plugins
install -m 755 %{SOURCE0} %{buildroot}%{_datadir}/nagios/plugins/check_nfs4.pl

perl -pi -e 's|/usr/local/nagios/libexec|%{_datadir}/nagios|' \
    %{buildroot}%{_datadir}/nagios/plugins/check_nfs4.pl

install -d -m 755 %{buildroot}%{_sysconfdir}/nagios/plugins.d
cat > %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_nfs4.cfg <<'EOF'
define command {
	command_name    check_nfs4
	command_line    %{_datadir}/nagios/plugins/check_nfs4.pl
}
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_nfs4.cfg
%{_datadir}/nagios/plugins/check_nfs4.pl


%changelog
* Sat Dec 11 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-4mdv2011.0
+ Revision: 620462
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.2-3mdv2010.0
+ Revision: 440225
- rebuild

* Sun Dec 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.2-2mdv2009.1
+ Revision: 317111
- fix configuration
- import nagios-check_nfs4


