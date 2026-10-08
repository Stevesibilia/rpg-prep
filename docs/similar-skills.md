# Similar skills

Agent skills for tabletop RPGs found on GitHub while designing `enhanced-avventure-rpg`, `campagna-rpg` and `revisione-avventura` (October 2026), with what each one does and what was borrowed from it. Found with `gh search code --filename SKILL.md` on terms such as "game master", "TTRPG", "dungeon master", "one-shot adventure", "secrets and clues", "scene framing", "NPC voice", "narration".

None of them is in Italian, and none of them forbids writing PC actions as strictly as the golden rule of `avventure-gdr` and its successors.

## Read in depth

### Session and adventure prep

| Skill                          | Repo                                                                                            | What it is                                                                                                                                                                                                        | Borrowed                                                                                                                                                                                                                                                                     |
| ------------------------------ | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ttrpg-session-prep`           | [AtomHeartFylus/ttrpg-campaign-skills](https://github.com/AtomHeartFylus/ttrpg-campaign-skills) | The most rigorous prep skill found: a self-sufficient running sheet built for an Obsidian vault and a campaign profile, 15 principles, references for scene anatomy, a red team pass and a worked example. 1 star | Two levels of reminders (evening-wide box, per-scene box), read-aloud with senses only, GM-only notes kept apart, derailment prediction with consequences instead of walls, optional scenes and a named first cut, a quiet conversation scene, worked example as calibration |
| `ttrpg-session-forge`          | [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills)             | One-page session plan, "situations not plots", in a popular general-purpose skill collection (about 1.4k stars)                                                                                                   | NPC card with the one line they would say, a name bank, the derailment ladder, never inventing stat blocks for named systems, session-zero safety tools                                                                                                                      |
| `dnd-campaign-starter`         | [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills)             | Premise, hook, session zero and a first adventure for a new campaign or one-shot                                                                                                                                  | Session-zero kit (tone, boundaries, safety tools, expectations)                                                                                                                                                                                                              |
| `dungeon-master-assistant`     | [NylasDev/nylas-dungeon-master-skills](https://github.com/NylasDev/nylas-dungeon-master-skills) | Generic co-DM with output formats for NPCs, encounters, factions, rumour tables and session prep                                                                                                                  | Scene table (purpose, pressure, exits), faction clocks, "make a labelled assumption instead of asking when the answer would not change the output"                                                                                                                           |
| `ttrpg-expert`, `session-prep` | [AntTheLimey/gm-apprentice](https://github.com/AntTheLimey/gm-apprentice)                       | Rules engine and content generator for five systems, with session plan and scene note templates                                                                                                                   | NPC quick-reference table, a word budget before the first scene, fail-forward patterns, yes-and / yes-but / no-but table                                                                                                                                                     |

### Campaign and story design

| Skill                | Repo                                                                                                  | What it is                                                                                                                 | Borrowed                                                                                                                                                                              |
| -------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ttrpg-campaign-arc` | [AtomHeartFylus/ttrpg-campaign-skills](https://github.com/AtomHeartFylus/ttrpg-campaign-skills)       | A living arc note above the session: backbone, deviation ledger, thread tracker, pacing, seeded endgame. Refuses one-shots | Arcs as functions with session ranges and a first cut, thread tracker with "lost" as a legitimate status, endings planted early in a named arc, one-shots left to the session skill   |
| `ttrpg-storytelling` | [vezril/claude-toolkit](https://github.com/vezril/claude-toolkit)                                     | A digest of four web guides on TTRPG storytelling, covering prep and table craft                                           | The 5 C's check (character, conflict, context, climax, change), the four conflict axes, a villain with a plan and a goal, Bang Bank, a diagnosis table for games that are not working |
| `ttrpg-narrative`    | [GabrielMartinMoran/cairil-ttrpg-setting](https://github.com/GabrielMartinMoran/cairil-ttrpg-setting) | Spanish-language narrative skill for one homebrew setting and its vault                                                    | World timelines that run without the PCs; never inventing facts that are not in the context                                                                                           |

### Narration and table craft

Studied for an improved `storytelling` skill, which was then dropped.

| Skill                                     | Repo                                                                                | What it is                                                                                                                                                         |
| ----------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `theatre-of-the-mind`                     | [Thedougler/ai-co-dm](https://github.com/Thedougler/ai-co-dm)                       | Strict rules for all player-facing prose: every description includes everything players can act on, every sentence changes the picture or the options, plain words |
| `gm-craft`                                | [Sstobo/Claude-Code-Game-Master](https://github.com/Sstobo/Claude-Code-Game-Master) | Narration guidance for an agent that runs the game: length matched to drama, silence, amplifying a player's flourish, NPCs with contradictions                     |
| `ironsworn-npc-voice`, `ironsworn-pacing` | [karimn/agentic-rpg](https://github.com/karimn/agentic-rpg)                         | Ironsworn-specific: NPC voice continuity read from the record before speaking; montage by default, zoom in only when it matters                                    |
| `dm-narrate`                              | [johncarpenter/dnd-dm-tools](https://github.com/johncarpenter/dnd-dm-tools)         | Short narration rules for a family D&D game: two or three senses, three or four sentences, end on "what do you do?"                                                |
| `trpg-live-aid`                           | [zeteticl/trpg-session-skills](https://github.com/zeteticl/trpg-session-skills)     | Chinese-language run sheet: scene order, music cue order and handout reveals, each citing the module page                                                          |

### Story and plot review

Studied for `revisione-avventura`.

| Skill                                | Repo                                                                                            | What it is                                                   | Borrowed                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------ | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `continuity-engine`, `campaign-qa`   | [AntTheLimey/gm-apprentice](https://github.com/AntTheLimey/gm-apprentice)                       | Plot-hole detection and campaign QA over a notes vault       | The plot-hole categories (timeline, knowledge, motivation, causal gap, orphaned thread, dead-end clue, agency violation, canon fabrication, premature access); clue paths checked against the Three Clue Rule, including "what if no PC has the skill"; their note that an automatic "PC as subject" scan was dropped for false positives |
| `plot-hole-auditing`                 | [bflandev/script-doctor](https://github.com/bflandev/script-doctor)                             | Screenwriting root-cause analysis                            | Name the symptom precisely, ask "why?" at least three levels back, fix at the root, then check for collateral damage                                                                                                                                                                                                                      |
| `ttrpg-continuity-audit`, `red-team` | [AtomHeartFylus/ttrpg-campaign-skills](https://github.com/AtomHeartFylus/ttrpg-campaign-skills) | Campaign continuity audit and derailment prediction          | Every finding carries evidence; the audit proposes and the GM decides; likely derailments answered with consequences, not walls                                                                                                                                                                                                           |
| `story-critic`                       | [heaversm/ralph-storywriter](https://github.com/heaversm/ralph-storywriter)                     | Developmental editing of prose chapters                      | Pacing checks (sagging middle), earned change, knowledge and travel-time consistency                                                                                                                                                                                                                                                      |
| `ttrpg-writing`                      | [Thedougler/agent-skills](https://github.com/Thedougler/agent-skills)                           | Writing standards for GM-facing and player-facing TTRPG text | Two audiences with opposite rules: GM reference text must give something to say, do or decide; read-aloud is prose                                                                                                                                                                                                                        |

Other review skills found but not read: `plot-consistency-checker` (several copies in skill marketplaces such as [aiskillstore/marketplace](https://github.com/aiskillstore/marketplace)), `plot-hole-detection` in [AndrasSama/dsh-omp-advisor](https://github.com/AndrasSama/dsh-omp-advisor), `story-editor` in [heaversm/ralph-storywriter](https://github.com/heaversm/ralph-storywriter), `dnd-adventure-design` in [johnalexwelch/wren](https://github.com/johnalexwelch/wren). None simulates different tables playing the adventure; that part of `revisione-avventura` has no direct model.

## Found but not read in depth

Listed for completeness; most are agent-run games (the AI is the GM) rather than tools for a human GM.

- [AtomHeartFylus/ttrpg-campaign-skills](https://github.com/AtomHeartFylus/ttrpg-campaign-skills): also `ttrpg-entity-note`, `ttrpg-session-log`
- [Bobby-Gray/open-tabletop-gm](https://github.com/Bobby-Gray/open-tabletop-gm)
- [camauger/ludomancien-skills](https://github.com/camauger/ludomancien-skills): `encounter-builder`, `ttrpg-print-design`
- [erikzaadi/dnd-fam-ftw](https://github.com/erikzaadi/dnd-fam-ftw): `dnd-adventure`
- [FerroxLabs/murage](https://github.com/FerroxLabs/murage): `create-tabletop-rpg`, `dnd-master`, `tabletop-rpg-designer`
- [gttdo/DM-5e-SKILL](https://github.com/gttdo/DM-5e-SKILL)
- [h34tsink/FATE-Nova-Praxis](https://github.com/h34tsink/FATE-Nova-Praxis): `narrative-humanizer`
- [johnalexwelch/wren](https://github.com/johnalexwelch/wren): `dnd-session-prep`
- [kino-6/black-stela](https://github.com/kino-6/black-stela): `drpg-scenario`
- [mickume/dndtale](https://github.com/mickume/dndtale), [mickume/lorewright-skill](https://github.com/mickume/lorewright-skill)
- [modbender/skill-library-mcp](https://github.com/modbender/skill-library-mcp): `ttrpg-gm`, `agent-rpg`
- [neuralinitiative/claude-dnd-skill](https://github.com/neuralinitiative/claude-dnd-skill)
- [omer-metin/skills-for-antigravity](https://github.com/omer-metin/skills-for-antigravity): `tabletop-rpg-design`
- [SimHacker/moollm](https://github.com/SimHacker/moollm): `adventure`
- [Thedougler/ai-co-dm](https://github.com/Thedougler/ai-co-dm): also `run-guide`, `session-beats`, `copy-writer`
- [VerisimLLC/draw-steel-codex](https://github.com/VerisimLLC/draw-steel-codex)
- [zenobi-us/dotfiles](https://github.com/zenobi-us/dotfiles): `ttrpg-gm`, a copy of [RogerKink6/ttrpg-gm](https://github.com/RogerKink6/ttrpg-gm), an agent-run dark campaign GM
- [majiayu000/claude-skill-registry-data](https://github.com/majiayu000/claude-skill-registry-data): a mirror of many skills, including `solo-rpg`, `playing-ose-solo`, `dice-roller`, `table-tone`

Ignored as noise: [ECNU-ICALK/AutoSkill](https://github.com/ECNU-ICALK/AutoSkill) and its copy in THUIR/MemoryBench (machine-generated role-play prompts), and mirrors such as gabrielmoreira/agent-skills-mirror.

## Method sources

The craft behind nearly all of the skills above:

- Justin Alexander, The Alexandrian: [Don't Prep Plots](https://thealexandrian.net/wordpress/date/2010/05), [the Three Clue Rule](https://thealexandrian.net/?p=7985), [node-based scenario design](https://thealexandrian.net/creations/misc/node-design/node-design2.html)
- Dungeon World, [The GM](https://roll20.net/compendium/dw/The%20GM): agenda, principles ("ask questions and use the answers", "begin and end with the fiction"), GM moves, fronts
- Apocalypse World: fronts and countdown clocks; Blades in the Dark: progress clocks
- Sly Flourish, The Lazy Dungeon Master: strong start, secrets and clues detached from locations
