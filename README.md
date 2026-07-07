# rpg-prep

Pre-session toolkit for tabletop RPG game masters, distributed as Claude Code skills.

Four skills:

| Skill | What it does |
|---|---|
| `adventure-writing` | Guided adventure/one-shot writing. Produces a structured Italian GM document with per-scene `visual:`/`mood:` hooks |
| `storytelling` | Narration technique advisor: description, NPC voices, pacing, tension, improv, spotlight |
| `midjourney-prompts` | Scene/NPC → ready-to-paste Midjourney prompts (v8.1/v7 aware), campaign style consistency |
| `suno-prompts` | Scene mood → ready-to-paste Suno prompts (v5.5), session cue types, campaign sonic identity |

The three generator skills chain: `adventure-writing` emits `visual:` and `mood:` fields per scene; `midjourney-prompts` and `suno-prompts` consume them.

## Install

See [INSTALL.md](INSTALL.md) for detailed instructions covering Claude Code (plugin marketplace, local or GitHub, private repo OK), claude.ai web (zip upload from `dist/`), and the desktop/mobile apps (inherit claude.ai uploads). A public repo is not required.

Quick version for Claude Code:

```
/plugin marketplace add /home/steve/Homelab/fun/rpg-prep
/plugin install rpg-prep@rpg-prep
```

## Layout

```
.claude-plugin/marketplace.json    marketplace manifest
plugins/rpg-prep/
  .claude-plugin/plugin.json       plugin manifest
  skills/*/SKILL.md                the four skills (+ references/)
dist/                              packaged zips for claude.ai upload
```
