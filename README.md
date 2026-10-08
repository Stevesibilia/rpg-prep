# rpg-prep

Pre-session toolkit for tabletop RPG game masters, distributed as Claude Code skills.

Five skills:

| Skill                    | What it does                                                                                                                                                                                                                                                                                             |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enhanced-avventure-rpg` | Session prep as situations, never PC scripts, in an Italian document built to be looked up at the table: at-a-glance block, clock, self-contained scenes, clue tracker (three clues per revelation), stat blocks, and `visual:`/`mood:` in an appendix. Ships `scripts/controlla.py` to check the output |
| `adventure-writing`      | Older guided adventure writing, kept for compatibility. Prefer `enhanced-avventure-rpg`                                                                                                                                                                                                                  |
| `storytelling`           | Narration technique advisor: description, NPC voices, pacing, tension, improv, spotlight                                                                                                                                                                                                                 |
| `midjourney-prompts`     | Scene/NPC → ready-to-paste Midjourney prompts (v8.1/v7 aware), campaign style consistency                                                                                                                                                                                                                |
| `suno-prompts`           | Scene mood → ready-to-paste Suno prompts (v5.5), session cue types, campaign sonic identity                                                                                                                                                                                                              |

The generator skills chain: `enhanced-avventure-rpg` (or `adventure-writing`) emits `visual:` and `mood:` fields per scene; `midjourney-prompts` and `suno-prompts` consume them.

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
  skills/*/SKILL.md                the five skills (+ references/, scripts/)
dist/                              packaged zips for claude.ai upload
```
