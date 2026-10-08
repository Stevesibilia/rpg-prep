---
name: suno-prompt-creator
description: Create optimized music prompts for Suno AI. Use this skill whenever the user wants to generate music, songs, soundtracks, jingles, background music, theme songs, or any audio content using Suno AI. Triggers include any mention of 'Suno', 'AI music', 'music prompt', 'song prompt', 'soundtrack', 'theme song', 'sigla', 'jingle', 'background music', 'ambient music', 'loop music', or requests to create music for videos, games, podcasts, comics, animations, or any creative project. Also use when the user asks to write lyrics with structure tags, create a music style description, or wants help formatting prompts for AI music generation. Even if the user doesn't mention Suno by name but asks for help creating or describing a song, use this skill.
---

# Suno Prompt Creator

A skill for generating ready-to-paste prompts for Suno AI's music generation interface.

## Suno Interface Overview

Suno has two creation modes that determine which fields are available:

### Instrumental Mode (no vocals)
When the user toggles off lyrics or wants instrumental-only tracks, Suno shows a single field:
- **Description** — a style prompt (max ~200 characters) describing genre, mood, instruments, tempo, and atmosphere.

In this mode, do NOT provide lyrics or any vocal/voice references anywhere. Everything goes into Description.

### Vocal Mode (with lyrics)
When the user wants a song with vocals, Suno shows these fields:
- **Styles** — the musical style prompt (max ~200 characters): genre, mood, instruments, vocal style, tempo, era.
- **Lyrics** — the song text with structure tags and lyric lines.
- **Title** — the song title.

There is NO separate "song description" field. All musical direction goes into Description (instrumental) or Styles (vocal).

---

## PART 1 — Structure Prompt (Lyrics Field)

The structure prompt is a sequence of `[bracket tags]` that tell Suno what each section sounds and feels like. This is the most powerful control mechanism in Suno — it shapes the entire dynamic arc of the song.

### The One Unbreakable Rule: Bracket Format

Every bracket tag occupies exactly one line by itself. A bracket contains one section word and at most one modifier. No commas ever appear inside a bracket.

**WRONG — never produce these:**
```
[intro, slow build, synth pad]
[dark intro] [bass intro]
[slow, dark intro]
```

**CORRECT — one tag per line, one modifier max:**
```
[slow intro]
[dark intro]
[synth pad intro]
[bass intro]
```

### Section Words

Use only these as the section word inside a bracket:

`intro` | `verse` | `verse 1` | `verse 2` | `verse 3` | `pre-chorus` | `chorus` | `bridge` | `solo` | `break` | `drop` | `build` | `transition` | `outro` | `end`

### Modifiers

A modifier is an instrument name, a tempo word, a mood adjective, a style word, or a compositional term. It appears BEFORE the section word.

**Valid modifier examples:**
```
[slow intro]  [dark chorus]  [bass drop]
[synth pad intro]  [hypnotic verse]  [explosive drop]
[electric piano verse]  [ostinato outro]  [four-on-the-floor chorus]
[driven build]  [spoken word verse]  [atmospheric bridge]
```

**Forbidden modifiers** — production adjectives that describe how an instrument is processed do NOT work as standalone structure modifiers:
```
✗ [filtered intro]  ✗ [sidechained verse]  ✗ [punchy chorus]
```
These belong in the Styles/Description field attached to their instrument. Use the instrument name instead: `[bass intro]`, `[synth intro]`.

### Reinforcement Through Redundancy

Use 3–6 tags per section. Each tag reinforces one dimension of that section (energy, instrument, mood, tempo). Suno reads all tags together to build the section's sound. This is intentional, not repetition.

**Example — a dark electronic intro:**
```
[slow intro]
[dark intro]
[synth pad intro]
[atmospheric intro]
```

**Example — an explosive chorus:**
```
[loud chorus]
[driving chorus]
[full band chorus]
[four-on-the-floor chorus]
```

### Voice and Vocal Tags

