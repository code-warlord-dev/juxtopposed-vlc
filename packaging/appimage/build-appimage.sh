#!/usr/bin/env bash
set -e
APPDIR="${1:-/tmp/opencode/AppDir}"
STAGING="${2:-/tmp/opencode/staging}"
rm -rf "$APPDIR"
mkdir -p "$APPDIR/usr"
cp -a "$STAGING/usr/." "$APPDIR/usr/"
# AppRun
cat > "$APPDIR/AppRun" <<'EOF'
#!/bin/bash
HERE="$(dirname "$(readlink -f "${0}")")"
export LD_LIBRARY_PATH="$HERE/usr/lib:$HERE/usr/lib/vlc:${LD_LIBRARY_PATH}"
exec "$HERE/usr/bin/vlc" "$@"
EOF
chmod +x "$APPDIR/AppRun"
# desktop
mkdir -p "$APPDIR/usr/share/applications"
cat > "$APPDIR/juxtopposed-vlc.desktop" <<'EOF'
[Desktop Entry]
Name=VLC media player (Juxtopposed)
Exec=vlc %U
Icon=vlc
Type=Application
Categories=AudioVideo;Player;
EOF
cp "$APPDIR/juxtopposed-vlc.desktop" "$APPDIR/usr/share/applications/"
# icon
mkdir -p "$APPDIR/usr/share/icons/hicolor/256x256/apps"
cp /usr/share/icons/hicolor/256x256/apps/vlc.png "$APPDIR/usr/share/icons/hicolor/256x256/apps/vlc.png" 2>/dev/null || true
ln -sf usr/share/icons/hicolor/256x256/apps/vlc.png "$APPDIR/vlc.png"
# build
cd /tmp/opencode
./appimagetool "$APPDIR" /tmp/opencode/JuxtopposedVLC-x86_64.AppImage
EOF