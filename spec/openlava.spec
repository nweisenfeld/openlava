#
# Copyright (C) 2007 Platform Computing Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of version 2 of the GNU General Public License as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA
#
#

%define major 2
%define minor 0
%define release 1

%define version %{major}.%{minor}
%define _openlavatop /opt/openlava-%{version}
%define _clustername openlava
%define _libdir %{_openlavatop}/lib
%define _bindir %{_openlavatop}/bin
%define _sbindir %{_openlavatop}/sbin
%define _sharedir %{_openlavatop}/share
%define _mandir %{_sharedir}/man
%define _logdir %{_openlavatop}/log
%define _includedir %{_openlavatop}/include
%define _etcdir %{_openlavatop}/etc-template
%define _workdir %{_openlavatop}/work
# the following will be symlinked to %{_openlavatop}/etc
%define _etcdirsh /wga/scr4/openlava/etc

Summary: openlava Distributed Batch Scheduler (Broad COMPRD MODIFIED)
Name: openlava-broad-comprd
Version: 2.0
Release: 1comprd
License: GPLv2
Group: Applications/Productivity
Vendor: openlava foundation
ExclusiveArch: x86_64
URL: http://www.openlava.net/
Source: %{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: gcc, tcl-devel, ncurses-devel
Requires: ncurses, tcl
%if 0%{?suse_version}
PreReq: %insserv_prereq
Requires(pre): pwdutils
%else
Requires(pre): /usr/sbin/useradd
Requires(pre): /usr/sbin/groupadd
%endif
Requires(pre): /usr/bin/getent
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Prefix: /opt

%description
openlava Distributed Batch Scheduler

#
# PREP
#
%prep
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

%setup -q -n %{name}-%{version}

#
# BUILD
#
%build
./bootstrap.sh
make

#
# CLEAN
#
%clean
/bin/rm -rf $RPM_BUILD_ROOT

#
# INSTALL
#
%install

# install directories and files
install -d $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -d $RPM_BUILD_ROOT%{_sysconfdir}/init.d
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_etcdir}
install -d $RPM_BUILD_ROOT%{_includedir}
install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_logdir}
install -d $RPM_BUILD_ROOT%{_sbindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -d $RPM_BUILD_ROOT%{_mandir}/man3
install -d $RPM_BUILD_ROOT%{_mandir}/man5
install -d $RPM_BUILD_ROOT%{_mandir}/man8
install -d $RPM_BUILD_ROOT%{_workdir}/logdir

# in openlava root
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/COPYING  $RPM_BUILD_ROOT%{_openlavatop}
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/README  $RPM_BUILD_ROOT%{_openlavatop}

# bin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/badmin  $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bbot    $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/bhist/bhist   $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bhosts  $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bjobs   $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bkill   $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bmgroup $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bmig    $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bmod    $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bparams $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bpeek   $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bqueues $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/brequeue $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/brestart $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/brun     $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bsub     $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/bswitch  $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/btop     $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/cmd/busers   $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/scripts/lam-mpirun $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lsacct     $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lsadm/lsadmin    $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lseligible $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lshosts    $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lsid       $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lsinfo     $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lsload     $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lsloadadj  $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lsmon      $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lsplace    $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lsrcp      $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lsrun      $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lsaddhost  $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lstools/lsrmhost   $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/scripts/mpich2-mpiexec $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/scripts/mpich-mpirun   $RPM_BUILD_ROOT%{_bindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/scripts/openmpi-mpirun $RPM_BUILD_ROOT%{_bindir}

# etc
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/config/lsf.cluster.openlava $RPM_BUILD_ROOT%{_etcdir}
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/config/lsf.conf $RPM_BUILD_ROOT%{_etcdir}
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/config/lsf.task $RPM_BUILD_ROOT%{_etcdir}
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/config/lsf.shared $RPM_BUILD_ROOT%{_etcdir}
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/config/lsb.params $RPM_BUILD_ROOT%{_etcdir}
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/config/lsb.queues $RPM_BUILD_ROOT%{_etcdir}
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/config/lsb.hosts $RPM_BUILD_ROOT%{_etcdir}
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/config/lsb.users $RPM_BUILD_ROOT%{_etcdir}
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/config/openlava.setup $RPM_BUILD_ROOT%{_etcdir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/config/openlava $RPM_BUILD_ROOT%{_etcdir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/config/openlava.sh $RPM_BUILD_ROOT%{_etcdir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/config/openlava.csh $RPM_BUILD_ROOT%{_etcdir}

# include
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lsf.h $RPM_BUILD_ROOT%{_includedir}
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/lsbatch.h $RPM_BUILD_ROOT%{_includedir}

# lib
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lib/liblsf.a $RPM_BUILD_ROOT%{_libdir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/lib/liblsbatch.a  $RPM_BUILD_ROOT%{_libdir}

# sbin
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/eauth/eauth  $RPM_BUILD_ROOT%{_sbindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/lim/lim  $RPM_BUILD_ROOT%{_sbindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/daemons/mbatchd  $RPM_BUILD_ROOT%{_sbindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/res/nios  $RPM_BUILD_ROOT%{_sbindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/pim/pim  $RPM_BUILD_ROOT%{_sbindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsf/res/res $RPM_BUILD_ROOT%{_sbindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/daemons/sbatchd $RPM_BUILD_ROOT%{_sbindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/chkpnt/echkpnt          $RPM_BUILD_ROOT%{_sbindir}
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/chkpnt/erestart         $RPM_BUILD_ROOT%{_sbindir}

# share
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bbot.1    $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bchkpnt.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bhosts.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bjobs.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bkill.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bmgroup.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bmig.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bmod.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bparams.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bpeek.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bqueues.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/brequeue.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/brestart.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bresume.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bstop.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bsub.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/btop.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bugroup.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/busers.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/bswitch.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lsacct.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lseligible.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lsfbase.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man1/lsfbatch.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lsfintro.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lshosts.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lsid.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lsinfo.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lsload.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lsloadadj.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lsmon.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lsplace.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man1/lsrcp.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man5/lsb.acct.5  $RPM_BUILD_ROOT%{_mandir}/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man5/lsb.events.5 $RPM_BUILD_ROOT%{_mandir}/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man5/lsb.hosts.5 $RPM_BUILD_ROOT%{_mandir}/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man5/lsb.params.5 $RPM_BUILD_ROOT%{_mandir}/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man5/lsb.queues.5 $RPM_BUILD_ROOT%{_mandir}/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man5/lsb.users.5 $RPM_BUILD_ROOT%{_mandir}/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man5/lim.acct.5 $RPM_BUILD_ROOT%{_mandir}/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man5/lsf.acct.5 $RPM_BUILD_ROOT%{_mandir}/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man5/lsf.cluster.5 $RPM_BUILD_ROOT%{_mandir}/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man5/lsf.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man5/lsf.shared.5 $RPM_BUILD_ROOT%{_mandir}/man5
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man8/badmin.8  $RPM_BUILD_ROOT%{_mandir}/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man8/brun.8  $RPM_BUILD_ROOT%{_mandir}/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man8/eauth.8  $RPM_BUILD_ROOT%{_mandir}/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man8/eexec.8  $RPM_BUILD_ROOT%{_mandir}/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man8/esub.8  $RPM_BUILD_ROOT%{_mandir}/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man8/lim.8  $RPM_BUILD_ROOT%{_mandir}/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man8/lsadmin.8  $RPM_BUILD_ROOT%{_mandir}/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man8/lsfinstall.8  $RPM_BUILD_ROOT%{_mandir}/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man8/mbatchd.8  $RPM_BUILD_ROOT%{_mandir}/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man8/nios.8  $RPM_BUILD_ROOT%{_mandir}/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man8/pim.8  $RPM_BUILD_ROOT%{_mandir}/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsf/man/man8/res.8  $RPM_BUILD_ROOT%{_mandir}/man8
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/lsbatch/man8/sbatchd.8  $RPM_BUILD_ROOT%{_mandir}/man8

ln -sf %{_bindir}/bkill  $RPM_BUILD_ROOT%{_bindir}/bstop
ln -sf %{_bindir}/bkill  $RPM_BUILD_ROOT%{_bindir}/bresume
ln -sf %{_bindir}/bkill  $RPM_BUILD_ROOT%{_bindir}/bchkpnt
ln -sf %{_bindir}/bmgroup  $RPM_BUILD_ROOT%{_bindir}/bugroup

# comprd change to use a shared open-lava directory
ln -sf %{_etcdirsh} %{_openlavatop}/etc

install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/config/openlava.sh $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/config/openlava.csh $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -m 755 $RPM_BUILD_DIR/%{name}-%{version}/config/openlava $RPM_BUILD_ROOT%{_sysconfdir}/init.d

#
# PRE
#
%pre
#
# Add "openlava" user
#
/usr/bin/getent group openlava >/dev/null || /usr/sbin/groupadd openlava
/usr/bin/getent passwd openlava >/dev/null || /usr/sbin/useradd -c "openlava Administrator" -g openlava -m -d /home/openlava openlava 2> /dev/null || :
exit 0
#
# POST
#
%post
# Register lava daemons
%if 0%{?suse_version}
%fillup_and_insserv -f -Y openlava
%else
/sbin/chkconfig --add openlava 2>/dev/null
/sbin/chkconfig openlava on 2>/dev/null
%endif

%preun
/sbin/service openlava stop > /dev/null 2>&1

%if 0%{?suse_version} == 0
/sbin/chkconfig openlava off
/sbin/chkconfig --del openlava
%endif

%postun
%if 0%{?suse_version}
%insserv_cleanup
%endif

#
# FILES
#
%files
%defattr(-,openlava,openlava)

%{_sysconfdir}/profile.d/openlava.sh
%{_sysconfdir}/profile.d/openlava.csh
%attr(0755,openlava,openlava) %{_sysconfdir}/init.d/openlava

%{_bindir}/bstop
%{_bindir}/bresume
%{_bindir}/bchkpnt
%{_bindir}/bugroup

%attr(0755,openlava,openlava) %{_etcdir}/openlava
%{_etcdir}/openlava.sh
%{_etcdir}/openlava.csh
%{_etcdir}/openlava.setup
%{_sbindir}/eauth
%{_sbindir}/echkpnt
%{_sbindir}/erestart
%{_sbindir}/mbatchd
%{_sbindir}/sbatchd
%{_sbindir}/lim
%{_sbindir}/res
%{_sbindir}/pim
%{_sbindir}/nios
%{_bindir}/badmin
%{_bindir}/lsadmin
%{_bindir}/bbot
%{_bindir}/bhist
%{_bindir}/bhosts
%{_bindir}/bjobs
%{_bindir}/bkill
%{_bindir}/bmgroup
%{_bindir}/bmig
%{_bindir}/bmod
%{_bindir}/bparams
%{_bindir}/bpeek
%{_bindir}/bqueues
%{_bindir}/brequeue
%{_bindir}/brestart
%{_bindir}/brun
%{_bindir}/bsub
%{_bindir}/bswitch
%{_bindir}/btop
%{_bindir}/busers
%{_bindir}/lam-mpirun
%{_bindir}/mpich-mpirun
%{_bindir}/mpich2-mpiexec
%{_bindir}/openmpi-mpirun
%{_bindir}/lsacct
%{_bindir}/lseligible
%{_bindir}/lshosts
%{_bindir}/lsid
%{_bindir}/lsinfo
%{_bindir}/lsload
%{_bindir}/lsloadadj
%{_bindir}/lsmon
%{_bindir}/lsplace
%{_bindir}/lsrcp
%{_bindir}/lsrun
%{_bindir}/lsaddhost
%{_bindir}/lsrmhost

# Man pages
%{_mandir}/man1/bbot.1
%{_mandir}/man1/bchkpnt.1
%{_mandir}/man1/bhosts.1
%{_mandir}/man1/bjobs.1
%{_mandir}/man1/bkill.1
%{_mandir}/man1/bmgroup.1
%{_mandir}/man1/bmig.1
%{_mandir}/man1/bmod.1
%{_mandir}/man1/bparams.1
%{_mandir}/man1/bpeek.1
%{_mandir}/man1/bqueues.1
%{_mandir}/man1/brequeue.1
%{_mandir}/man1/brestart.1
%{_mandir}/man1/bresume.1
%{_mandir}/man1/bstop.1
%{_mandir}/man1/bsub.1
%{_mandir}/man1/btop.1
%{_mandir}/man1/bugroup.1
%{_mandir}/man1/busers.1
%{_mandir}/man1/bswitch.1
%{_mandir}/man1/lsacct.1
%{_mandir}/man1/lseligible.1
%{_mandir}/man1/lsfbase.1
%{_mandir}/man1/lsfbatch.1
%{_mandir}/man1/lsfintro.1
%{_mandir}/man1/lshosts.1
%{_mandir}/man1/lsid.1
%{_mandir}/man1/lsinfo.1
%{_mandir}/man1/lsload.1
%{_mandir}/man1/lsloadadj.1
%{_mandir}/man1/lsmon.1
%{_mandir}/man1/lsplace.1
%{_mandir}/man1/lsrcp.1
%{_mandir}/man5/lsb.acct.5
%{_mandir}/man5/lsb.events.5
%{_mandir}/man5/lsb.hosts.5
%{_mandir}/man5/lsb.params.5
%{_mandir}/man5/lsb.queues.5
%{_mandir}/man5/lsb.users.5
%{_mandir}/man8/badmin.8
%{_mandir}/man8/brun.8
%{_mandir}/man8/eauth.8
%{_mandir}/man8/eexec.8
%{_mandir}/man8/esub.8
%{_mandir}/man8/lim.8
%{_mandir}/man8/lsadmin.8
%{_mandir}/man8/lsfinstall.8
%{_mandir}/man8/mbatchd.8
%{_mandir}/man8/nios.8
%{_mandir}/man8/pim.8
%{_mandir}/man8/res.8
%{_mandir}/man8/sbatchd.8
%{_mandir}/man5/lim.acct.5
%{_mandir}/man5/lsf.acct.5
%{_mandir}/man5/lsf.cluster.5
%{_mandir}/man5/lsf.conf.5
%{_mandir}/man5/lsf.shared.5

# libraries
%{_libdir}/liblsf.a
%{_libdir}/liblsbatch.a

# headers
%{_includedir}/lsbatch.h
%{_includedir}/lsf.h

# docs
%doc COPYING

%defattr(0664,openlava,wga)
%config(noreplace) %{_etcdir}/lsb.params
%config(noreplace) %{_etcdir}/lsb.queues
%config(noreplace) %{_etcdir}/lsb.hosts
%config(noreplace) %{_etcdir}/lsb.users
%config(noreplace) %{_etcdir}/lsf.shared
%config(noreplace) %{_etcdir}/lsf.conf
%config(noreplace) %{_etcdir}/lsf.cluster.%{_clustername}
%config(noreplace) %{_etcdir}/lsf.task
%config(noreplace) %{_openlavatop}/README
%config(noreplace) %{_openlavatop}/COPYING

%attr(0755,openlava,openlava) %dir %{_openlavatop}
%attr(0755,openlava,openlava) %dir %{_bindir}
%attr(0755,openlava,openlava) %dir %{_etcdir}
%attr(0755,openlava,openlava) %dir %{_includedir}
%attr(0755,openlava,openlava) %dir %{_libdir}
%attr(0755,openlava,openlava) %dir %{_logdir}
%attr(0755,openlava,openlava) %dir %{_sbindir}
%attr(0755,openlava,openlava) %dir %{_openlavatop}/share
%attr(0755,openlava,openlava) %dir %{_openlavatop}/share/man
%attr(0755,openlava,openlava) %dir %{_openlavatop}/share/man/man1
%attr(0755,openlava,openlava) %dir %{_openlavatop}/share/man/man5
%attr(0755,openlava,openlava) %dir %{_openlavatop}/share/man/man8
%attr(0755,openlava,openlava) %dir %{_workdir}
%attr(0755,openlava,openlava) %dir %{_workdir}/logdir

%changelog
* Sun Oct 30 2011 modified the spec file so that autoconf creates
- openlava configuration files and use the outptu variables to make
- the necessary subsititution in the them. Change the post install
- to just erase the package without saving anything.
- Removed the symbolic link as that is something sites have to
- do as they may want to run more versions together, also
- in now the lsf.conf has the version in the openlava
- fundamental variables clearly indicating which version is in use.
* Sun Sep 4 2011 David Bigagli restructured to follow the new directory layout after
the GNU autoconf project.
* Thu Jul 14 2011 Robert Stober <robert@openlava.net> 1.0-1
- Enhanced support for RPM uninstall. rpm -e openlava
- will now stop the openlava daemons and then completely
- remove openlava.
- openlava configuration files and log files are saved to
- /tmp/openlava.$$.tar.gz
- Uninstallation supports shared and non-shared file system
- installations
* Sat Jul 9 2011 Robert Stober <robert@openlava.net> 1.0-1
- Added the following files so that they're installed by the RPM:
- lsb.hosts
- openmpi-mpirun
- mpich-mpirun
- lam-mpirun
- mpich2-mpiexec
- The RPM installer now uses the template files that are in the
- scripts directory instead of the standard files that are installed
- by make:
- lsf.cluster.openlava
- lsf.conf
- lsf.shared
- openlava
- openlava.csh
- openlava.sh
* Thu Jun 16 2011 Robert Stober <robert@openlava.net> 1.0-1
- Changed name of openlava startup script from "lava" to "openlava"
- Changed the name of the linux service from "lava" to openlava in
- the openlava startup script
- Changed the name of the openlava shell initialization scripts
- from lava.sh and lava.csh to openlava.sh and openlava.csh respectively.
- Changed the openlava.spec file to install the README and COPYING files.
- Added the openlava.setup script, which streamlines openlava setup
- on compute servers.
* Sat Jun 11 2011 Robert Stober <robert@openlava.net> 1.0-1
- Changed default install directory to /opt/openlava-1.0
- Installation now creates a symbolic link openlava -> openlava-1.0
- RPM is now relocatable. Specify --prefix /path/to/install/dir
- for example, rpm -ivh --prefix /opt/test openlava-1.0-1.x86_64.rpm installs
- /opt/test/openlava -> /opt/test/openlava-1.0
- Added creation of openlava user
- Changed default cluster name to "openlava"
- Added support for cstomizing the cluster name
- For example, export OPENLAVA_CLUSTER_NAME="bokisius"
- then rpm -ivh openlava-1.0-1.x86_64.rpm this will:
- 1. Set the cluster name in the lsf.shared file
- 2. renames the "clustername" directories
- The LSF binaries are now statically linked instead of being
- dynamically linked.
- Renamed /etc/init.d/lava.sh to /etc/init.d/lava
- The openlava shell initialization files lava.sh and lava.csh
- are now installed in /etc/profile.d
* Fri Apr 22 2011 Robert Stober <rmstober@gmail.com> 1.0-6.6
- Changed to install in /opt/lava
- Added support for autoconfig of various lava config files
- Removed creation of openlava user
* Fri May 30 2008 Shawn Starr <sstarr@platform.com> 1.0-6
- Fix symlinks for MVAPICH1/2.
* Tue May 27 2008 Gerry Wen <gwen@platform.com> 1.0-2
- Add wrapper script for MPICH2 mpiexec
* Mon Feb 13 2008 Shawn Starr <sstarr@platform.com> 1.0-1
- Make home directory for openlava user.
* Mon Jan 23 2008 Shawn Starr <sstarr@platform.com> 1.0-0
- Initial release of Lava 1.0
