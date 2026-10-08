---
name: cronaca-di-sessione
description: "Turn a session recap into an in-world chronicle in the style of medieval travel accounts (Il Milione), with a chronicler chosen to fit the milieu the PCs moved in. Use for \"riassunto della sessione\", \"cronaca\", \"resoconto in stile\"."
---

# Cronaca di sessione

Trasforma il resoconto grezzo di una sessione di gioco in una **cronaca in-world**,
raccontata da un personaggio cronista, in stile cronachistico antico (modello: *Il
Milione* di Marco Polo: rubriche di capitolo, digressioni sui costumi e i commerci,
formule di garanzia come «e questo vi dico per certo»).

Il risultato non è un verbale: è un testo che si rilegge prima della sessione
successiva, o si fa leggere al resto del tavolo.

---

## 1. Prima cosa: c'è la fonte o no?

Due modalità molto diverse. Stabilisci subito in quale sei.

### Modalità MASTER: la traccia dell'avventura è accessibile

Cerca e leggi la traccia, in quest'ordine:

1. i doc del progetto Claude collegato (`project_search` / `project_read`);
2. le note Joplin (`search_notes` col titolo dell'atto/missione, poi `get_note`);
3. i file allegati alla conversazione.

Possono esistere **due versioni** della stessa avventura: una vecchia nel progetto e
una aggiornata in Joplin. Se divergono, chiedi quale è stata portata al tavolo.

Poi confronta traccia e riassunto e annota le divergenze tipiche:

- PNG assenti dalla traccia che compaiono nel riassunto (o viceversa);
- ruoli cambiati (un complice che nella traccia era una vittima ricattata);
- fili mai emersi al tavolo (un intero ramo dell'indagine ignorato);
- finali diversi da quello previsto; nomi storpiati.

Fai **una sola tornata di domande** prima di scrivere:

- nomi, specie e ruolo di ciascun PG (il riassunto usa spesso i nomi dei *giocatori*);
- chi sono i PNG che compaiono senza presentazione;
- per ogni divergenza: **scrivo secondo ciò che i PG hanno capito o secondo la
  verità?** (di norma secondo i PG, perché è la loro cronaca);
- cosa deve restare non detto (ganci per gli atti successivi).

Se manca il pezzo che apre o chiude la cronaca, **non inventarlo**: chiedilo.

### Modalità GIOCATORE: c'è solo il riassunto

È il caso normale quando chi scrive siede dall'altra parte dello schermo. Nessuna
traccia, nessun retroscena: **e va benissimo**, perché il cronista per sentito dire
non dovrebbe saperne di più dei personaggi.

Regole in questa modalità:

- **Non cercare la fonte** e non chiederla: parti dal riassunto.
- **Massimo 3–4 domande**, e solo su ciò senza cui il testo non sta in piedi: nomi e
  specie dei PG, il nome di un PNG centrale, com'è finita davvero una scena confusa.
- **Non inventare mai fatti di trama**: moventi, mandanti, retroscena, il vero nome di
  chi tira i fili. Se il buco è evidente, diventa materiale del cronista: una diceria
  attribuita a una fonte («la lavandaia giura che…, ma la lavandaia giura molte
  cose»), oppure una reticenza dichiarata («chi pagasse, io non lo so»).
- **L'incertezza del riassunto è un pregio**: dove il resoconto è vago, il testo
  guadagna, perché quel vago diventa l'ignoranza del narratore.
- In coda, fuori finzione, una riga di **«fili aperti»**: le domande rimaste sospese.
  È quello che il giocatore si porterà alla sessione dopo.

## 2. Scegli il cronista in base all'ambiente

La campagna non ha *un* cronista: ha **un cronista per ambiente**. La voce nasce dal
luogo in cui i PG si sono mossi in questa sessione. Il porto non racconta come una
sala di palazzo, e un frate di strada non sa nulla di dogane.

Usa `AskUserQuestion` con tre opzioni:

1. **il cronista già usato per quell'ambiente** (vedi registro), se l'avventura torna
   negli stessi luoghi;
2. **un cronista nuovo che proponi tu**, tagliato sull'ambiente di questa sessione,
   descritto in una riga (specie/mestiere + perché sa le cose);
3. **un registro diverso** (voce ufficiale, atti di un processo, lettera privata), se
   l'ambiente lo suggerisce.

Nella stessa chiamata chiedi anche:

- **quanto sa il cronista**: solo ciò che i PG videro / sa quanto i PG ma allude /
  onnisciente. In modalità GIOCATORE non proporre l'onnisciente.
- **formato**: capitoletti con rubriche (~1200–1500 parole, default) / racconto unico
  breve (~700) / cronaca ampia con digressioni (~2000+).

Se la sessione attraversa più ambienti, **scegline uno solo**, quello che ospita più
scene, e lascia che il cronista citi gli altri come informatori («questo me l'ha
detto il copista, ché io in dogana non ci metto piede»). Due narratori nello stesso
testo lo spezzano.

### Come si costruisce un buon cronista

- **Testimone laterale, mai protagonista.** Non ha partecipato: ha *raccolto*.
- **Fonti nominate**: il garzone del banco, una lavandaia, uno scrivano ubriaco. Le
  fonti spiegano cosa sa e giustificano i buchi.
- **Un mestiere che gli dia le metafore**: il calafato parla di scafi che imbarcano
  acqua, un contabile di colonne che non tornano. Tutte le immagini vengono da lì.
- **Un difetto sensoriale o un vizio** (un occhio solo, sordo, beve): è la licenza per
  non sapere ciò che non deve essere rivelato.
- **Una posizione sociale che spiega l'accesso**: chi sta al margine di un ambiente ne
  sente tutto: servitori, garzoni, portinai, copisti, ostesse.
- Coerente con specie e genere dell'ambientazione (setting antropomorfo → animale).

## 3. Regole di stile

- **Rubriche di capitolo** alla maniera antica: «Capitolo IV. Della nipote, e del
  garzone che la guardava», «Qui si dice di…», «Come i tre…». Da 6 a 10 capitoli.
- **Proemio** in cui il cronista si presenta e dichiara fonti e limiti.
- **Explicit** finale con formula di chiusura («Qui finisce quel che ho raccolto»).
- **Una digressione sui costumi** (un commercio, una legge, un'usanza del luogo)
  piazzata presto: nel Milione è il marchio di fabbrica, e rende leggibile l'intrigo a
  chi rilegge fra un mese. La digressione deve nascere dall'ambiente del cronista.
- **Seconda persona plurale rivolta a un uditorio**: «Signori», «sappiate che», «voi
  crederete che… non è così».
- **Dubitativo per sentito dire**: «dicono», «giura di aver visto», «se qualche tavola
  non combacia, la colpa è del mare».
- **Chiusure di capitolo che aprono**, non che riassumono.
- **Niente meccaniche**: mai tiri, prove, classi, punti ferita, nomi di giocatori.
- **Allusione, non spiegazione.** Ciò che i PG non sanno si accenna e si lascia cadere:
  «il denaro di chi non c'è più continuava a camminare per conto suo. Io non so cosa
  significhi.» Il cronista ha il diritto di non capire.
- **I fallimenti dei PG si raccontano con affetto**, non con scherno: «e lo dico senza
  malizia, ché è cosa che capita anche ai buoni».
- Cita **testualmente** le battute memorabili della sessione, in blockquote.
- **Regole di scrittura**: prima di scrivere, leggi la skill `scrittura-italiana` e
  applicala a tutto il testo, titoli compresi (in sintesi: niente trattino lungo,
  punteggiatura italiana). Nelle rubriche il numero del capitolo si separa con il
  punto: «Capitolo IV. Della nipote…», «Proemio. Chi vi parla…».

### Formattazione del testo

Tutte le cronache della campagna hanno la stessa impaginazione, così nell'archivio si
leggono come un unico libro:

- **Titolo** con `#`, in maiuscolo: `# LA CRONACA DEL GABBIANO`.
- **Sottotitolo** alla maniera antica con `###`, subito sotto il titolo: `### Nella
  quale…`.
- **Riga di servizio** fuori finzione subito dopo il sottotitolo, in blockquote
  corsivo: `> *Riassunto narrativo di [missione], come effettivamente giocata. PG: Nome
  (specie e ruolo), Nome (specie e ruolo)…*`. Il nome del cronista non va qui: va nel
  campo narratore dell'archivio.
- **Proemio, capitoli ed explicit** tutti con `###`, numero e rubrica separati da un
  punto: `### Capitolo IV. Della nipote…`. Mai `##`: i titoli restano piccoli.
- **Nessuna linea orizzontale** (`---`) fra le sezioni: a separarle bastano i titoli.
- **Battute citate, documenti in-world e glosse del cronista** in blockquote corsivo:
  `> *«…»*`.
- **Formula di chiusura** dell'explicit in corsivo, come ultima riga del testo.

## 4. Consegna

1. Scrivi il file `.md` (titolo della cronaca + sottotitolo alla maniera antica) e
   consegnalo con `SendUserFile`.
2. Sotto il sottotitolo, la riga di servizio fuori finzione descritta in
   «Formattazione del testo»: missione, PG con specie e ruolo. Rende la nota
   autosufficiente fra sei mesi.
3. Salvala dove vive la campagna: nota Joplin nel taccuino giusto (`create_note` con il
   `parent_id` del taccuino della campagna) e/o `project_write` nel progetto collegato.
   Chiedi conferma solo se il taccuino non è ovvio.
4. Offri, in una riga, una **versione da leggere ad alta voce** (2–3 minuti) per aprire
   la sessione successiva.

## 5. Registro dei cronisti: Historia (Nova Marina e dintorni)

Stesso ambiente = stessa voce. Un cronista già usato può richiamare le cronache
precedenti («ve ne parlai l'altra volta») e citare i colleghi degli altri ambienti.

| Ambiente | Cronista | Chi è |
|---|---|---|
| Porto, Boccatonda, bassifondi marinari | **Zenone Malamocco** *(in uso)* | vecchio gabbiano calafato, un occhio solo, siede alla taverna della Zia e racconta per un bicchiere; fonti: il garzone del banco del pesce, una lavandaia del vicolo delle Corde, uno scrivano della dogana |
| Palazzi, casate, quartieri alti | *(da creare)* | archetipo consigliato: un maestro di cerimonie in disgrazia: conosce le anticamere, e chi è caduto parla |
| Gilde, dogane, tribunali, archivi | *(da creare)* | archetipo consigliato: un copista miope che ricopia atti tutto il giorno: sa tutto per iscritto e nulla di persona |
| Strade, entroterra, villaggi | *(da creare)* | archetipo consigliato: un questuante o cantastorie ambulante: sa le cose in ritardo e deformate, e le porta da un paese all'altro |

Quando crei un cronista nuovo, proponilo con nome e specie e, se il master conferma
che lo riuserà, annotalo nelle note della campagna e aggiungi la riga a questa tabella
alla prossima revisione della skill.