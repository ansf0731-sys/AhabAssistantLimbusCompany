from __future__ import annotations

import ast
from pathlib import Path

from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parents[1]
PRESET_PATH = ROOT / "tasks" / "mirror" / "select_theme_pack.py"
CATALOG_PATH = ROOT / "assets" / "config" / "theme_pack_list.example.yaml"


def _preset_targets():
    tree = ast.parse(PRESET_PATH.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        if any(isinstance(target, ast.Name) and target.id == "floor_targets" for target in node.targets):
            return ast.literal_eval(node.value)
    raise AssertionError("select_theme_pack.py is missing floor_targets")


def test_dawn_black_beast_floor_keywords_exist_in_catalog() -> None:
    catalog = YAML().load(CATALOG_PATH.read_text(encoding="utf-8"))
    targets = _preset_targets()
    sections = {
        1: ("theme_pack_list_cn", "theme_pack_list"),
        2: ("theme_pack_list_cn", "theme_pack_list"),
        3: ("theme_pack_list_cn", "theme_pack_list"),
        4: ("theme_pack_list_cn", "theme_pack_list"),
        5: ("theme_pack_list_hard_cn", "theme_pack_list_hard"),
    }

    assert set(targets) == {1, 2, 3, 4, 5}
    for floor, (zh_targets, en_targets) in targets.items():
        zh_section, en_section = sections[floor]
        missing_zh = set(zh_targets) - set(catalog[zh_section])
        missing_en = set(en_targets) - set(catalog[en_section])
        assert not missing_zh, f"Floor {floor} Chinese keywords missing: {sorted(missing_zh)}"
        assert not missing_en, f"Floor {floor} English keywords missing: {sorted(missing_en)}"
