# Japanese font configuration.
# Ren'Py's default font may not include Japanese glyphs, so all dialogue and
# project UI styles point at bundled OFL Noto Sans CJK Japanese fonts.

define gui.language = "japanese-normal"

define gui.text_font = "fonts/NotoSansJP-Regular.otf"
define gui.name_text_font = "fonts/NotoSansJP-Bold.otf"
define gui.interface_text_font = "fonts/NotoSansJP-Regular.otf"
define gui.system_font = "fonts/NotoSansJP-Regular.otf"

style default:
    font gui.text_font
    language "japanese-normal"

style say_dialogue:
    font gui.text_font
    language "japanese-normal"

style say_label:
    font gui.name_text_font
    language "japanese-normal"

style button_text:
    font gui.interface_text_font
    language "japanese-normal"

style input:
    font gui.text_font
    language "japanese-normal"

style tsuki_title_text:
    font gui.interface_text_font
    language "japanese-normal"

style tsuki_subtle_text:
    font gui.interface_text_font
    language "japanese-normal"

style tsuki_button_text:
    font gui.interface_text_font
    language "japanese-normal"

style alma_log_text:
    font gui.interface_text_font
    language "japanese-normal"

