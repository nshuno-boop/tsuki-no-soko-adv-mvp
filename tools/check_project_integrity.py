"""Static integrity checks for the Ren'Py MVP.

This is not a Ren'Py parser. It catches the common project-level mistakes that
matter while Ren'Py itself is unavailable: missing files, broken image paths,
missing evidence IDs, stale names, and documentation drift.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "game/script.rpy",
    "game/evidence.rpy",
    "game/screens.rpy",
    "game/characters.rpy",
    "game/options.rpy",
    "game/font_config.rpy",
    "game/images.rpy",
    "game/fonts/README.md",
    "game/fonts/NotoSansJP-Regular.otf",
    "game/fonts/NotoSansJP-Bold.otf",
    "docs/ASSET_MANIFEST.md",
    "docs/ART_DIRECTION.md",
    "docs/FONT_LICENSE.md",
    "docs/IMAGE_PROMPTS.md",
    "docs/PLAYTEST_CHECKLIST.md",
    "tools/generate_placeholder_assets.py",
    "tools/check_project_integrity.py",
    ".github/workflows/static-check.yml",
]

REQUIRED_EVIDENCE_IDS = [
    "e_r7_decompression_log",
    "e_personnel_location_log",
    "e_autopsy_record",
    "e_manual_bulkhead_blood",
    "e_white_rabbit_usage_log",
    "e_white_rabbit_co2_absorber",
    "e_white_rabbit_dust_test",
    "e_thermal_sensor_frost",
    "e_manual_valve_scratch",
    "e_maintenance_admin_log",
    "e_earth_meeting_audio",
    "e_noah_testimony",
    "e_toru_audit_file",
    "e_lunarborn_medical_report",
    "e_sena_dust_trace",
]

NEW_NAMES = [
    "シロワ",
    "セレネ資源開発",
    "ALMA",
    "白兎3号",
    "佐伯 澪",
    "雨宮 セナ",
    "檜山 徹",
    "北条 リツ",
    "ルカ・ナディム",
    "白石 アカリ",
    "雨宮 ノア",
    "鷹峰 ジン",
]

OLD_TERMS = [
    "アステリオン",
    "はっかんし",
    "北条ミナト",
    "白石ユナ",
    "九条 カイ",
    "白石 ルイ",
    "HAKKAN CITY",
    "HAKKAN",
]

REQUIRED_SCREENS = [
    "objective_overlay",
    "investigation_hub_screen",
    "evidence_screen",
    "person_memo_screen",
    "evidence_choice_screen",
    "multi_evidence_choice_screen",
    "person_choice_screen",
    "missing_evidence_screen",
    "interview_progress_warning_screen",
    "alma_log_screen",
    "timeline_screen",
]

REQUIRED_INTERVIEW_RETURNS = [
    "interview:sena",
    "interview:ritsu",
    "interview:luka",
    "interview:akari",
    "interview:noah",
    "interview:jin",
]


def read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def check_required_files(errors: list[str]) -> None:
    for file_name in REQUIRED_FILES:
        if not (ROOT / file_name).exists():
            errors.append(f"missing required file: {file_name}")


def check_image_paths(errors: list[str]) -> None:
    images_text = read_text("game/images.rpy")
    paths = re.findall(r'"([^"]+\.png)"', images_text)
    for path in paths:
        if not (ROOT / "game" / path).exists():
            errors.append(f"missing image referenced by images.rpy: game/{path}")


def check_font_config(errors: list[str], warnings: list[str]) -> None:
    font_config = read_text("game/font_config.rpy")
    required = [
        'define gui.language = "japanese-normal"',
        'define gui.text_font = "fonts/NotoSansJP-Regular.otf"',
        "define gui.interface_text_font",
        'language "japanese-normal"',
    ]
    for item in required:
        if item not in font_config:
            errors.append(f"font config missing: {item}")

    font_dir = ROOT / "game" / "fonts"
    regular = font_dir / "NotoSansJP-Regular.otf"
    if not regular.exists():
        errors.append("Japanese font missing: game/fonts/NotoSansJP-Regular.otf")

    suspicious = ["meiryo", "msgothic", "ms gothic", "yu gothic", "yugothic"]
    for path in font_dir.glob("*"):
        lower = path.name.lower()
        if any(term in lower for term in suspicious):
            warnings.append(f"possible OS-bundled font committed: {path.name}")


def check_image_definitions(errors: list[str]) -> None:
    images_text = read_text("game/images.rpy")
    required_defs = [
        "image bg lander_interior",
        "image bg shirowa_hab_ring",
        "image bg core",
        "image bg oxygen_workshop_r7",
        "image mio neutral",
        "image sena broken",
        "image noah tears",
        "image alma speaking",
    ]
    for image_def in required_defs:
        if image_def not in images_text:
            errors.append(f"missing image definition: {image_def}")


def check_manifest_assets(errors: list[str]) -> None:
    manifest = read_text("docs/ASSET_MANIFEST.md")
    paths = re.findall(r"(game/images/[^\s|]+\.png)", manifest)
    for path in paths:
        if not (ROOT / path).exists():
            errors.append(f"manifest asset missing: {path}")


def check_evidence_ids(errors: list[str]) -> None:
    evidence_text = read_text("game/evidence.rpy")
    script_text = read_text("game/script.rpy")
    for evidence_id in REQUIRED_EVIDENCE_IDS:
        if evidence_id not in evidence_text:
            errors.append(f"evidence id missing from evidence.rpy: {evidence_id}")
        if evidence_id not in script_text:
            errors.append(f"evidence id missing from script.rpy: {evidence_id}")


def check_screens_and_labels(errors: list[str]) -> None:
    screens_text = read_text("game/screens.rpy")
    script_text = read_text("game/script.rpy")

    defined_screens = set(re.findall(r"^screen\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", screens_text, re.MULTILINE))
    for screen_name in REQUIRED_SCREENS:
        if screen_name not in defined_screens:
            errors.append(f"required screen missing: {screen_name}")

    called_screens = set(re.findall(r"call\s+screen\s+([A-Za-z_][A-Za-z0-9_]*)", script_text))
    for screen_name in called_screens:
        if screen_name not in defined_screens:
            errors.append(f"script calls missing screen: {screen_name}")

    labels = set(re.findall(r"^label\s+([A-Za-z_][A-Za-z0-9_]*)(?:\s*\([^)]*\))?\s*:", script_text, re.MULTILINE))
    called_labels = set(re.findall(r"^\s*call\s+(?!screen\b)([A-Za-z_][A-Za-z0-9_]*)", script_text, re.MULTILINE))
    jumped_labels = set(re.findall(r"^\s*jump\s+([A-Za-z_][A-Za-z0-9_]*)", script_text, re.MULTILINE))
    for label_name in sorted(called_labels | jumped_labels):
        if label_name not in labels:
            errors.append(f"script references missing label: {label_name}")


def check_investigation_hub_routes(errors: list[str]) -> None:
    screens_text = read_text("game/screens.rpy")
    script_text = read_text("game/script.rpy")
    evidence_text = read_text("game/evidence.rpy")
    if "聞き込み対象" not in screens_text:
        errors.append("investigation hub missing visible heading: 聞き込み対象")
    for route in REQUIRED_INTERVIEW_RETURNS:
        if route not in screens_text:
            errors.append(f"investigation hub missing interview route: {route}")
    if "__back_to_investigation__" not in screens_text:
        errors.append("deduction screens missing route back to investigation hub")
    if "back_to_investigation" not in script_text:
        errors.append("script does not handle returning from final deduction to investigation hub")
    if "sync_story_evidence_for_chapter" not in evidence_text or "sync_story_evidence_for_chapter(5)" not in script_text:
        errors.append("story evidence sync is missing for final chapter recovery")


def check_names(errors: list[str], warnings: list[str]) -> None:
    combined = "\n".join(
        read_text(path)
        for path in ["README.md", "game/script.rpy", "game/evidence.rpy", "game/screens.rpy", "game/characters.rpy"]
    )
    for name in NEW_NAMES:
        if name not in combined:
            errors.append(f"new naming system term not found: {name}")
    for term in OLD_TERMS:
        if term in combined:
            warnings.append(f"old term remains: {term}")


def check_data_hygiene(warnings: list[str]) -> None:
    evidence_text = read_text("game/evidence.rpy")
    screens_text = read_text("game/screens.rpy")
    if '"acquired"' in evidence_text:
        warnings.append("evidence_catalog still contains acquired fields; use evidence_unlocked instead")
    if "第[chapter]章" in screens_text:
        warnings.append("screens.rpy may duplicate chapter numbers via 第[chapter]章")


def check_readme(errors: list[str]) -> None:
    readme = read_text("README.md")
    for term in ["Phase 3", "Phase 4", "通しプレイMVP", "git remote", "check_project_integrity.py", "GitHub Actions"]:
        if term not in readme:
            errors.append(f"README missing Phase 3 note: {term}")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    check_required_files(errors)
    if not errors:
        check_image_paths(errors)
        check_font_config(errors, warnings)
        check_image_definitions(errors)
        check_manifest_assets(errors)
        check_evidence_ids(errors)
        check_screens_and_labels(errors)
        check_investigation_hub_routes(errors)
        check_names(errors, warnings)
        check_data_hygiene(warnings)
        check_readme(errors)

    print("Project integrity check")
    print("=======================")
    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"  - {warning}")
    if errors:
        print("Errors:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("OK: no blocking integrity errors found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
