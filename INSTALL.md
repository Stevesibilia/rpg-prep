# Installing the rpg-prep skills

Ten skills: `campagna-rpg`, `enhanced-avventure-rpg`, `revisione-avventura`, `avventure-gdr`, `adventure-writing`, `cronaca-di-sessione`, `scrittura-italiana`, `midjourney-prompts`, `suno-prompts`, `suno-prompt-creator`.

The repository is public at <https://gitlab.siberio.eu/oss/rpg-prep> and is a Claude plugin marketplace: `.claude-plugin/marketplace.json` lists one plugin, `rpg-prep`, which bundles all ten skills. A plugin installed on your Claude account is available in chat, in Cowork and in Claude Code.

## 1. Claude.ai, desktop and mobile apps

1. Open **Customize** in the sidebar, then **Plugins**.
2. Select **Add marketplace** and enter `https://gitlab.siberio.eu/oss/rpg-prep`.
3. Install the `rpg-prep` plugin.
4. On the marketplace, turn on **Sync automatically**, or select **Check for updates** after each change.

The [plugin guide](https://claude.com/docs/cowork/guide/plugins.md) lists GitHub and public GitLab and Bitbucket repositories as supported sources. Whether that includes a self-hosted GitLab instance is not documented; if the marketplace cannot be added, use the zip fallback in section 3.

If you previously uploaded these skills as zips, remove those copies, or every skill will exist twice.

## 2. Claude Code

```
/plugin marketplace add https://gitlab.siberio.eu/oss/rpg-prep.git
/plugin install rpg-prep@rpg-prep
```

Update after a change:

```
/plugin marketplace update rpg-prep
```

From a local clone instead, for editing:

```
/plugin marketplace add /path/to/rpg-prep
```

## 3. Fallback: zip upload on claude.ai

Every tag builds one zip per skill and attaches them to the [release](https://gitlab.siberio.eu/oss/rpg-prep/-/releases). On claude.ai: **Settings → Capabilities → Skills → Upload skill**, one zip per skill. Re-upload after each release.

To build the zips locally:

```bash
cd plugins/rpg-prep/skills
for s in */; do zip -qr "../../../dist/${s%/}.zip" "${s%/}"; done
```

## Using the skills

Skills trigger when the request matches their description. A typical flow:

```
> Progetta la campagna: Venezia 1923, le isole della laguna si svuotano
  → campagna-rpg writes the Joplin note «Campagna: La Laguna Muta»

> Prepara l'avventura di sabato per Symbaroum: il villaggio ai margini
  del Davokar è stato abbandonato in una notte
  → enhanced-avventure-rpg produces the full Italian adventure doc

> Rivedi l'avventura: regge?
  → revisione-avventura reports the problems in the chat, then brainstorms fixes

> Dammi le immagini per tutte le scene
  → midjourney-prompts reads the visual: fields, emits MJ prompts

> E le musiche
  → suno-prompts reads the mood: fields, emits Suno prompts
```

You can also name a skill explicitly: «usa revisione-avventura su questa avventura».

## Keeping everything in sync

This repository is the single source of truth.

1. Edit `plugins/rpg-prep/skills/<name>/`.
2. Push to `main`. A marketplace with sync turned on picks the change up; in Claude Code, run `/plugin marketplace update rpg-prep`.
3. Tag a release only if you still use the zip fallback.
