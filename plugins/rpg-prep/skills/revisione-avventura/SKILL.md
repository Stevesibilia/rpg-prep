---
name: revisione-avventura
description: "Revisione avversaria di un'avventura o di una campagna di GDR: cerca buchi di logica, cause mancanti, PNG che sanno ciò che non possono sapere, indizi che non portano da nessuna parte, scene irraggiungibili, piani dell'antagonista che non reggono, vicoli ciechi, tradimenti della regola d'oro, ritmo che cede; simula tavoli diversi per vedere dove la storia si rompe; poi discute i problemi con il master in un brainstorming. Non riscrive il documento. Usala quando il master chiede di controllare, criticare, rivedere o mettere alla prova un'avventura, una one-shot o una campagna, di trovare buchi di trama, di capire se la logica regge o se la storia scorre. Frasi tipiche: «rivedi l'avventura», «trova i buchi», «regge?», «fai l'avvocato del diavolo», «mettila alla prova», «brainstorming sull'avventura», «review my adventure». Funziona sui documenti di enhanced-avventure-rpg e campagna-rpg e su qualsiasi testo d'avventura."
---

# Revisione avversaria di avventure e campagne

Attacca un'avventura o una campagna per trovare ciò che si romperà al tavolo, prima che si rompa. Il compito è **trovare e spiegare**, non riscrivere: il documento resta del master. Il rapporto va **nella conversazione**, poi si apre un brainstorming sui problemi trovati.

Scrivi in **italiano** e applica la skill `scrittura-italiana`: niente trattino lungo né medio, virgolette basse, punteggiatura italiana.

## Atteggiamento

- **Avversario, non ostile.** Cerchi i punti deboli come farebbe il tavolo più difficile. Non elogi, non addolcisci; non inventi problemi per sembrare utile.
- **Prove, non impressioni.** Ogni problema indica dove sta (S3, I7, R2, F1.2, A2, o la frase citata) e cosa succede al tavolo.
- **Alla radice.** Un sintomo («il colpo di scena non funziona») si segue all'indietro almeno tre volte con «perché?» finché si trova la causa («l'indizio che lo preparava sta solo in una scena facoltativa»). La correzione proposta agisce lì, non sul sintomo.
- **Il master decide.** Proponi correzioni; non le applichi. Se il master chiede di applicarle, usa il formato della skill che ha prodotto il documento (`enhanced-avventure-rpg` o `campagna-rpg`).
- **Regola d'oro.** Anche le correzioni preparano verità e pressioni, mai azioni dei PG.

## Procedura

### 1. Leggi e capisci cosa hai davanti

- **Il documento:** un file, una nota Joplin, un testo incollato. Se è un'avventura di `enhanced-avventure-rpg` o una nota «Campagna: <nome>» di `campagna-rpg`, usa i loro identificativi (S, R, I, F, A, T).
- **Il contesto:** per un'avventura di campagna, leggi anche la nota della campagna; se hai GDR Archive, le schede dei PG. Un problema può nascere dal rapporto fra i due.
- **Il tipo:** avventura (una sessione o una one-shot) o campagna (fronti, archi, finali). Gli attacchi cambiano.
- **Gli strumenti strutturali:** se il documento viene da `enhanced-avventure-rpg` o `campagna-rpg` e puoi eseguire codice, esegui prima il loro `scripts/controlla.py`. Gli errori di struttura vanno nel rapporto come problemi minori; la revisione si occupa del resto.

### 2. Costruisci la mappa

Prima di attaccare, ricostruisci per iscritto, per te:

- **la cronologia:** cosa succede, in che ordine, quanto tempo passa, quanto distano i luoghi;
- **chi sa cosa, e da quando:** PNG, antagonisti, PG;
- **il grafo degli indizi:** ogni rivelazione, gli indizi che ci portano, le scene dove stanno, le abilità che servono;
- **il grafo delle scene:** per ogni scena, come i PG vengono a sapere che esiste e come ci arrivano;
- **il piano dell'antagonista:** obiettivo, passi, risorse, cosa fa se nessuno interviene.

La mappa rivela da sola metà dei problemi: una freccia che manca è un buco.

### 3. Attacca

Leggi gli attacchi per il tipo di documento:

- avventura: [references/attacchi-avventura.md](references/attacchi-avventura.md);
- campagna: [references/attacchi-campagna.md](references/attacchi-campagna.md).

Poi esegui i **tavoli simulati** di [references/tavoli.md](references/tavoli.md): giochi il documento con quattro tavoli diversi e annoti dove smette di funzionare.

Se puoi lanciare sotto-agenti, affida ogni attacco e ogni tavolo simulato a un agente separato, con il documento, la mappa e la sua lista: occhi indipendenti trovano cose diverse. Poi raccogli e verifica tu.

### 4. Verifica ogni problema

Prima di riportarlo, prova a **smontare** ogni problema trovato:

- cerca nel documento la frase che lo risolve già (un indizio in un'altra scena, una regola nelle schede, una reazione nella tabella);
- chiediti se un master ragionevole lo risolverebbe al volo senza danni;
- se è risolto, scartalo; se dipende da qualcosa che il documento non dice, tienilo come **da chiarire** e trasformalo in una domanda per il master.

Riporta solo ciò che sopravvive. Meglio cinque problemi veri che venti dubbi.

### 5. Rapporto, nella conversazione

Segui il formato di [references/rapporto.md](references/rapporto.md): verdetto in una frase, problemi dal più grave, controlli superati, domande aperte. Niente file, niente note: il rapporto sta nella chat.

### 6. Brainstorming

Dopo il rapporto, apri il brainstorming. **Una domanda alla volta**, partendo dal problema più grave:

- chiedi al master cosa intendeva, quando il documento non lo dice;
- proponi due o tre alternative diverse nella struttura, non varianti della stessa idea, con il loro costo;
- usa i «e se…?» per mettere alla prova le soluzioni del master: ogni correzione si attacca come il resto;
- quando una questione è chiusa, riassumi la decisione in una riga e passa alla successiva.

Alla fine, riepiloga le decisioni prese. Se il master lo chiede, applicale al documento con la skill che lo ha prodotto.
