# Fonts

This project bundles Japanese-capable open fonts so Ren'Py can render Japanese text without tofu boxes.

## Included Fonts

- `NotoSansJP-Regular.otf`
- `NotoSansJP-Bold.otf`

These files are Japanese OTF fonts from the Noto Sans CJK project:

- Source: https://github.com/notofonts/noto-cjk
- Original filenames:
  - `NotoSansCJKjp-Regular.otf`
  - `NotoSansCJKjp-Bold.otf`
- License: SIL Open Font License 1.1

The files are renamed inside this project for clarity. Do not replace them with Windows system fonts such as Meiryo, MS Gothic, or Yu Gothic, because redistribution rights for OS-bundled fonts are not assumed here.

If Japanese text appears as tofu boxes in Ren'Py, confirm that these files exist and that `game/font_config.rpy` points to them.

