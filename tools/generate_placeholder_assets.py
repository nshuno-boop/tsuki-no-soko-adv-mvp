"""Generate placeholder assets for the Ren'Py MVP.

The script prefers Pillow for labeled, transparent placeholders. If Pillow is
not available, it falls back to a tiny standard-library PNG writer so the
project still gets real image files.
"""

from __future__ import annotations

import math
import struct
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BG_DIR = ROOT / "game" / "images" / "bg"
CHAR_DIR = ROOT / "game" / "images" / "chars"
UI_DIR = ROOT / "game" / "images" / "ui"
ICON_DIR = ROOT / "game" / "images" / "icons"

SCREEN_SIZE = (1280, 720)
SPRITE_SIZE = (520, 760)

try:
    from PIL import Image, ImageDraw, ImageFont

    HAS_PILLOW = True
except Exception:
    Image = None
    ImageDraw = None
    ImageFont = None
    HAS_PILLOW = False


BACKGROUNDS = [
    ("bg_lander_interior.png", "LANDER INTERIOR", ("#0b1220", "#26364f"), "#8bd3ff"),
    ("bg_shirowa_hab_ring.png", "SHIROWA HAB RING", ("#09111d", "#334155"), "#dbeafe"),
    ("bg_core.png", "CORE", ("#06111f", "#172554"), "#67e8f9"),
    ("bg_oxygen_workshop_r7.png", "OXYGEN WORKSHOP R-7", ("#101923", "#374151"), "#fbbf24"),
    ("bg_outer_port.png", "OUTER PORT", ("#07121c", "#1f2937"), "#93c5fd"),
    ("bg_medbay.png", "MEDBAY", ("#0b1320", "#1e3a3a"), "#bfdbfe"),
    ("bg_sena_office.png", "SENA OFFICE", ("#140f1f", "#3b2536"), "#f9a8d4"),
    ("bg_dawn_window.png", "DAWN WINDOW", ("#050816", "#1e293b"), "#fde68a"),
    ("bg_shadow_well.png", "SHADOW WELL", ("#020617", "#1f2937"), "#a78bfa"),
]

CHARACTERS = [
    ("mio", ["neutral", "thinking", "surprised", "pained"], "#6bb7ff"),
    ("sena", ["neutral", "smile", "calm", "shaken", "broken"], "#ff8fb3"),
    ("toru", ["neutral", "tired", "gentle", "recording"], "#d8b76a"),
    ("ritsu", ["neutral", "anxious", "angry", "relieved"], "#60a5fa"),
    ("luka", ["neutral", "sarcastic", "angry", "sad"], "#f59e0b"),
    ("akari", ["neutral", "doctor", "worried"], "#cbd5e1"),
    ("noah", ["neutral", "rebellious", "tears", "smile"], "#86efac"),
    ("jin", ["neutral", "business_smile", "irritated", "defeated"], "#fb923c"),
]

ALMA_STATES = ["idle", "alert", "speaking"]

UI_ASSETS = [
    ("ui_textbox.png", (1100, 230), "#0f172a", "#67e8f9", "TEXTBOX"),
    ("ui_nameplate.png", (420, 90), "#111827", "#93c5fd", "NAMEPLATE"),
    ("ui_evidence_card.png", (760, 420), "#0b1120", "#fbbf24", "EVIDENCE CARD"),
    ("ui_log_panel.png", (900, 520), "#020617", "#67e8f9", "LOG PANEL"),
    ("ui_choice_button.png", (760, 120), "#172033", "#67e8f9", "CHOICE"),
    ("ui_timeline_panel.png", (900, 320), "#111827", "#a78bfa", "TIMELINE"),
    ("ui_alma_panel.png", (900, 520), "#03121c", "#22d3ee", "ALMA PANEL"),
]

ICONS = [
    ("icon_evidence_log.png", "#67e8f9", "LOG"),
    ("icon_evidence_suit.png", "#93c5fd", "SUIT"),
    ("icon_evidence_audio.png", "#a78bfa", "AUD"),
    ("icon_evidence_medical.png", "#bfdbfe", "MED"),
    ("icon_evidence_key.png", "#fbbf24", "KEY"),
    ("icon_person.png", "#86efac", "PER"),
    ("icon_location.png", "#38bdf8", "LOC"),
    ("icon_warning.png", "#f59e0b", "WARN"),
]


