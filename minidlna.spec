Name:		minidlna
Version:	1.2.1
Release:	1
Summary:	DLNA Server

License:	BSD
URL:		https://sourceforge.net/projects/minidlna
Source0:	%{name}-%{version}.tar.gz

%description

%Group:		Applications/Multimedia

%prep

%build


%install
tar -xvf %{_sourcedir}/%{name}-%{version}.tar.gz -C %{buildroot}

%files
/etc/systemd/system/minidlnad.service
/etc/minidlna.conf
/usr/share/locale/it/LC_MESSAGES/minidlna.mo
/usr/share/locale/ru/LC_MESSAGES/minidlna.mo
/usr/share/locale/de/LC_MESSAGES/minidlna.mo
/usr/share/locale/sl/LC_MESSAGES/minidlna.mo
/usr/share/locale/sv/LC_MESSAGES/minidlna.mo
/usr/share/locale/ja/LC_MESSAGES/minidlna.mo
/usr/share/locale/nb/LC_MESSAGES/minidlna.mo
/usr/share/locale/nl/LC_MESSAGES/minidlna.mo
/usr/share/locale/ko/LC_MESSAGES/minidlna.mo
/usr/share/locale/da/LC_MESSAGES/minidlna.mo
/usr/share/locale/pl/LC_MESSAGES/minidlna.mo
/usr/share/locale/es/LC_MESSAGES/minidlna.mo
/usr/share/locale/fr/LC_MESSAGES/minidlna.mo
/usr/sbin/minidlnad

%pre

%post
systemctl enable minidlnad
systemctl start minidlnad

%preun
systemctl stop minidlnad
systemctl disable minidlnad

%postun
rm -f /etc/systemd/system/minidlnad.service
rm -f /etc/minidlna.conf
rm -f /usr/share/locale/it/LC_MESSAGES/minidlna.mo
rm -f /usr/share/locale/ru/LC_MESSAGES/minidlna.mo
rm -f /usr/share/locale/de/LC_MESSAGES/minidlna.mo
rm -f /usr/share/locale/sl/LC_MESSAGES/minidlna.mo
rm -f /usr/share/locale/sv/LC_MESSAGES/minidlna.mo
rm -f /usr/share/locale/ja/LC_MESSAGES/minidlna.mo
rm -f /usr/share/locale/nb/LC_MESSAGES/minidlna.mo
rm -f /usr/share/locale/nl/LC_MESSAGES/minidlna.mo
rm -f /usr/share/locale/ko/LC_MESSAGES/minidlna.mo
rm -f /usr/share/locale/da/LC_MESSAGES/minidlna.mo
rm -f /usr/share/locale/pl/LC_MESSAGES/minidlna.mo
rm -f /usr/share/locale/es/LC_MESSAGES/minidlna.mo
rm -f /usr/share/locale/fr/LC_MESSAGES/minidlna.mo
rm -f /usr/sbin/minidlnad

%clean
rm -f  %{_sourcedir}/%{name}-%{version}.tar.gz
rm -rf %{buildroot}

%changelog
