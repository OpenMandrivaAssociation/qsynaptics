%define name qsynaptics
%define version 0.22.0

Summary:	A QT application to configure Synaptic TouchPad
Name:		%{name}
Version:	%{version}
Release:	%mkrel 8
License:	GPL
Url:		http://qsynaptics.sourceforge.net/
Group:		System/Configuration/Hardware
Source:		http://prdownloads.sourceforge.net/qsynaptics/%{name}/%{name}-%{version}.tar.bz2
Source11:	mmouse.png
Source12:	mouse.png
Source13:	lmouse.png
Patch1: qsynaptics-0.22-stdlib-for-exit.patch
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
MimeType=foo/bar;foo2/bar2;
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