**Vocal mode:** Add voice tags to relevant sections: `[vocal chorus]`, `[spoken word verse]`, `[female vocal verse]`. After the tags for each section, include the actual lyric lines.

**Instrumental mode:** Do NOT include any voice, vocal, spoken word, or singing tags anywhere. Zero exceptions.

### Song Theory Arc

Build a coherent dynamic arc. Not every section should be the same energy level:

- **intro** → establish palette, lower energy, set the mood
- **verse** → develop theme, medium energy
- **pre-chorus** → build tension, rising energy
- **chorus** → peak energy, climactic, most intense
- **bridge** → contrast, fresh angle, often strips back
- **break/drop** → breakdown followed by explosive re-entry
- **solo** → showcase the lead instrument named in the Styles field
- **outro** → mirror and resolve the intro, fade or hard stop

### Closing Tag

The very last line of the structure must always be `[end]`.

---

## PART 2 — Style/Description Prompt

The style prompt has a ~200 character limit. Every word counts. Suno weighs earlier tags more heavily.

### Organizing the Style Prompt

Think of the style prompt as having these internal layers, ordered by priority:

1. **Genre/era** (first) — the foundation: `1950s noir jazz`, `synthwave`, `folk rock`
2. **Key instruments** — with specific adjectives attached: `gritty analog bass`, `muted trumpet`, `sidechained synth stabs`
3. **Mood/energy** — emotional direction: `melancholic`, `hypnotic rhythm`, `explosive drops`
4. **Vocal style** (vocal mode only) — `smoky baritone`, `warm female voice`, `spoken word delivery`
5. **Production/feel** — finishing touches: `lo-fi`, `cinematic`, `vinyl crackle`
6. **Tempo** — use BPM for precision: `70 BPM`, `140 BPM`

### Instrument Descriptions

Be specific about instruments. Production adjectives (filtered, sidechained, gritty, punchy, sweeping) belong HERE attached to their instrument — not in bracket tags and not as standalone genre words.

**Good:** `gritty analog bass, sidechained synth stabs, sharp hi-hats, filtered disco samples, sweeping risers`

**Bad:** `bass, synths, hi-hats, samples, risers`

### Coherence Rule

Every instrument named in the style prompt should appear as a modifier in at least 2 structure tags. Mood words must match the emotional arc of the structure. If the structure contains a `[solo]` section, name a specific lead instrument suitable for soloing.

### Style Prompt Best Practices

- Keep it to 4–7 descriptors. More confuses the model.
- Shorter prompts produce cleaner audio; long prompts risk sounding narrow and repetitive.
- Use comma-separated tags, not sentences.
- Describe what you want, not what you don't want.
- For instrumental tracks, end with `no vocals, instrumental`.
- For loopable tracks, add `seamless loop, consistent dynamics` and avoid tags that imply dramatic builds.
- Hybrid genres work well: `jazz-infused trip hop`, `cinematic hip hop`.
- Era references are powerful: `1950s`, `80s`, `90s` dramatically change production style.
- Don't repeat the same idea in different words (`sad, melancholic, sorrowful` — pick one).
- Don't exceed ~200 characters; Suno truncates beyond that.

---

## Output Format

Always provide output as ready-to-copy code blocks, clearly labeled by field name. The user should be able to copy-paste directly into Suno without editing. All text inside the code blocks must be lowercase.

### For Instrumental Tracks

```
**Title:**
[title here]

**Description:**
[style tags, under 200 chars, ending with "no vocals, instrumental"]

**Structure (paste in Lyrics field if available, otherwise omit):**
[full bracket structure ending with [end]]
```

If the user confirmed they have NO lyrics field (instrumental toggle), provide only Title and Description. If they do have the lyrics field available, include the Structure as well — it dramatically improves results.

### For Vocal Tracks

```
**Title:**
[title here]

**Styles:**
[style tags, under 200 chars, including vocal style]

**Lyrics:**
[bracket tags + lyric lines for each section, ending with [end]]
```

