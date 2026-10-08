# Formato del rapporto

Il rapporto va nella conversazione, in Markdown. Breve dove può, preciso dove deve.

## Struttura

```markdown
## Revisione: [titolo]

**Cosa ho letto:** [documento, e il contesto usato: nota della campagna, schede]

**Verdetto:** [una frase: regge, regge con riserve, non regge, e perché]

### Problemi

**P1. [Il problema in poche parole]** · bloccante · S5, Schede: Sabaoth

- **Cosa non va:** [una o due frasi, con la citazione se serve]
- **Al tavolo:** [cosa succede concretamente, e con quale tavolo simulato emerge]
- **Radice:** [la causa, dopo almeno tre «perché?»]
- **Correzione proposta:** [alla radice; se ci sono strade diverse, due al massimo]

**P2. …** · serio · …

### Da chiarire

- [Domande su ciò che il documento non dice e che cambia il giudizio]

### Controlli superati

- [Attacchi e tavoli che non hanno trovato problemi, in una riga ciascuno]
```

## Gravità

| Gravità       | Quando                                                                                                              |
| ------------- | ------------------------------------------------------------------------------------------------------------------- |
| **bloccante** | La storia può fermarsi al tavolo: climax impossibile, rivelazione irraggiungibile, scena chiave senza accesso       |
| **serio**     | È probabile che il tavolo si confonda, si annoi o venga costretto; una scelta sensata dei giocatori non ha risposta |
| **minore**    | Imprecisione, incoerenza di dettaglio, errore di struttura del modello                                              |

Ordina per gravità, poi per posizione nel documento. Numera P1, P2… per poterli citare nel brainstorming.

## Esempio

Su «L'Ancora di Sabaoth», l'esempio di `enhanced-avventure-rpg`. Illustra la forma, non è una revisione completa.

```markdown
## Revisione: L'Ancora di Sabaoth

**Cosa ho letto:** il documento dell'avventura; nessuna nota di campagna (one-shot).

**Verdetto:** regge nella struttura e negli indizi; il climax ha due buchi di regole che i giocatori troveranno.

### Problemi

**P1. «L'Ancora distrutta» non ha una regola** · serio · S5, Regole della situazione

- **Cosa non va:** il documento elenca l'esito «L'Ancora distrutta», ma non dice come si distrugge un ferro antico di bronzo, né cosa costa.
- **Al tavolo:** il tavolo laterale ci prova subito, con un martello o con la dinamite dei Quieti; il master improvvisa la regola più importante della serata.
- **Radice:** le regole della situazione descrivono gli esiti, non le condizioni per ottenerli.
- **Correzione proposta:** dare all'Ancora una sola via di distruzione, legata alla storia (la fonderia del porto, o il fuoco del Duomo), con un prezzo chiaro.

**P2. Donato arriva a Peloro prima o dopo i PG?** · minore · Orologio 2, S5

- **Cosa non va:** Donato muove i Quieti alla seconda scossa; S5 dice che arrivano «poco dopo i PG», ma il tavolo impaziente può arrivare a Peloro prima della seconda scossa.
- **Al tavolo:** il master deve decidere al volo se Donato c'è.
- **Radice:** la posizione di Donato dipende dall'orologio, quella dei PG no.
- **Correzione proposta:** legare l'arrivo di Donato alla scossa, non ai PG: se la seconda scossa non è ancora arrivata, Donato non c'è.

### Da chiarire

- «La Maestà» ferma chi non si è Risvegliato: se a S5 nessun PG si è Risvegliato, un solo «Fermi» può bloccarli tutti? Dipende da come Kulthos risolve il talento. Se li blocca, è un problema bloccante; la variante della Guida sui dadi Dissonanza lo attenua, ma non lo esclude.

### Controlli superati

- Indizi: ogni rivelazione ha almeno tre indizi in almeno due scene.
- Flusso: ogni scena è raggiungibile; i segreti dei PG portano a S2, S3 e S4.
- Regola d'oro: nessuna azione dei PG prescritta; le reazioni sono tutte condizionali.
- Tavolo disinteressato: l'orologio e «Se nessuno interviene» lo raggiungono.
```
