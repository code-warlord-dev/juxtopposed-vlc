Name:           juxtopposed-vlc
Version:        4.0.0
Release:        1%{?dist}
Summary:        VLC media player with Juxtopposed redesign (Russian UI)
License:        GPLv2+
URL:            https://github.com/code-warlord-dev/juxtopposed-vlc
Source0:        %{name}-%{version}.tar.gz

Requires:       glibc, libgcc, glib2, qt6-qtbase, ffmpeg-libs

%description
VLC media player with Juxtopposed redesign and fully Russian UI (100% translation).

%prep
%setup -q

%build

%install
cp -a usr %{buildroot}/

%files
/usr/bin/vlc
/usr/lib*/vlc/
/usr/lib/libvlc.so*
/usr/lib/libvlccore.so*
/usr/share/vlc/
/usr/share/locale/ru/
/usr/share/applications/juxtopposed-vlc.desktop
/usr/share/icons/hicolor/*/apps/vlc.png

%changelog
* Sun Oct 18 2026 code_warlord - 4.0.0-1
- Initial package (Russian UI by code-warlord-dev)
