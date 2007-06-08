%define name qsynaptics
%define version 0.22.0
%define release %mkrel 2

Summary:	A QT application to configure Synaptic TouchPad
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Url:		http://qsynaptics.sourceforge.net/
Group:		System/Configuration/Hardware
Source:		http://prdownloads.sourceforge.net/qsynaptics/%{name}/%{name}-%{version}.tar.bz2
Source11:	mmouse.png
Source12:	mouse.png
Source13:	lmouse.png
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

%build
cd src
qmake
%make

%install
mkdir -p %{buildroot}/usr/bin
install bin/%{name} %{buildroot}%{_bindir}

mkdir -p %{buildroot}/%{_menudir}
cat > %buildroot/%_menudir/%{name} <<EOF
?package(%{name}): \
	command="%{name}" \
	icon="%{name}.png" \
	needs="x11" \
	title="Synaptics TouchPad" \
	longtitle="A QT application to configure Synaptics TouchPad" \
	section="System/Configuration/Hardware"
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

mkdir -p %{buildroot}/%{_sysconfdir}/X11/xinit.d
cat > %{buildroot}/%{_sysconfdir}/X11/xinit.d/qsynaptics <<EOF
#!/bin/sh
[ -s ~/.qsynaptics ] && %{_bindir}/qsynaptics -r >/dev/null 2>&1
EOF

%clean
rm -rf %{buildroot}

%post
%update_menus
 
%postun
%clean_menus

%files
%defattr(644,root,root, 755)
%doc README AUTHORS ChangeLog TODO COPYING 
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %config(noreplace) %{_sysconfdir}/X11/xinit.d/qsynaptics
%{_menudir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
