# Midjourney Parameter Reference

Current as of mid-2026. Default model: **v8.1**. V7 remains selectable and is required for Omni Reference and Quality.

## Model selection

| Parameter | Notes |
|---|---|
| `--v 8.1` | Default. ~4–5× faster than v7, native 2048px HD output |
| `--v 7` | Full feature coverage: Omni Reference (`--oref`), Quality (`--q`) |
| `--niji 7` | Anime/manga specialist model |

## Core parameters

| Parameter | Range | Default | Purpose |
|---|---|---|---|
| `--ar W:H` | any ratio | 1:1 | Aspect ratio (`16:9`, `2:3`, `3:2`, `21:9`…) |
| `--s` / `--stylize` | 0–1000 | 100 | Strength of Midjourney's own aesthetic |
| `--chaos` | 0–100 | 0 | Variation between the 4 grid images |
| `--weird` | 0–3000 | 0 | Unconventional/offbeat aesthetics |
| `--exp` | 0–100 | 0 | Experimental aesthetics: detail, dynamics, tone-mapping. Sweet spot 10–25 |
| `--raw` | flag | off | Minimal AI aesthetic interpretation; more literal |
| `--no item, item` | list | — | Negative prompt (exclude things) |
| `--seed N` | number | random | Reproducibility |
| `--tile` | flag | off | Seamless pattern (textures, battle-map tiles) |

## Reference parameters

| Parameter | Range | Default | Purpose |
|---|---|---|---|
| `--sref <url or code>` | — | — | Style reference: transfer look of an image or numeric style code |
| `--sw` | 0–1000 | 100 | Style weight for `--sref` |
| `--oref <url>` | v7 only | — | Omni Reference: keep a subject/character consistent. Costs 2× GPU |
| `--ow` | 0–1000 | 100 | Omni weight: adherence to the reference subject |
| `--iw` | 0–2 | 1 | Image prompt weight (when prompt starts with image URLs) |
| `--p` | flag/code | off | Apply account personalization/moodboard |

## Speed / cost / resolution

| Parameter | Notes |
|---|---|
| `--draft` | 10× faster, half cost — exploration passes |
| `--hd` | v8.1 only: native 2048px (1.33 GPU-min) |
| `--sd` | v8.1 only: standard definition, lower cost |
| `--q 1/2/4` | v7 only: quality/GPU-time levels |

## Practical recipes (RPG use)

- **Scene splash for screen**: `--ar 16:9 --exp 10`
- **NPC portrait**: `--ar 2:3`, close or medium shot, single subject; add `--oref <portrait-url> --ow 200 --v 7` for recurrence
- **Aged handout/photo**: `--ar 3:2 --raw`, describe medium in prose ("scratched daguerreotype", "water-stained telegram")
- **Token/icon**: `--ar 1:1 --no background` or "on plain dark background"
- **Battle-map texture**: `--tile`, top-down description
- **Locking campaign style**: same style block every prompt + `--sref <best-image-url> --sw 200–400`

## Version gotchas

- `--oref` and `--q` silently require `--v 7` — appending them to a v8.1 prompt errors.
- `--exp` above ~50 fights with `--stylize`; keep one dominant.
- Style codes (`--sref 1234567890`) are model-version-sensitive; a code tuned on v7 renders differently on v8.1.
