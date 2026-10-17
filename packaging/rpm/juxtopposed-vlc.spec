Name:           juxtopposed-vlc
Version:        4.0.0
Release:        1%{?dist}
Summary:        VLC media player with Juxtopposed redesign (Russian UI)
License:        GPLv2+
URL:            https://github.com/code-warlord-dev/juxtopposed-vlc
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  meson, ninja-build, gcc, pkgconfig
Requires:       vlc

%description
VLC media player with Juxtopposed redesign and Russian UI.

%prep
%autosetup

%build
meson setup build --prefix=/usr -Dtests=disabled
ninja -C build

%install
DESTDIR=%{buildroot} ninja -C build install

%files
/usr/bin/vlc
/usr/lib64/vlc/
/usr/share/vlc/

%changelog
* Sat Oct 17 2026 code_warlord - 4.0.0-1
- Initial package