def ensure_dirs() -> None:
    for directory in [BG_DIR, CHAR_DIR, UI_DIR, ICON_DIR]:
        directory.mkdir(parents=True, exist_ok=True)


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def write_png_rgba(path: Path, width: int, height: int, rows: list[bytes]) -> None:
    def chunk(kind: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)

    raw = b"".join(b"\x00" + row for row in rows)
    payload = b"\x89PNG\r\n\x1a\n"
    payload += chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0))
    payload += chunk(b"IDAT", zlib.compress(raw, 9))
    payload += chunk(b"IEND", b"")
    path.write_bytes(payload)


def fallback_image(path: Path, width: int, height: int, color: str, alpha: int = 255) -> None:
    rgb = hex_to_rgb(color)
    rows = []
    for y in range(height):
        shade = int(18 * (y / max(height - 1, 1)))
        pixel = bytes((min(rgb[0] + shade, 255), min(rgb[1] + shade, 255), min(rgb[2] + shade, 255), alpha))
        rows.append(pixel * width)
    write_png_rgba(path, width, height, rows)


def font(size: int):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except Exception:
        return ImageFont.load_default()


def draw_label(draw, xy: tuple[int, int], text: str, fill: str, size: int = 44) -> None:
    # Kept for future debugging, but Phase 4 placeholders avoid embedding text.
    draw.text(xy, text, fill=fill, font=font(size))


def make_background(filename: str, title: str, colors: tuple[str, str], accent: str) -> None:
    path = BG_DIR / filename
    width, height = SCREEN_SIZE
    if not HAS_PILLOW:
        fallback_image(path, width, height, colors[0])
        return

    img = Image.new("RGB", SCREEN_SIZE, colors[0])
    draw = ImageDraw.Draw(img)
    c1 = hex_to_rgb(colors[0])
    c2 = hex_to_rgb(colors[1])
    for y in range(height):
        ratio = y / max(height - 1, 1)
        rgb = tuple(int(c1[i] * (1 - ratio) + c2[i] * ratio) for i in range(3))
        draw.line([(0, y), (width, y)], fill=rgb)

    for i in range(8):
        x = 70 + i * 150
        draw.rounded_rectangle((x, 120, x + 76, 565), radius=18, outline="#64748b", width=2)
        draw.line((x + 14, 145, x + 62, 145), fill="#334155", width=2)
        draw.line((x + 14, 535, x + 62, 535), fill="#334155", width=2)

    draw.line((80, 555, 1200, 555), fill=accent, width=3)
    draw.line((80, 600, 1200, 600), fill="#1e293b", width=2)
    draw.ellipse((930, 78, 1180, 328), outline=accent, width=4)
    draw.ellipse((980, 128, 1130, 278), outline="#334155", width=2)
    for i in range(6):
        y = 225 + i * 48
        draw.line((120, y, 420, y), fill="#1f2937", width=2)
    draw.rounded_rectangle((760, 420, 1130, 535), radius=18, outline="#475569", width=2, fill="#020617")
    draw.line((790, 455, 1100, 455), fill=accent, width=2)
    draw.line((790, 488, 1040, 488), fill="#334155", width=2)
    draw.rectangle((0, 600, width, height), fill="#020617")
    draw.line((0, 600, width, 600), fill=accent, width=2)
    img.save(path)


