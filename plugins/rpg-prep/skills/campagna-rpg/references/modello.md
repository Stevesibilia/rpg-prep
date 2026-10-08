# Modello della nota di campagna

Titolo della nota in Joplin: **«Campagna: <nome>»**.

Segui quest'ordine di sezioni. I titoli di livello 2 (`##`) sono fissi: lo script di controllo li cerca per nome. I commenti fra `<!-- -->` spiegano la regola e non vanno nella nota.

Identificativi, ricercabili con Ctrl+F:

- **F1, F2…** per i fronti, nel titolo `### F1. Nome`;
- **A1, A2…** per gli archi, nel titolo `### A1. Nome`;
- **T1, T2…** per i fili;
- **R1, R2…** per le rivelazioni degli archi.

**Righe vuote.** Ogni campo in grassetto è un paragrafo a sé, con una riga vuota prima e dopo. Senza riga vuota, Joplin lo attacca alla riga precedente.

```markdown
# Campagna: [Nome]

**Sistema:** … · **Tono:** … · **Tavolo:** [giocatori]

**Sessioni:** 12-16 (ogni due settimane, circa sei mesi)

**Arco corrente:** A1. [Nome]

## A colpo d'occhio

**Premessa:** [la situazione in una o due frasi]

**Domanda della campagna:** [una domanda aperta sulle scelte dei PG, senza risposta dentro]

**Temi:** [due o tre temi]

| Fronte | Obiettivo | Volto | Orologio |
| ------ | --------- | ----- | -------- |
| F1. …  | …         | …     | 1/5      |

## Verità del mondo

<!-- Solo l'angolo di mondo dove si gioca. 5-8 voci di una o due righe.
     La prima è la pressione già in corso quando la campagna comincia. -->

- **[Cosa].** …

## Fronti

<!-- 2-4 fronti. L'orologio ha 4-6 passi; l'ultimo è «Se vince». -->

### F1. [Nome]

**Obiettivo:** [comprensibile, anche se mostruoso]

**Volto:** [il PNG che incarna il fronte]; vuole …; dice: «…»

**Perché è difficile da fermare:** …

**Orologio**

- [ ] **F1.1** [cosa accade] _Segni:_ [cosa i PG possono percepire]
- [ ] **F1.2** …
- [ ] **F1.3** …
- [ ] **Se vince.** [lo stato del mondo]

## Fazioni

| Fazione | Vuole | Teme | Risorse | Conflitto interno | Rapporti |
| ------- | ----- | ---- | ------- | ----------------- | -------- |
| …       | …     | …    | …       | …                 | …        |

## PG e agganci

<!-- Uno per PG. Mai cosa farà. -->

### [Nome del PG]

**Giocatore:** …

**Desiderio:** … · **Paura:** … · **Segreto:** …

**Legame:** …

**Domanda aperta:** …

**Fronti che lo toccano:** F1, F2

**Archi che parlano a lui:** A2

## Archi

<!-- 2-5 archi. Ogni arco è una funzione, non una trama. -->

### A1. [Nome]

**Stato:** da giocare / in corso / chiuso

**Sessioni:** 3-5

**Funzione:** [cosa deve consegnare alla campagna]

**Domanda dell'arco:** …

**Fronti in gioco:** F1 (fino a F1.2)

**Rivelazioni**

- **R1.** …

**PG al centro:** [nomi]

**Cambio di tono:** …

**Primo taglio:** [cosa si sacrifica se mancano sessioni]

## Finali possibili

<!-- 2-4 stati del mondo. Le condizioni sono pressioni o fatti, non scelte previste. -->

- **[Nome del finale].** [stato del mondo] _Condizioni:_ … _Da seminare:_ T2 in A1, T4 in A2

## Fili aperti

<!-- Stato: aperto, ripagato, perso. -->

| ID  | Filo | Seminato in | Cosa lo ripaga | Stato  |
| --- | ---- | ----------- | -------------- | ------ |
| T1  | …    | A1          | …              | aperto |

## Temi e motivi

**Temi:** …

**Motivi ricorrenti**

- **[Immagine o simbolo].** Dove ritorna e cosa significa.

## Controllo

<!-- I cinque elementi di una storia di campagna, e i riflettori. -->

- [ ] **Personaggi:** desideri e difetti veri, per PG e antagonisti.
- [ ] **Conflitto:** esterno (fronti, fazioni) e interno (paure e segreti dei PG).
- [ ] **Contesto:** il mondo dà peso alle scelte.
- [ ] **Climax:** i finali sono all'altezza di ciò che la campagna chiede.
- [ ] **Cambiamento:** PG e mondo possono uscirne diversi.
- [ ] **Riflettori:** ogni PG è al centro di almeno un arco.

## Prima della campagna

**Tono:** …

**Linee e veli:** …

**Strumenti di sicurezza:** …

**Aspettative:** [cadenza, durata, stile di gioco]

**Domande per la creazione dei PG**

- …

## Aggiornamenti

- **[data].** Creata. [oppure: sessioni lette, cosa è cambiato]

## Appendice: stile visivo e sonoro

<!-- Non serve al tavolo. Stile comune per midjourney-prompts e le skill di Suno. -->

### Campagna

visual: [English: era, palette, light, recurring textures]

mood: [English: overall sonic identity, instruments, register]

### F1. [Nome]

visual: …

mood: …
```
