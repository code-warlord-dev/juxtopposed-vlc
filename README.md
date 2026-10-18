# VLC media player (Juxtopposed, русская версия)

Этот форк адаптирует [редизайн VLC от Juxtopposed](https://www.figma.com/community/file/1691465999134370980/vlc-redesign)
для нативного интерфейса VLC. Интерфейс и настройки находятся в активной разработке.

**Перевод интерфейса на русский язык выполнен [code-warlord-dev](https://github.com/code-warlord-dev).**

## Демонстрация (русскоязычный интерфейс)

▶ [Смотреть демо-видео (66 с, MP4)](doc/videos/demo-ru.mp4)

![Простой проигрыватель с видео pixel-cat](doc/images/redesign/player.png)

| Библиотека слева | Настройки видео |
| --- | --- |
| ![Библиотека слева поверх видео](doc/images/redesign/sidebar.png) | ![Настройки видео поверх видео](doc/images/redesign/video-settings.png) |

**VLC** — это свободный и открытый **музыкально-видеопроигрыватель** и **мультимедийный движок**,
который сосредоточен на **воспроизведении всего** и **работе везде**.

**VLC** может воспроизводить большинство мультимедийных файлов, дисков, потоков и устройств, а также
конвертировать, кодировать, **стримить** и обрабатывать потоки в многочисленных форматах.

VLC используется многими людьми по всему миру, на многочисленных платформах и для самых разных задач.

**Движок VLC** может быть встроен в сторонние приложения и называется *libVLC*.

**VLC** является частью [проекта VideoLAN](https://videolan.org) и
разрабатывается и поддерживается сообществом добровольцев.

Проект VideoLAN был начат в университете [École Centrale Paris](https://www.centralesupelec.fr/), который
переиздал VLC под лицензией GPLv2 в феврале 2001 года. С тех пор VLC был скачан
**миллиарды** раз.

## Установка

Готовые пакеты доступны на [странице релизов](https://github.com/code-warlord-dev/juxtopposed-vlc/releases):

- **AppImage** (универсальный для любых дистрибутивов Linux)
- **deb** (Debian, Ubuntu и производные)
- **rpm** (Fedora, RHEL, openSUSE и производные)
- **pkg.tar.zst** (Arch Linux, CachyOS и производные)

### Arch Linux / CachyOS
```bash
sudo pacman -U juxtopposed-vlc-*.pkg.tar.zst
```

### Debian / Ubuntu
```bash
sudo apt install ./juxtopposed-vlc_*.deb
```

### Fedora / RHEL
```bash
sudo rpm -i juxtopposed-vlc-*.rpm
```

### AppImage
```bash
chmod +x JuxtopposedVLC-*.AppImage
./JuxtopposedVLC-*.AppImage
```

### Сборка из исходников
```bash
meson setup build --prefix=/usr -Dtests=disabled
ninja -C build
sudo ninja -C build install
```

## Лицензия

**VLC** распространяется под лицензией GPLv2 *(или более новой)*.
*На некоторых платформах де-факто используется GPLv3 из-за лицензий зависимостей*.

**libVLC**, движок, распространяется под лицензией LGPLv2 *(или более новой)*.
Это позволяет встраивать движок в сторонние приложения, оставляя их под другими лицензиями.

## Атрибуция редизайна

Интерфейс в `master` адаптирован из **VLC Redesign**
авторства [Juxtopposed](https://www.juxtopposed.com/) и распространяется по лицензии
[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
Оригинальный дизайн доступен в
[Figma Community](https://www.figma.com/community/file/1691465999134370980/vlc-redesign),
там же есть [видеообзор](https://www.youtube.com/watch?v=ERFeOgqk324).

Эта реализация модифицирует дизайн для нативного интерфейса VLC, включая
адаптивные компоновки, интерактивные элементы управления, организацию настроек и интеграцию
с воспроизведением и медиатекой VLC. Заслуга за дизайн и уведомление CC BY 4.0
относятся к оригинальному дизайну; лицензии VLC остаются описанными выше.

Интерфейс использует [Inter](https://rsms.me/inter/) Рамуса Андерссона и контрибьюторов.
Встроенные шрифты распространяются по лицензии [SIL Open Font License 1.1](modules/gui/qt/fonts/LICENSE.txt).

# Платформы

VLC доступен для следующих платформ:
- [Windows] *(с 7 и далее, включая UWP и все версии Windows 10)*
- [macOS] *(10.10 и далее)*
- [GNU/Linux] и производные
- [BSD] и производные
- [Android] *(4.2 и далее)*, включая Android TV и Android Auto
- [iOS] *(9 и далее)*, включая AppleTV и iPadOS
- Haiku, OS/2 и некоторые другие.

[Windows]: https://www.videolan.org/vlc/download-windows.html
[macOS]: https://www.videolan.org/vlc/download-macosx.html
[GNU/Linux]: https://www.videolan.org/vlc/#download
[BSD]: https://www.videolan.org/vlc/download-freebsd.html
[Android]: https://www.videolan.org/vlc/download-android.html
[iOS]: https://www.videolan.org/vlc/download-ios.html

Не все платформы получают одинаковое внимание из-за ограниченных ресурсов.

**Примечание**: приложения [Android](https://code.videolan.org/videolan/vlc-android/) и
[iOS](https://code.videolan.org/videolan/vlc-ios/) находятся в других репозиториях,
а не в основном.

# Участие в разработке и сообщество

**VLC** поддерживается сообществом людей, и VideoLAN никому за это не платит.
Сообщество состоит из разработчиков, помощников, мейнтейнеров, дизайнеров и писателей,
которые хотят, чтобы этот проект с открытым исходным кодом процветал.

Основная разработка VLC ведётся на языке C, но в этом репозитории также много
C++, Obj-C, asm и Rust.

Другие репозитории, связанные с VLC, написаны на таких языках, как Kotlin/Java [(Android)](https://code.videolan.org/videolan/vlc-android/),
Swift [(iOS)](https://code.videolan.org/videolan/vlc-ios/) и C# [(libVLCSharp)](https://code.videolan.org/videolan/libvlcsharp/).

Нам нужна помощь в следующем:
- Кодирование
- Упаковка для Windows, macOS и дистрибутивов Linux
- Техническое писательство для документации
- Дизайн
- Поддержка
- Управление сообществом и коммуникация.

Пожалуйста, участвуйте :)

Мы в IRC. Нас можно найти в канале **#videolan** на *[Libera.chat]*.

[Libera.chat]: https://libera.chat

## Вклад

Вклад вносится через Merge Requests в нашем [репозитории GitLab](https://code.videolan.org/videolan/vlc/).

CI и обсуждения должны быть завершены, прежде чем Merge Request сможет быть принят.

# libVLC

**libVLC** — это встраиваемый движок для сторонних приложений и фреймворков.

Он работает на тех же платформах, что и VLC *(иногда и на больших)* и может обеспечивать
воспроизведение, стриминг и конвертацию мультимедийных файлов и потоков.

У **libVLC** есть многочисленные привязки для других языков, таких как C++, Python и C#.

# Поддержка

## Ссылки

Несколько полезных ссылок, которые могут помочь:

- [Веб-сайт VLC](https://www.videolan.org/vlc/)
- [Поддержка](https://www.videolan.org/support/)
- [Форумы](https://forum.videolan.org/)
- [Wiki](https://wiki.videolan.org/)
- [Раздел для разработчиков](https://wiki.videolan.org/Developers_Corner)
- [Гайд по изучению VLC](https://wiki.videolan.org/Hacker_Guide)
- [Багтрекер](https://code.videolan.org/videolan/vlc/-/issues)
- [Веб-сайт VideoLAN](https://www.videolan.org/)

## Карта каталогов исходного кода
```
ABOUT-NLS          - Заметки о Free Translation Project.
AUTHORS            - Авторы VLC.
COPYING            - Лицензия GPL.
COPYING.LIB        - Лицензия LGPL.
INSTALL            - Инструкции по сборке и установке.
NEWS               - Важные изменения между релизами.
README             - Описание проекта.
THANKS             - Благодарности контрибьюторам VLC.

bin/               - Бинарники VLC.
bindings/          - Привязки libVLC к другим языкам.
compat/            - библиотека совместимости для операционных систем,
                     в которых отсутствуют необходимые функции.
contrib/           - Инструменты для получения внешних библиотек и их сборки
                     для систем, у которых нет нужных версий.
doc/               - Различная документация.
extras/analyser    - Специфичные для код-анализатора файлы.
extras/buildsystem - Различные файлы для сборки.
extras/misc        - Файлы, которые не вписываются в другие категории extras/.
extras/package     - Файлы упаковки VLC, например spec-файлы.
extras/tools/      - Инструменты для получения внешних инструментов сборки
                     для систем, у которых нет нужных версий.
include/           - Заголовочные файлы.
lib/               - Исходный код libVLC.
modules/           - Плагины и модули VLC. Здесь большая часть кода.
po/                - Переводы VLC.
share/             - Общие ресурсные файлы.
src/               - Исходный код libvlccore.
test/              - Тестовая система.
```