def make_character(name: str, expression: str, color: str) -> None:
    path = CHAR_DIR / f"{name}_{expression}.png"
    if not HAS_PILLOW:
        fallback_image(path, SPRITE_SIZE[0], SPRITE_SIZE[1], color, 220)
        return

    img = Image.new("RGBA", (900, 1400), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    accent = hex_to_rgb(color)
    body = tuple(max(c - 55, 0) for c in accent) + (238,)
    coat = tuple(min(c + 38, 255) for c in accent) + (210,)
    line = (226, 242, 255, 210)

    profile = {
        "mio": (335, 150, 565, 365, 255, 400, 645, 1130),
        "sena": (330, 135, 570, 365, 245, 390, 655, 1125),
        "toru": (320, 145, 580, 380, 235, 410, 665, 1135),
        "ritsu": (325, 135, 575, 360, 250, 405, 650, 1125),
        "luka": (310, 150, 590, 390, 220, 420, 680, 1150),
        "akari": (330, 145, 570, 370, 250, 400, 650, 1130),
        "noah": (350, 175, 550, 370, 290, 420, 610, 1080),
        "jin": (325, 140, 575, 365, 250, 395, 650, 1130),
    }.get(name, (330, 145, 570, 370, 250, 400, 650, 1130))

    hx1, hy1, hx2, hy2, bx1, by1, bx2, by2 = profile
    draw.ellipse((hx1, hy1, hx2, hy2), fill=(28, 38, 52, 245), outline=line, width=5)
    draw.pieslice((hx1 - 30, hy1 - 35, hx2 + 35, hy2 + 45), 185, 355, fill=body)
    draw.rounded_rectangle((bx1, by1, bx2, by2), radius=110, fill=body, outline=line, width=5)
    draw.polygon([(bx1 + 25, by1 + 80), (145, 930), (bx1 + 55, 980)], fill=coat)
    draw.polygon([(bx2 - 25, by1 + 80), (755, 930), (bx2 - 55, 980)], fill=coat)
    draw.line((bx1 + 95, by1 + 70, bx1 + 170, by2 - 80), fill=coat, width=10)
    draw.line((bx2 - 95, by1 + 70, bx2 - 170, by2 - 80), fill=coat, width=10)
    draw.rectangle((340, 1085, 420, 1320), fill=body)
    draw.rectangle((480, 1085, 560, 1320), fill=body)

    if name == "sena":
        draw.line((310, 435, 590, 435), fill="#f9a8d4", width=8)
    elif name == "akari":
        draw.rounded_rectangle((270, 430, 630, 1060), radius=70, outline="#e2e8f0", width=8)
    elif name == "jin":
        draw.line((405, 410, 450, 610), fill="#f8fafc", width=10)
        draw.line((495, 410, 450, 610), fill="#f8fafc", width=10)
    elif name == "noah":
        draw.line((310, 500, 590, 500), fill="#86efac", width=6)
    elif name == "luka":
        draw.line((260, 520, 640, 520), fill="#f59e0b", width=7)
    elif name == "ritsu":
        draw.rectangle((600, 620, 675, 780), outline="#93c5fd", width=5)

    eye_y = 260
    if expression in ["surprised", "shaken", "anxious"]:
        draw.ellipse((380, eye_y, 410, eye_y + 28), fill="#e0f2fe")
        draw.ellipse((490, eye_y, 520, eye_y + 28), fill="#e0f2fe")
    elif expression in ["pained", "sad", "tired", "broken", "defeated", "tears"]:
        draw.line((374, eye_y + 15, 424, eye_y), fill="#e0f2fe", width=6)
        draw.line((476, eye_y, 526, eye_y + 15), fill="#e0f2fe", width=6)
        if expression == "tears":
            draw.line((510, eye_y + 35, 505, eye_y + 95), fill="#93c5fd", width=5)
    elif expression in ["smile", "gentle", "relieved", "business_smile"]:
        draw.arc((370, eye_y - 10, 430, eye_y + 45), 20, 160, fill="#e0f2fe", width=5)
        draw.arc((470, eye_y - 10, 530, eye_y + 45), 20, 160, fill="#e0f2fe", width=5)
    else:
        draw.line((375, eye_y + 5, 425, eye_y + 5), fill="#e0f2fe", width=6)
        draw.line((475, eye_y + 5, 525, eye_y + 5), fill="#e0f2fe", width=6)

    if expression in ["angry", "rebellious", "irritated"]:
        draw.line((365, 245, 425, 225), fill="#f8fafc", width=5)
        draw.line((475, 225, 535, 245), fill="#f8fafc", width=5)

    img = img.resize(SPRITE_SIZE, Image.Resampling.LANCZOS)
    img.save(path)


def make_alma(state: str) -> None:
    path = CHAR_DIR / f"alma_{state}.png"
    if not HAS_PILLOW:
        fallback_image(path, SPRITE_SIZE[0], SPRITE_SIZE[1], "#22d3ee", 190)
        return

    img = Image.new("RGBA", (900, 1400), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    accent = "#f59e0b" if state == "alert" else "#22d3ee"
    draw.rounded_rectangle((190, 330, 710, 980), radius=90, outline=accent, width=6, fill=(2, 6, 23, 120))
    draw.ellipse((300, 430, 600, 730), outline=accent, width=5)
    draw.ellipse((360, 490, 540, 670), outline=(148, 163, 184, 180), width=3)
    for i in range(14):
        x = 230 + i * 34
        h = 80 + int(55 * math.sin(i * 0.9 + len(state)))
        draw.line((x, 1030 - h, x, 1030 + h), fill=accent, width=6)
    img = img.resize(SPRITE_SIZE, Image.Resampling.LANCZOS)
    img.save(path)


def make_ui(filename: str, size: tuple[int, int], fill: str, accent: str, label: str) -> None:
    path = UI_DIR / filename
    if not HAS_PILLOW:
        fallback_image(path, size[0], size[1], fill, 235)
        return

    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    w, h = size
    draw.rounded_rectangle((6, 6, w - 6, h - 6), radius=24, fill=hex_to_rgb(fill) + (238,), outline=accent, width=3)
    draw.line((26, h - 28, w - 26, h - 28), fill=accent, width=2)
    draw.line((26, 28, min(w - 26, 260), 28), fill=accent, width=2)
    img.save(path)


def make_icon(filename: str, color: str, label: str) -> None:
    path = ICON_DIR / filename
    if not HAS_PILLOW:
        fallback_image(path, 256, 256, color, 255)
        return

    img = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((18, 18, 238, 238), radius=42, fill="#0f172a", outline=color, width=7)
    if "log" in filename:
        draw.rectangle((72, 58, 184, 188), outline=color, width=7)
        for y in [88, 116, 144]:
            draw.line((92, y, 165, y), fill=color, width=5)
    elif "suit" in filename:
        draw.ellipse((84, 50, 172, 138), outline=color, width=7)
        draw.rounded_rectangle((68, 130, 188, 210), radius=28, outline=color, width=7)
    elif "audio" in filename:
        for x in [78, 104, 130, 156, 182]:
            draw.line((x, 74, x, 182), fill=color, width=7)
    elif "medical" in filename:
        draw.line((128, 62, 128, 194), fill=color, width=12)
        draw.line((62, 128, 194, 128), fill=color, width=12)
    elif "key" in filename:
        draw.ellipse((66, 76, 136, 146), outline=color, width=8)
        draw.line((130, 138, 196, 204), fill=color, width=9)
        draw.line((168, 176, 194, 150), fill=color, width=7)
    elif "person" in filename:
        draw.ellipse((86, 58, 170, 142), outline=color, width=7)
        draw.arc((64, 140, 192, 232), 200, 340, fill=color, width=8)
    elif "location" in filename:
        draw.polygon([(128, 46), (196, 190), (128, 158), (60, 190)], outline=color, fill=None)
        draw.line((128, 46, 196, 190), fill=color, width=7)
        draw.line((128, 46, 60, 190), fill=color, width=7)
    else:
        draw.polygon([(128, 50), (210, 198), (46, 198)], outline=color, fill=None)
        draw.line((128, 92, 128, 148), fill=color, width=8)
        draw.ellipse((122, 165, 134, 177), fill=color)
    img.save(path)


def main() -> None:
    ensure_dirs()

    for filename, title, colors, accent in BACKGROUNDS:
        make_background(filename, title, colors, accent)

    for name, expressions, color in CHARACTERS:
        for expression in expressions:
            make_character(name, expression, color)

    for state in ALMA_STATES:
        make_alma(state)

    for filename, size, fill, accent, label in UI_ASSETS:
        make_ui(filename, size, fill, accent, label)

    for filename, color, label in ICONS:
        make_icon(filename, color, label)

    total = len(BACKGROUNDS) + sum(len(item[1]) for item in CHARACTERS) + len(ALMA_STATES) + len(UI_ASSETS) + len(ICONS)
    engine = "Pillow" if HAS_PILLOW else "standard library fallback"
    print(f"Generated {total} placeholder PNG files using {engine}.")


if __name__ == "__main__":
    main()
