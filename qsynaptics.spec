%define name qsynaptics
%define version 0.22.0

Summary:	A QT application to configure Synaptic TouchPad
Name:		%{name}
Version:	%{version}
Release:	16
License:	GPL
Url:		http://qsynaptics.sourceforge.net/
Group:		System/Configuration/Hardware
Source:		http://prdownloads.sourceforge.net/qsynaptics/%{name}/%{name}-%{version}.tar.bz2
Source11:	mmouse.png
Source12:	mouse.png
Source13:	lmouse.png
Patch1:		qsynaptics-0.22-stdlib-for-exit.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	qt3-devel >= 3.2
Requires:	synaptics

%description
QSynaptics aims to help desktop users to configure their synaptics touch pad
that's commonly used in laptops.  The program uses Qt 3.2, is easy to manage
and performs the basic configuration steps to use your pad more efficiently.
The program is based on the X11 synaptics touch pad driver.

%prep
%setup -q
%patch1 -p1

%build
export PATH=%{_prefix}/lib/qt3/bin:$PATH
export QTDIR=%{_prefix}/lib/qt3
cd src
qmake
%make

%install
mkdir -p %{buildroot}/usr/bin
install bin/%{name} %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=Qsynaptics
Comment=A QT application to configure Synaptics TouchPad
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Qt;Utility;Settings;HardwareSettings;X-MandrivaLinux-System-Configuration-Hardware;
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png

mkdir -p %{buildroot}/%{_sysconfdir}/X11/xinit.d
cat > %{buildroot}/%{_sysconfdir}/X11/xinit.d/qsynaptics <<EOF
#!/bin/sh
[ -s ~/.qsynaptics ] && %{_bindir}/qsynaptics -r >/dev/null 2>&1
EOF

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif
 
%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%files
%defattr(644,root,root, 755)
%doc README AUTHORS ChangeLog TODO COPYING 
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %config(noreplace) %{_sysconfdir}/X11/xinit.d/qsynaptics
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.22.0-12mdv2011.0
+ Revision: 669383
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.22.0-11mdv2011.0
+ Revision: 607263
- rebuild

* Thu Mar 18 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.22.0-9mdv2010.1
+ Revision: 524904
- fix .desktop file, it doesn't need a MimeType

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.22.0-8mdv2010.1
+ Revision: 523884
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.22.0-7mdv2010.0
+ Revision: 426806
- rebuild

* Thu Apr 23 2009 Colin Guthrie <cguthrie@mandriva.org> 0.22.0-6mdv2009.1
+ Revision: 368832
- Drop SHM patch. Using device properties should now work with newer synaptics.

* Sat Apr 18 2009 Colin Guthrie <cguthrie@mandriva.org> 0.22.0-5mdv2009.1
+ Revision: 367979
- Update to work with new synaptics driver by using synclient -s

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.22.0-4mdv2008.1
+ Revision: 179406
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Thu Jun 14 2007 Adam Williamson <awilliamson@mandriva.org> 0.22.0-3mdv2008.0
+ Revision: 39249
- XDG menu, fd.o icons; rebuild for new era
- Import qsynaptics



* Sat Apr 15 2006 Luca Berra <bluca@vodka.it> 0.22.0-2mdk
- rebuild
- use %%mkrel

* Thu Mar 15 2005 Nicolas Brouard <nicolas.brouard@mandrake.org> 0.22.0-1mdk
- 0.22.0-1mdk
* Sun Aug 08 2004 Luca Berra <bluca@vodka.it> 0.21-1mdk 
- Initial mandrake contrib (started from an rpm by Arnaud Quette)
