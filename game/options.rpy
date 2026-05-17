# Ren'Py project options for the MVP prototype.
# Full GUI tuning can be added later when real art assets are available.

define config.name = "月の底で、息をする"
define config.version = "v0.5-alpha"
define config.save_directory = "tsuki_no_soko_mvp"
define config.window_title = "月の底で、息をする"
define config.window_icon = "gui/window_icon.png"

# 16:9 baseline. This keeps temporary backgrounds and investigation screens
# predictable while prototyping.
define config.screen_width = 1280
define config.screen_height = 720

# MVPではボイス・BGMなしでも動くようにしておく。
define config.has_sound = True
define config.has_music = True
define config.has_voice = False
