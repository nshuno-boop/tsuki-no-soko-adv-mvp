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
    "game/images.rpy",
    "docs/ASSET_MANIFEST.md",
    "docs/ART_DIRECTION.md",
    "docs/IMAGE_PROMPTS.md",
    "docs/PLAYTEST_CHECKLIST.md",
    "tools/generate_placeholder_assets.py",
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


def check_readme(errors: list[str]) -> None:
    readme = read_text("README.md")
    for term in ["Phase 3", "通しプレイMVP", "git remote", "check_project_integrity.py"]:
        if term not in readme:
            errors.append(f"README missing Phase 3 note: {term}")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    check_required_files(errors)
    if not errors:
        check_image_paths(errors)
        check_manifest_assets(errors)
        check_evidence_ids(errors)
        check_names(errors, warnings)
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

