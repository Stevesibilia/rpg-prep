---
name: adventure-writing
description: Write, structure, and refine tabletop RPG adventures and one-shots through a guided prep workflow. Use this skill whenever the user wants to prepare a session, write an adventure, design a scenario, plan a one-shot, develop a plot hook, outline scenes, create NPCs for an upcoming session, or brainstorm "what happens next" in their campaign. Also trigger on Italian requests like "prepara l'avventura", "scrivi la sessione", "nuova avventura", or when the user mentions session prep for systems like D&D, Call of Cthulhu, Symbaroum, 7th Sea, Broken Compass, or Vileborn. Even a vague "I need something for Saturday's game" should trigger this skill.
---

# Adventure Writing

Help a game master turn an idea (or nothing at all) into a playable adventure document. The output is a structured markdown file the GM reads at the table, with per-scene hooks that downstream skills (`midjourney-prompts`, `suno-prompts`) can consume to generate art and music.

## Language rule

The adventure document is written in **Italian** — it is read aloud at an Italian table. Structural keys in the template (`visual:`, `mood:`, scene headers) stay in English so companion skills can parse them reliably. If the user writes in English and asks for an English document, follow their lead; Italian is the default, not a cage.

## Workflow

### 1. Gather context before inventing anything

Ask only what you can't infer. The essentials:

- **System and genre** — a Cthulhu investigation and a 7th Sea swashbuckler have opposite pacing DNA. The system implies tone, lethality, and scene types.
- **The party** — who are the PCs? Adventures land when scenes hook specific characters. A secret is more fun when it belongs to someone at the table.
- **Where the campaign stands** — what happened last session, what threads are open. Ask the user to paste a summary if one exists; don't demand it.
- **Practical constraints** — one-shot or campaign episode? Expected session length? Any set pieces the GM already dreams of running?

If the user gives you nothing but a vibe, propose three distinct premises (one sentence each, different in structure not just in skin) and let them pick before investing in detail.

### 2. Build the skeleton before the flesh

Work top-down. A good adventure skeleton, in order of importance:

1. **The dramatic question** — one sentence the session answers. "Will the PCs discover who's poisoning the harbor before the fleet sails?" If you can't state it, the adventure will wander.
2. **The strong start** — open in motion: an event already underway that demands reaction. Never open with "you're in a tavern, what do you do?". The first five minutes set the session's energy.
3. **Secrets and clues** — write ~10 discoverable facts as one-liners, each detached from any fixed location. The GM reveals them through whatever scene the players actually visit. This is what makes an adventure robust to player chaos: prep truths, not paths.
4. **Scenes** — 4–6 for a 3–4 hour session. Each scene needs a purpose (what it changes) and at least two exits. More scenes than that and you're writing a railroad; fewer and you're improvising anyway.
5. **NPCs** — for each: one want, one fear, one table-visible mannerism. Skip biography; the GM needs playable handles, not lore.
6. **The flexible climax** — know the collision the adventure builds toward, but let where and how stay soft until play determines it.

### 3. Write scenes with sensory and tonal handles

Every scene gets `visual` and `mood` fields (in English). These aren't decoration: `midjourney-prompts` turns `visual` into scene art, `suno-prompts` turns `mood` into a music cue. Write them as raw material — concrete nouns, light, weather, era, palette for `visual`; emotional register, energy, instrumentation hints for `mood`.

### 4. Pressure-test before delivering

Before handing over the document, check:

- Can every clue be found in at least two places? (If a clue lives in one scene only, the adventure breaks when players skip it.)
- Does each PC have at least one scene that speaks to them specifically?
- What happens if the players ignore the hook? There should be a consequence that comes to them.
- Is there at least one scene of each type the system loves? (Cthulhu: dread + research. 7th Sea: derring-do + repartee. Symbaroum: wilderness menace + corruption temptation.)

## Adventure document template

ALWAYS use this exact structure (content in Italian, keys in English):

```markdown
# [Titolo avventura]

**Campagna:** [nome] · **Sistema:** [sistema] · **Durata prevista:** [ore]

## Domanda drammatica
[Una frase.]

## Inizio forte
[La scena d'apertura, in medias res. 3-5 frasi da leggere o parafrasare.]

## Segreti e indizi
- [ ] [fatto scopribile 1]
- [ ] [fatto scopribile 2]
- [ ] ... (~10 in totale, spuntabili durante la sessione)

## Scene

### Scena 1 — [Nome evocativo]
**Scopo:** [cosa cambia nella storia]
**Luogo:** [dove]
visual: [English: concrete visual description — subjects, light, era, palette]
mood: [English: emotional register + musical energy]

[Descrizione della scena: cosa sta succedendo, cosa possono fare i PG.]

**Uscite:** [almeno due modi in cui la scena può risolversi/collegarsi]

### Scena 2 — ...

## PNG

### [Nome] — [ruolo]
**Vuole:** [una cosa] · **Teme:** [una cosa] · **Segno distintivo:** [manierismo visibile]
[Una riga di contesto se serve.]

## Climax flessibile
[La collisione finale: chi converge, cosa è in gioco, 2-3 modi in cui può andare.]

## Se i giocatori ignorano l'esca
[La conseguenza che li raggiunge comunque.]
```

## Example scene (abbreviated)

```markdown
### Scena 3 — Il faro spento
**Scopo:** i PG scoprono che il guardiano è scomparso da tre giorni
**Luogo:** faro di Punta Corvo, notte, tempesta in arrivo
visual: abandoned lighthouse on jagged cliffs at night, storm clouds, cold moonlight through broken lantern room, 1920s Italian coast, muted blues and slate grey
mood: creeping dread, sparse and tense, low drones, distant thunder, something is wrong here

La porta del faro è aperta e sbatte al vento. Dentro: cena per una persona,
intatta, coperta di muffa. Il registro del guardiano si interrompe a metà frase.

**Uscite:** salire alla lanterna (Scena 4) · seguire le impronte verso la
scogliera (Scena 5) · tornare al villaggio con le prove (Scena 6)
```

## Working style

Iterate conversationally. Draft the skeleton, show it, refine what the user pushes on. Don't dump a finished 3000-word adventure on someone who wanted to brainstorm — but when they say "write it", write all of it. Save the document where the user asks; if they don't say, propose `adventures/<campaign>/<slug>.md` relative to the current directory.
