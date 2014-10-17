Name: sshguard
Version: 1.5
Release: 5%{?dist}
# The entire source code is BSD 
# except src/parser/* witch is GPLv2+ 
# except src/hash_32a.c witch is Public Domain
License: BSD and GPLv2+ and Public Domain
Group: System Environment/Shells
Summary: Protect hosts from brute force attacks against ssh
Url: http://sshguard.sourceforge.net
Source0: http://downloads.sourceforge.net/sshguard/%{name}-%{version}.tar.bz2
Source1: systemd.sshguard.service
Source2: sysconfig.sshguard
Source3: sshguard.init
Requires: iptables
Requires: openssh-server
%if 0%{?fedora} >= 16
BuildRequires: systemd-units
%endif

%description
Sshguard protects networked hosts from brute force attacks
against ssh servers. It detects such attacks and blocks the
attacker's address with a firewall rule.

%prep
%setup -q

%build
%{configure} --with-firewall=iptables
make %{?_smp_mflags} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
make install-strip DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_unitdir} $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig $RPM_BUILD_ROOT/%{_libexecdir} $RPM_BUILD_ROOT/%{_initrddir}
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/sshguard
%if 0%{?fedora} >= 16
   install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{_unitdir}/sshguard.service
   install -m 755 %{SOURCE3} $RPM_BUILD_ROOT/%{_libexecdir}/sshguard.init
%else
   install -m 755 %{SOURCE3} $RPM_BUILD_ROOT/%{_initrddir}/sshguard
%endif 

%post
if [ $1 -eq 1 ] ; then 
    # Initial installation 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable sshguard.service > /dev/null 2>&1 || :
    /bin/systemctl stop sshguard.service > /dev/null 2>&1 || :
fi

%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart sshguard.service >/dev/null 2>&1 || :
fi

%files
%doc Changes README
%config(noreplace) %{_sysconfdir}/sysconfig/sshguard
%if 0%{?fedora} >= 16
   %{_unitdir}/sshguard.service
   %{_libexecdir}/sshguard.init
%else
   %{_initrddir}/sshguard
%endif
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}*

%changelog
* Wed Oct 15 2014 Ryan Schlesinger ryan@aceofsales.com 1.5-5.amzn1
- Removed Log Validation as using it with the Log Sucker is discouraged

* Tue Aug 16 2012 Sebastien Caps sebastien.caps@guardis.com 1.5-4.fc16
- Fix multi licensed files 

* Tue Aug 16 2012 Sebastien Caps sebastien.caps@guardis.com 1.5-3.fc16
- Added systemd script,
- correct license.

* Tue Aug 14 2012 Sebastien Caps sebastien.caps@guardis.com 1.5-2.fc16
- Fix some spec issue.

* Tue Aug 14 2012 Sebastien Caps sebastien.caps@guardis.com 1.5-1.fc16
- Rebuilt for RedHat based distro.

* Wed Mar 02 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.5-1mdv2011.0
+ Revision: 641382
- update to new version 1.5

* Sat Sep 26 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4-1mdv2010.0
+ Revision: 449478
- update to new version 1.4

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 1.3-2mdv2010.0
+ Revision: 445231
- rebuild

* Sun Oct 12 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3-1mdv2009.1
+ Revision: 293010
- update to new version 1.3
- update to new version 1.3
- update to new version 1.2

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.1-0.beta3.1mdv2009.0
+ Revision: 140851
- restore BuildRoot

+ Thierry Vignaud <tv@mandriva.org>
- kill re-definition of %%buildroot on Pixel's request

* Fri Oct 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1-0.beta3.1mdv2008.1
+ Revision: 102372
- new version

* Tue May 22 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-0.beta2.2mdv2008.0
+ Revision: 29621
- fix group

* Tue May 22 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-0.beta2.1mdv2008.0
+ Revision: 29613
- Import sshguard