---

## Practical Tips to Share with Users

- Generate 5–10 variations per prompt. Tweak the style prompt slightly between generations — swap a mood word, try a different instrument.
- For loop/background music: pick the generation with the most consistent dynamics (no dramatic swells or silences).
- For action/tense scenes: look for aggressive rhythm and driving bass.
- For ambient/atmospheric: look for space between notes — silence is part of the music.
- Suno generates clips of ~1–2 min. Use the Extend feature to build longer tracks.
- The Covers feature can restyle a generated track into a different genre.

---

## Example Prompts

### Noir Jazz — Detective Theme (Instrumental)

**Title:**
```
shadows on 5th avenue
```

**Description:**
```
1950s noir jazz, smoky muted trumpet, walking upright bass, soft brushed snare, cinematic, melancholic, slow swing, no vocals, instrumental
```

**Structure:**
```
[slow intro]
[dark intro]
[muted trumpet intro]
[upright bass verse]
[brushed snare verse]
[melancholic verse]
[dark bridge]
[atmospheric bridge]
[sparse bridge]
[muted trumpet solo]
[slow solo]
[upright bass outro]
[dark outro]
[slow outro]
[end]
```

### Electro House — Dark Club Track (Instrumental)

**Title:**
```
midnight protocol
```

**Description:**
```
dark electro house, gritty analog bass, sidechained synth stabs, sharp hi-hats, punchy claps, sweeping risers, hypnotic, 128 BPM, no vocals, instrumental
```

**Structure:**
```
[synth pad intro]
[slow intro]
[atmospheric intro]
[bass verse]
[hi-hat verse]
[hypnotic verse]
[driven build]
[synth stab build]
[bass drop]
[explosive drop]
[four-on-the-floor chorus]
[driving chorus]
[synth stab chorus]
[atmospheric bridge]
[sparse bridge]
[bass build]
[explosive drop]
[driving chorus]
[synth pad outro]
[slow outro]
[end]
```

### Indie Folk — Campfire Ballad (Vocal)

**Title:**
```
miles from home
```

**Styles:**
```
indie folk, fingerpicked acoustic guitar, gentle harmonica, warm male vocals, nostalgic, campfire feel, 90 BPM
```

**Lyrics:**
```
[slow intro]
[acoustic guitar intro]
[atmospheric intro]

[acoustic guitar verse]
[warm verse]
[vocal verse]
the road stretched out like a promise
dust and gravel under my shoes
i left the porch light burning
knowing i had nothing to lose

[driven build]
[rising pre-chorus]

[full band chorus]
[vocal chorus]
[loud chorus]
i'm miles from home but i'm not lost
just walking where the rivers run
every bridge i burn still keeps me warm
underneath a fading sun

[acoustic guitar verse]
[warm verse]
[vocal verse]
the diner closed at midnight
coffee cold and words unsaid
a stranger smiled across the counter
and i remembered what you said

[full band chorus]
[vocal chorus]
[loud chorus]
i'm miles from home but i'm not lost
just walking where the rivers run
every bridge i burn still keeps me warm
underneath a fading sun

[harmonica solo]
[slow solo]

[acoustic guitar outro]
[slow outro]
underneath a fading sun
[end]
```

### Tension / Suspense — Soundtrack (Instrumental)

**Title:**
```
something in the walls
```

**Description:**
```
dark cinematic suspense, dissonant strings, sparse piano, low drone bass, eerie atmosphere, slow tempo, tense, 60 BPM, no vocals, instrumental
```

**Structure:**
```
[slow intro]
[dark intro]
[drone bass intro]
[sparse piano verse]
[dissonant strings verse]
[eerie verse]
[tense build]
[slow build]
[strings build]
[dark chorus]
[dissonant strings chorus]
[drone bass chorus]
[sparse bridge]
[piano bridge]
[atmospheric bridge]
[tense build]
[dark chorus]
[eerie outro]
[slow outro]
[drone bass outro]
[end]
```
