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
    draw.text(xy, text, fill=fill, font=font(size))


def make_background(filename: str, title: str, colors: tuple[str, str], accent: str) -> None:
    path = BG_DIR / filename
    if not HAS_PILLOW:
        fallback_image(path, 1920, 1080, colors[0])
        return

    img = Image.new("RGB", (1920, 1080), colors[0])
    draw = ImageDraw.Draw(img)
    c1 = hex_to_rgb(colors[0])
    c2 = hex_to_rgb(colors[1])
    for y in range(1080):
        ratio = y / 1079
        rgb = tuple(int(c1[i] * (1 - ratio) + c2[i] * ratio) for i in range(3))
        draw.line([(0, y), (1920, y)], fill=rgb)

    for i in range(9):
        x = 120 + i * 210
        draw.rounded_rectangle((x, 190, x + 120, 860), radius=24, outline="#64748b", width=3)
    draw.line((120, 820, 1800, 820), fill=accent, width=5)
    draw.ellipse((1420, 120, 1780, 480), outline=accent, width=6)
    draw.rectangle((0, 900, 1920, 1080), fill="#020617")
    draw_label(draw, (80, 70), title, accent, 58)
    draw_label(draw, (80, 145), "MOON CITY MVP PLACEHOLDER", "#cbd5e1", 28)
    img.save(path)


def make_character(name: str, expression: str, color: str) -> None:
    path = CHAR_DIR / f"{name}_{expression}.png"
    if not HAS_PILLOW:
        fallback_image(path, 900, 1400, color, 220)
        return

    img = Image.new("RGBA", (900, 1400), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    accent = hex_to_rgb(color)
    body = accent + (225,)
    dark = tuple(max(c - 45, 0) for c in accent) + (235,)

    draw.ellipse((325, 125, 575, 375), fill=body, outline=(230, 245, 255, 230), width=5)
    draw.rounded_rectangle((260, 360, 640, 1100), radius=130, fill=dark, outline=(230, 245, 255, 210), width=5)
    draw.polygon([(260, 500), (130, 930), (260, 960)], fill=body)
    draw.polygon([(640, 500), (770, 930), (640, 960)], fill=body)
    draw.rectangle((330, 1080, 410, 1320), fill=dark)
    draw.rectangle((490, 1080, 570, 1320), fill=dark)

    if expression in ["surprised", "shaken", "anxious", "alert"]:
        draw.ellipse((380, 225, 410, 255), fill="#ffffff")
        draw.ellipse((490, 225, 520, 255), fill="#ffffff")
    elif expression in ["pained", "sad", "tired", "broken", "defeated"]:
        draw.line((375, 250, 425, 235), fill="#ffffff", width=6)
        draw.line((475, 235, 525, 250), fill="#ffffff", width=6)
    else:
        draw.line((375, 240, 425, 240), fill="#ffffff", width=6)
        draw.line((475, 240, 525, 240), fill="#ffffff", width=6)

    draw_label(draw, (70, 70), f"{name.upper()} / {expression}", "#e5e7eb", 36)
    img.save(path)


def make_alma(state: str) -> None:
    path = CHAR_DIR / f"alma_{state}.png"
    if not HAS_PILLOW:
        fallback_image(path, 900, 1400, "#22d3ee", 190)
        return

    img = Image.new("RGBA", (900, 1400), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    accent = "#f59e0b" if state == "alert" else "#22d3ee"
    draw.rounded_rectangle((170, 260, 730, 1080), radius=90, outline=accent, width=8, fill=(2, 6, 23, 190))
    for i in range(14):
        x = 230 + i * 34
        h = 80 + int(55 * math.sin(i * 0.9 + len(state)))
        draw.line((x, 690 - h, x, 690 + h), fill=accent, width=8)
    draw.ellipse((320, 390, 580, 650), outline=accent, width=6)
    draw_label(draw, (240, 180), f"ALMA / {state.upper()}", "#e0f2fe", 38)
    img.save(path)


def make_ui(filename: str, size: tuple[int, int], fill: str, accent: str, label: str) -> None:
    path = UI_DIR / filename
    if not HAS_PILLOW:
        fallback_image(path, size[0], size[1], fill, 235)
        return

    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    w, h = size
    draw.rounded_rectangle((6, 6, w - 6, h - 6), radius=24, fill=hex_to_rgb(fill) + (238,), outline=accent, width=4)
    draw.line((26, h - 28, w - 26, h - 28), fill=accent, width=3)
    draw_label(draw, (30, 24), label, accent, 30)
    img.save(path)


def make_icon(filename: str, color: str, label: str) -> None:
    path = ICON_DIR / filename
    if not HAS_PILLOW:
        fallback_image(path, 256, 256, color, 255)
        return

    img = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((18, 18, 238, 238), radius=42, fill="#0f172a", outline=color, width=8)
    draw.ellipse((74, 58, 182, 166), outline=color, width=8)
    draw.line((64, 190, 192, 190), fill=color, width=8)
    draw_label(draw, (54, 104), label, "#e5e7eb", 28)
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
