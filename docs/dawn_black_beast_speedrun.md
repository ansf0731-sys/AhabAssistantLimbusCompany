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
3. Preserve **成捆的符咒 + 荆棘套索 + 标准负载电池** as the ingredients for the level-IV **快感** (Enrapturing Trance) fusion. The documented recipe uses those three gifts; they must not be consumed by unrelated generic fusion.
4. Target **雷击木 III** as a separate rupture gift, and enhance it only to the guide's required level. The guide's screenshot labels this as a manual synthesis step; its exact material combination still needs to be mapped to the repository's current formula templates.
5. If the second-floor **地狱鸡无事事件** gives/uses **鸡胸肉**, handle that event reward as a separate high-priority target.
6. Two additional **level-IV slash gifts** may be synthesized as supplementary gifts, but this is optional and lower priority than the core gifts.
7. Complete the required shop operations no later than the bottom of floor four.


The preset now reuses AALC's existing shop workflow rather than reimplementing it. It locks the runtime team system to **rupture** (without changing the saved team config), forces conservative ordinary fusion (not aggressive fusion), and enables the existing purchase, ordinary fusion, rupture formula fusion, and enhancement stages. It disables selling and skips no shop floors for this run; it also disables the optional second-system route and post-level-IV shop shortcut. The existing unfiltered purchase path considers both AALC's must-buy items and rupture-system shop gifts. All overrides are runtime-only; the user's saved team config is not rewritten. No second click/coordinate system is introduced.

The guide's skill-exchange plan is wired into the existing OCR-based skill replacement: Faust and Sinclair use 1→2 on floors 1–2, then 1→3 from floor 3 onward; Outis uses 2→3; other selected sinners use 1→3. The preset enables skill replacement for all selected sinners. This mapping assumes the guide's shorthand “菲辛” means Faust + Sinclair and “兔奥” means Rabbit Outis. AALC's existing skill selector recognizes sinner slots, not the equipped Identity name, so the selected Outis slot receives 2→3 even if a non-Rabbit Outis Identity is equipped; the preset does not independently verify Identity ownership. The runtime floor number is passed into the existing shop handler so the rule changes at floor 3.

However, the existing routines are system-oriented and generic: `buy_gifts()` buys rupture-system gifts; `fuse_useless_gifts()` fuses gifts classified by the repository's `must_be_abandoned` templates; `fuse_system_gifts()` uses rupture formula-result templates; and `enhance_gifts()` enhances gifts recognized by the rupture templates. The known 快感 IV recipe is 成捆的符咒 + 荆棘套索 + 标准负载电池, but current AALC code does **not** explicitly reserve these three ingredients or prove which `rupture_hard_*` result template corresponds to 快感. It also does not guarantee 雷击木 III or explicitly protect chicken breast and all other named guide gifts. Do not interpret enabling ordinary fusion as a guarantee that these named targets will be made.

## Shop operation

The preset runs the existing shop at every floor, does not sell gifts, performs ordinary (non-aggressive) fusion, performs rupture formula fusion, enables enhancement, and enables the floor-aware skill-exchange plan. It keeps the existing refresh limits from the user's team settings. AALC runs its shop handler when it reaches each shop; the current code does not have a separate timer/deadline that can prove all purchases and target gifts are complete by the floor-four bottom. Exact target gift completion is still unverified.

## Fifth-floor event-pack compatibility

The existing fifth-floor event-pack settings are deliberately preserved:

- When `select_event_pack` is enabled, the existing special handler still selects the leftmost event pack before ordinary priority matching.
- When `skip_event_pack` is enabled, the existing selector still excludes the leftmost event pack and evaluates the remaining packs.
- Otherwise, the normal OCR/weight selector runs with the fifth-floor `转困牢 2号线 / line` priority when that keyword exists in the active difficulty's pack list.

The preset is opt-in and does not change other teams or the default selection behavior.

## Validation status

The branch contains the opt-in team setting, floor-specific theme-pack priority, opening star-bonus selection, a runtime rupture-system lock, runtime shop defaults that reuse AALC's existing buy/fuse/formula-fuse/enhance stages without selling, and per-sinner floor-aware skill replacement. No existing shop click/refresh/fusion/enhancement mechanism has been rewritten. The existing formula templates are system-level, not proof of exact named target outputs; target-specific gift acquisition, ingredient reservation and deterministic 快感 IV fusion, exact 雷击木 III recipe enforcement, explicit protection of all named gifts, a verified floor-four completion deadline, and live-game execution remain unimplemented or unverified. Do not treat the preset as a fully autonomous execution of the entire guide yet.
