# Installing the rpg-prep skills

Eight skills: `enhanced-avventure-rpg`, `avventure-gdr`, `adventure-writing`, `cronaca-di-sessione`, `scrittura-italiana`, `midjourney-prompts`, `suno-prompts`, `suno-prompt-creator`.

**Short answer on visibility: no, a public repo is not required.** Claude Code installs from a local directory or from a private GitHub repo (it uses your own git credentials to clone). Claude.ai web and the Claude desktop/mobile apps don't use repos at all: you upload zip files manually. A public repo is only useful if you want to share the skills with other people.

---

## 1. Claude Code (CLI / IDE)

### Option A — Plugin marketplace from the local directory (recommended for you)

The repo is already a valid plugin marketplace. From any Claude Code session:

```
/plugin marketplace add /home/steve/Homelab/fun/rpg-prep
/plugin install rpg-prep@rpg-prep
```

All eight skills become available in every project. Update flow after editing a skill:

```
/plugin marketplace update rpg-prep
```

### Option B — Plugin marketplace from GitHub (private repo works)

Push the repo to GitHub (private is fine, as long as `gh auth status` or your git credentials can clone it):

```
/plugin marketplace add stefanosibilia/rpg-prep
/plugin install rpg-prep@rpg-prep
```

Same commands on any machine where you're authenticated. This is the way to sync skills across multiple computers.

### Option C — Plain personal skills (no plugin machinery)

Copy the skill folders into your personal skills directory:

```bash
cp -r plugins/rpg-prep/skills/* ~/.claude/skills/
```

Simplest, but updates are manual copies and there's no versioning/uninstall.

### Using the skills

Skills trigger automatically when the request matches their description. Typical session:

```
> Prepara l'avventura di sabato per Symbaroum: il villaggio ai margini
  del Davokar è stato abbandonato in una notte
  → enhanced-avventure-rpg produces the full Italian adventure doc

> Dammi le immagini per tutte le scene
  → midjourney-prompts reads the visual: fields, emits MJ prompts

> E le musiche
  → suno-prompts reads the mood: fields, emits Suno prompts

```

You can also invoke explicitly: "use the adventure-writing skill to...".

---

## 2. Claude.ai (web)

Marketplaces don't exist on claude.ai; skills are uploaded as zip files.

Requirements: a paid plan (Pro/Max/Team/Enterprise) with code execution / skills capability enabled.

1. Zips are pre-built in `dist/`:
   - `dist/enhanced-avventure-rpg.zip`
   - `dist/avventure-gdr.zip`
   - `dist/adventure-writing.zip`
   - `dist/cronaca-di-sessione.zip`
   - `dist/scrittura-italiana.zip`
   - `dist/suno-prompt-creator.zip`
   - `dist/midjourney-prompts.zip`
   - `dist/suno-prompts.zip`
2. On claude.ai: **Settings → Capabilities → Skills → Upload skill** and upload each zip (one skill per zip; each zip contains the skill folder with its `SKILL.md` and `references/`).
3. Toggle the uploaded skills on.
4. In any chat, phrase requests as at the table ("preparami l'avventura...", "musiche per la sessione...") — Claude consults the matching skill automatically.

After editing a skill locally, rebuild its zip and re-upload:

```bash
cd plugins/rpg-prep/skills
zip -qr ../../../dist/adventure-writing.zip adventure-writing
```

Note: on claude.ai the skills can't read your local files. Paste campaign context (or attach the adventure doc) into the conversation; the generator skills work from what's in the chat.

---

## 3. Claude desktop and mobile apps

Skills uploaded to claude.ai are account-level: the desktop app and mobile app use the same backend, so the eight skills are available there automatically once uploaded via the web UI (step 2 above). There is no separate installation.

The desktop app additionally bundles Claude Code — inside a Claude Code pane, the plugin marketplace from section 1 applies instead.

---

## Keeping everything in sync

Single source of truth: this repo. Suggested flow when you improve a skill:

1. Edit `plugins/rpg-prep/skills/<name>/SKILL.md`
2. Claude Code picks it up via `/plugin marketplace update rpg-prep` (local) or `git push` + update (GitHub)
3. Rebuild the zip and re-upload to claude.ai for web/app use

The zip rebuild for all four:

```bash
cd plugins/rpg-prep/skills
for s in */; do zip -qr "../../../dist/${s%/}.zip" "${s%/}"; done
```
