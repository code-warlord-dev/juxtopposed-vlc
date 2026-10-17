# Juxtopposed VLC — русская сборка

Форк [dsojevic/juxtopposed-vlc](https://github.com/dsojevic/juxtopposed-vlc) с русским интерфейсом и пакетами для Linux.

## Сборка из исходников

```bash
meson setup build --prefix=/usr -Dtests=disabled
ninja -C build
sudo ninja -C build install
```

## Пакеты

- Arch Linux: `packaging/arch/PKGBUILD`
- Debian/Ubuntu: `packaging/deb`
- Fedora/RHEL: `packaging/rpm/juxtopposed-vlc.spec`
- AppImage: `packaging/appimage/build-appimage.sh`

CI собирает артефакты автоматически (см. `.github/workflows/build.yml`).

## Язык

Интерфейс использует системную локаль. Для русского:

```bash
LANG=ru_RU.UTF-8 vlc
```
EOF