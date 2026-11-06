# Dawn Black Beast speedrun preset

Enable **黎明黑兽速刷预设（逐层卡包优先级）** in the team settings to activate the floor-specific theme-pack priorities and the opening star-bonus selection.

## Floor-by-floor route

| Floor | Preferred theme-pack keyword | Guide requirement |
| --- | --- | --- |
| 1 | 赌徒 / 遗忘 (gambl / forgot) | Prefer the pack whose bottom preview contains bundled talismans; the guide names “身无分文的赌徒 / 被遗忘者们”. |
| 2 | 地狱鸡 (chick) | Prefer the Hell Chicken pack; if the chicken-breast reward/event appears, handle the manual synthesis described below. |
| 3 | 当斩 (cleaved) | Prefer the “当斩之物” pack. |
| 4 | 憎恶与绝望 (Hatred / despair) | Prefer the “憎恶与绝望” pack. |
| 5 | 转困牢 2号线 (line) | Prefer the hard-mode 2号线 pack when no event-pack override is active. |

The preset changes only the in-memory priority for the current floor. It does not overwrite the user's global or per-team theme-pack weight YAML files. If the current language's keyword is not present in the loaded theme-pack list, the selector logs a warning and falls back to the existing weights.

## Opening star bonuses

The preset selects star-bonus positions **1, 3, and 10** for this run. It does not modify the saved team configuration.

## Gift and shop route from the supplied guide image

The supplementary guide image specifies the following target state and ordering:

1. Obtain **成捆的符咒** from the first-floor bottom reward.
2. Obtain **标准负载电池** through star-bonus **增益 10**.
3. Manually synthesize **快感** to level **IV** and **雷击木** to level **III**. These are the core gift targets.
4. If the second-floor **地狱鸡无事事件** gives/uses **鸡胸肉**, manually synthesize it as instructed by the guide.
5. Two additional **level-IV slash gifts** may be synthesized as supplementary gifts, but this is optional and lower priority than the core gifts.
6. Complete the required shop operations no later than the bottom of floor four.

The preset now reuses AALC's existing shop workflow rather than reimplementing it. If the team has left the shop strategy at its default “出售” value (0), enabling this preset switches the runtime strategy to ordinary fusion (1). An explicitly selected ordinary-fusion or level-IV-priority strategy is preserved. This activates the existing purchase, generic fusion, formula-gift fusion, and enhancement routines; it does not introduce a second click/coordinate system.

However, the existing routines are system-oriented and generic: `buy_gifts()` buys system gifts according to the configured team system and shopping strategy; `fuse_useless_gifts()` fuses gifts already classified by the repository's `must_be_abandoned` templates; `fuse_system_gifts()` uses the repository's formula-result templates for the selected system; and `enhance_gifts()` enhances gifts recognized by the selected system's templates. They do **not** yet prove a specific recipe or guarantee the exact target levels 快感 IV and 雷击木 III, nor do they explicitly protect all five named guide gifts. The first-floor bundled talisman, standard load battery, chicken-breast event, and exact target fusion remain unverified. Do not interpret enabling ordinary fusion as a guarantee that these named targets will be made.

## Shop operation

The guide's shop policy remains a required part of the route: finish the necessary operations before the floor-four bottom. The repository's existing generic shop controls (purchase/fuse/enhance/refresh and sinner skill replacement) remain available, but the preset does not yet override their per-sinner exchange counts or enforce a floor-four deadline. Configure/monitor those actions manually until a dedicated, tested route controller is implemented.

## Fifth-floor event-pack compatibility

The existing fifth-floor event-pack settings are deliberately preserved:

- When `select_event_pack` is enabled, the existing special handler still selects the leftmost event pack before ordinary priority matching.
- When `skip_event_pack` is enabled, the existing selector still excludes the leftmost event pack and evaluates the remaining packs.
- Otherwise, the normal OCR/weight selector runs with the fifth-floor `转困牢 2号线 / line` priority when that keyword exists in the active difficulty's pack list.

The preset is opt-in and does not change other teams or the default selection behavior.

## Validation status

The branch contains the opt-in team setting, floor-specific theme-pack priority, opening star-bonus selection, and a runtime fallback to AALC's existing ordinary shop-fusion strategy when the user's shop strategy is still at its default. No existing shop click/refresh/fusion/enhancement mechanism has been rewritten. Target-specific gift recognition, exact recipe/level enforcement, explicit protection of every named guide gift, sinner-by-sinner exchange counts, the floor-four deadline, and live-game execution remain unimplemented or unverified. Do not treat the preset as a fully autonomous execution of the entire guide yet.
