# Suno Syntax Reference

Current as of mid-2026. Flagship model: **v5.5** (Voices, Custom Models, My Taste personalization on top of v5's audio quality).

## The three control systems

1. **Style field** — the sound world: genre, tempo feel, instruments, vocal lane, production, mood. Natural language, 4–7 descriptors is the sweet spot. Most-important descriptors first: weight decays after the first ~20–30 words.
2. **Lyrics field** — structure and per-section behavior via meta tags in `[square brackets]`, plus actual lyrics if any.
3. **Creative sliders** — Weirdness (structure conventionality), Style Influence (how strictly style descriptors are honored), Audio Influence (for audio-input features).

## Meta tags

### Structural

| Tag | Effect |
|---|---|
| `[Intro]` | opening section |
| `[Verse]`, `[Verse 1]` | narrative section |
| `[Chorus]` | hook/refrain |
| `[Bridge]` | contrasting section |
| `[Outro]` | closing section |
| `[End]` | hard stop — ALWAYS include to prevent trailing audio |

### Instrumental / dynamics

| Tag | Effect |
|---|---|
| `[Instrumental]` | vocal-free section |
| `[Instrumental Break]` | vocal-free interlude |
| `[Piano Solo]`, `[Guitar Solo]`… | featured instrument passage |
| `[Strings Rise]`, `[Crescendo]` | swell/build |
| `[Build]`, `[Drop]` | energy shifts |
| `[Fade In]` / `[Fade Out]` | gradual volume |
| `[Silence]` | brief pause |

### Vocal (when vocals wanted)

| Tag | Effect |
|---|---|
| `[Male Vocal]` / `[Female Vocal]` | vocal gender |
| `[Whisper]`, `[Spoken Word]` | delivery |
| `[Choir]`, `[Harmonies]` | ensemble vocals |

Vocal tags work in both Style and Lyrics fields. In Lyrics, place directly before the section they modify; in Style, they apply globally.

### Parameterized tags (per-section control)

```
[Verse: sparse, ambient pads, reverb-heavy]
[Bridge: stripped down, piano only]
[Outro: fade out, ambient reprise]
```

Free-text instructions after the colon. This is the main tool for shaping instrumental cues.

## Tag budget

Too many tags confuse the model. Per generation: 1–2 genre tags, 2–3 instruments, 1–2 mood/energy words, structure tags only at section changes. More than 3–4 named instruments produces inconsistent renders.

## Fully instrumental recipe

Belt and suspenders — all three:
1. Instrumental toggle ON (Custom Mode)
2. `[Instrumental]` tag in Lyrics field
3. "vocals" in the Exclude field (Advanced Options)

Plus: no vocal descriptors in Style.

## Sliders for score work

- **Weirdness**: low-to-center → conventional structure, predictable genre adherence. Raise only for ritual/eldritch cues.
- **Style Influence**: high/strong → descriptors honored strictly. Ambient briefs need this; Suno drifts upbeat otherwise.

## Extend workflow

Generate the core section first (best 1–2 minutes), then Extend with new meta tags for additional movements. Extension preserves musical continuity better than prompting one long piece. Useful for: combat tracks with phases, boss music with a final-form shift.

## Common failure modes

| Symptom | Fix |
|---|---|
| Trailing noise/garbage at end | `[Outro: fade out]` then `[End]` |
| Cheerful when brief said dark | double dark mood words, raise Style Influence |
| Vocals despite instrumental intent | apply all three instrumental controls above |
| Wall of sound, no space | "sparse, minimal, slowly evolving" + cut instrument list to 2 |
| Style descriptors ignored | move them into first 20 words of Style field |
| Inconsistent between generations | more specific descriptors — each one constrains a dimension |
