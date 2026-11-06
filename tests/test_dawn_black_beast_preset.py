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



def test_dawn_black_beast_skill_modes_follow_floor_and_sinner() -> None:
    shop_path = ROOT / "tasks" / "mirror" / "in_shop.py"
    tree = ast.parse(shop_path.read_text(encoding="utf-8"))
    shop_class = next(node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == "Shop")
    method = next(
        node
        for node in shop_class.body
        if isinstance(node, ast.FunctionDef) and node.name == "_dawn_black_beast_skill_mode"
    )
    isolated = ast.Module(body=[method], type_ignores=[])
    namespace: dict[str, object] = {}
    exec(compile(ast.fix_missing_locations(isolated), str(shop_path), "exec"), namespace)
    choose_mode = namespace["_dawn_black_beast_skill_mode"]

    class FakeShop:
        current_layer = 1

    shop = FakeShop()
    for floor in (1, 2):
        shop.current_layer = floor
        assert choose_mode(shop, "Faust") == 2
        assert choose_mode(shop, "Sinclair") == 2
    for floor in (3, 4, 5):
        shop.current_layer = floor
        assert choose_mode(shop, "Faust") == 0
        assert choose_mode(shop, "Sinclair") == 0
    assert choose_mode(shop, "Outis") == 1
    assert choose_mode(shop, "Gregor") == 0
