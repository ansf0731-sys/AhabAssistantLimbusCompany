# Dawn Black Beast speedrun preset

Enable **黎明黑兽速刷预设（逐层卡包优先级）** in the team settings to activate the floor-specific theme-pack priorities.

| Floor | Preferred theme-pack keyword |
| --- | --- |
| 1 | 赌徒 / 遗忘 (gambl / forgot) |
| 2 | 地狱鸡 (chick) |
| 3 | 当斩 (cleaved) |
| 4 | 绝望 / Hatred |
| 5 | 号线 / line (the hard-mode 2号线 pack) |

The preset changes only the in-memory priority for the current floor. It does not overwrite the user's global or per-team theme-pack weight YAML files. If the current language's keyword is not present in the loaded theme-pack list, the selector logs a warning and falls back to the existing weights.

## Fifth-floor event-pack compatibility

The existing fifth-floor event-pack settings are deliberately preserved:

- When `select_event_pack` is enabled, the existing special handler still selects the leftmost event pack before ordinary priority matching.
- When `skip_event_pack` is enabled, the existing selector still excludes the leftmost event pack and evaluates the remaining packs.
- Otherwise, the normal OCR/weight selector runs with the fifth-floor `号线 / line` priority when that keyword exists in the active difficulty's pack list.

The preset is opt-in and does not change other teams or the default selection behavior.
