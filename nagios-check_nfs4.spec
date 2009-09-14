Name:		nagios-check_nfs4
Version:	0.2
Release:	%mkrel 3
Summary:	NFSv4 monitoring for clients and servers
License:	GPL
Group:		Networking/Other
URL:		http://www.nagiosexchange.org/cgi-bin/page.cgi?g=2070.html;d=1
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
