# diagramma flowchart: come fare un diagramma UML/mermaid
```mermaid
flowchart TD
    A{{Informazione necessaria?}}
    B1[Fine]
    B{{Informazione atomica?}}
    C1[Attributo]
    C{{Informazione indipendente?}}
    D1{{Ereditarietà?}}
    L[Classe]
    L1[Classe derivata]
    D[Associazione]
    E{{Tipologia di associazione?}}
    subgraph Traduzione Associazioni

        F{{Bidirezionale?}}
        I[Attributo che punta all'altra classe]
        I1[Per ognuna delle due, attributo che punta all'altra classe]
        G{{Bidirezionale?}}
        J[Lista nella classe con cardinalita 1]
        J1[Lista in una classe e attributo semplice nell'altra]
        H{{Attributi della associazione?}}
        K1[Classe associativa: classe con relazione 1-to-many]
        K[Lista in una o entrambe le classi]
    end

    A --> |si| B
    A --> |no| B1
    B --> |no| C
    B --> |si| C1
    C --> |no| D
    C --> |si| D1
    D --> E
    E -- "1-to-1" --> F
    E -- "1-to-many" --> G
    E -- "many-to-many" --> H
    F --> |no| I
    F --> |si| I1
    G --> |no| J
    G --> |si| J1
    H --> |no| K
    H --> |si| K1
    D1 --> |no| L
    D1 --> |si| L1
    
```


# Informatica Appunti 14/02/2025

## Associazioni

**1-n:** una lista nella classe principale e un attributo nell'altra.

Nelle associazioni, dipende dal verbo il senso dell'associazione (contiene, ecc.). Leggendo la cardinalità, posso capire dai due sensi come fare l'associazione.

**Esempio: tradurre VisitaVeterinaria da Animale**

- **1-n:** Un animale può avere più visite veterinarie.
- **n-1:** Una visita veterinaria può avere più animali.
- **n-n:** Un animale può avere più visite veterinarie e una visita veterinaria può avere più animali.

## Informatica Appunti 18/02/2025

### Classi semplici e derivate

- La relazione **N-N** va scomposta. Se si aggiungono informazioni, va fatta una classe in mezzo (classe associativa), altrimenti no.

- Se nella verifica aggiungo metodi in più, va bene.

### Esempio di verifica
- Devo restituire l'elenco dei docenti di una determinata materia.
  -stringa materia
  - lista docenti
- Devo capire la classe dove metterle (**in questo caso Scuola**).
- Devo calcolare l'età media dei docenti.
  - Si fa nella classe **Scuola**.
  - Metodo: `calcola_età_media_docenti() -> float`

### Relazioni tra classi
- **N-N** → Lista in due classi
  - Se c'è una classe in mezzo, vengono messi gli attributi delle due classi.

  - ` Scuola "1" -- "*" docente : lavora`
  - Se l'asterisco (`*`) è in basso → lista sopra, attributo semplice in basso.
  - Se l'asterisco (`*`) è in alto → attributo semplice sopra, lista in basso.
  - **Esempio di relazione:**
    - `Scuola → list<Docente> → Docenti`
    - `Docente → Scuola → Scuola`

### Metodi
- Partire dalla classe più semplice.
- Per verificare se qualcosa è booleano:
  - `attiva() -> None`
  - `disattiva() -> None`
  - `verificaStato() -> bool`



### Alcuni consigli per la verifica:

Inizia identificando le classi principali e le loro relazioni

Per ogni relazione, usa la giusta cardinalità (1-1, 1-n, n-n)

Ricorda di aggiungere gli attributi necessari per le associazioni

Aggiungi i metodi essenziali per la gestione delle relazioni

Usa le frecce appropriate:

--> per associazioni

<|-- per ereditarietà

..> per dipendenze

Le associazioni più comuni da implementare sono:


One-to-Many (1-*): usa una lista nella classe "uno" e un riferimento singolo nella classe "molti"

Many-to-Many (-): usa liste in entrambe le classi o crea una classe intermedia

One-to-One (1-1): usa riferimenti singoli in entrambe le classi

# Preparazione alla Verifica di Informatica

## Appunti

**1-n**: Una lista nella classe principale e un attributo nell'altra.

**Dipende dal verbo il senso dell'associazione (contiene, possiede, ecc.)**.

**Leggendo la cardinalità posso capire dai due sensi come fare l'associazione**:

- **1-n**: Un animale può avere più visite veterinarie.
- **n-1**: Una visita veterinaria può riguardare più animali.
- **n-n**: Un animale può avere più visite veterinarie e una visita veterinaria può riguardare più animali.

Esempio in **Mermaid**:

```mermaid
classDiagram
    Animale "1" -- "*" VisitaVeterinaria : ha
```

---

## Associazioni nelle Classi

Le associazioni tra classi si classificano in diverse tipologie:

### Associazione 1-1

Un utente può avere un solo profilo e ogni profilo appartiene a un solo utente.

- In questo caso, ogni classe contiene un riferimento diretto all'altra classe.

```mermaid
classDiagram
    Utente "1" -- "1" Profilo : possiede
    class Utente {
        +string nome
        +Profilo profilo
    }
    class Profilo {
        +string bio
        +string foto
    }
```

### Associazione 1-N

Un autore può scrivere più libri, ma ogni libro ha un solo autore.

- La classe con cardinalità "1" avrà una lista degli oggetti della classe con cardinalità "N".
- La classe con cardinalità "N" avrà un riferimento singolo all'oggetto della classe con cardinalità "1".

```mermaid
classDiagram
    Autore "1" -- "*" Libro : scrive
    class Autore {
        +string nome
        +List<Libro> libri
    }
    class Libro {
        +string titolo
        +Autore autore
    }
```

### Associazione N-N

Uno studente può essere iscritto a più corsi, e ogni corso può avere più studenti iscritti.

- Entrambe le classi contengono una lista degli oggetti dell'altra classe.

```mermaid
classDiagram
    Studente "*" -- "*" Corso : frequenta
    class Studente {
        +string nome
        +List<Corso> corsi
    }
    class Corso {
        +string titolo
        +List<Studente> studenti
    }
```

### Associazione con Classe Associativa

Un dottore può visitare più pazienti e un paziente può avere più visite. Creiamo una classe **Visita** che raccoglie informazioni aggiuntive come la data della visita.

- La classe intermedia "Visita" rappresenta la relazione e contiene riferimenti alle altre due classi.

```mermaid
classDiagram
    Dottore "1" -- "*" Visita : effettua
    Paziente "1" -- "*" Visita : riceve
    class Dottore {
        +string nome
    }
    class Paziente {
        +string nome
    }
    class Visita {
        +Date data
        +Dottore dottore
        +Paziente paziente
    }
```

### Associazione con Ereditarietà

Una persona può essere uno studente o un docente. Definiamo una classe "Persona" e due classi derivate "Studente" e "Docente".

```mermaid
classDiagram
    class Persona {
        +string nome
    }
    class Studente {
        +string corso
    }
    class Docente {
        +string materia
    }
    Persona <|-- Studente
    Persona <|-- Docente
```

---

## Verifica precendente
# Diagramma UML del Sistema Gestione Zoo

```mermaid
classDiagram
    note "Nel diagramma mancano gli attributi
    che derivano dalla conversione
    delle associazioni in codice."

    Animale <|-- Mammifero
    Animale <|-- Rettile
    Habitat "1" --> "*" Animale : contiene
    VisitaVeterinaria "*" --> "1" Veterinario : effettuata da
    VisitaVeterinaria "*" --> "1" Animale : effettuata su
    SistemaGestioneZoo "1" ..> "*" Animale : gestisce
    SistemaGestioneZoo "1" ..> "*" Habitat : gestisce
    SistemaGestioneZoo "1" ..> "*" Veterinario : gestisce
    SistemaGestioneZoo "1" ..> "*" VisitaVeterinaria : gestisce

    class Animale {
        +str codiceIdentificativo
        +str nome
        +int eta
        +float peso
        +aggiungi_visita(VisitaVeterinaria visita) None
    }

    class Mammifero {
        +str tipoPelliccia
        +float temperaturaCorpo
        +int periodoGestazione
    }

    class Rettile {
        +bool velenoso
    }

    class Habitat {
        +str codiceArea
        +str nome
        +float dimensione
        +aggiungi_animale(Animale animale) None
        +rimuovi_animale(Animale animale) None
        +get_animali() list[Animale]
        +get_eta_media() float
    }

    class Veterinario {
        +str matricola
        +str nome
        +str cognome
        +str specializzazione
        +int anniEsperienza
        +effettua_visita(Animale animale, str diagnosi, str trattamento) VisitaVeterinaria
    }

    class VisitaVeterinaria {
        +datetime data
        +str diagnosi
        +str trattamentoProposto
    }

    class SistemaGestioneZoo {
        +aggiungi_animale(Animale animale) None
        +rimuovi_animale(Animale animale) None
        +assegna_habitat(Animale animale, Habitat habitat) bool
        +registra_visita(VisitaVeterinaria visita) None
        +get_animali_habitat(Habitat habitat) list[Animale]
        +get_storico_visite(Animale animale) list[VisitaVeterinaria]
        +get_habitat_compatibili(Animale animale) list[Habitat]
        +calcola_eta_media_per_habitat() dict[str, float]
    }
```

# esercizio in preparazione alla verifica

# testo esercizio
### Serra automatizzata

Un'azienda agricola moderna vuole automatizzare la gestione della propria serra. Ogni serra viene utilizzata per diverse coltivazioni e deve essere monitorata costantemente. Per garantire la crescita ottimale delle _piante_, vengono utilizzati vari dispositivi e sensori che controllano le condizioni ambientali.

Le serre sono divise in sezioni separate per ospitare colture diverse che richiedono condizioni specifiche. _Il sistema deve tenere traccia di cosa viene coltivato, quando è stato piantato e quando si prevede il raccolto. Per ogni coltivazione, si deve poter calcolare lo stadio di crescita e stimare la quantità prevista al raccolto._

I vari dispositivi presenti nella serra (come irrigatori, ventilatori, luci) possono essere attivati o disattivati. I sensori forniscono continuamente letture delle condizioni ambientali attraverso un metodo di rilevazione.

_Il sistema deve essere in grado di intervenire automaticamente su una determinata sezione quando necessario, monitorando i parametri ambientali di tutta la serra (attraverso il metodo monitoraParametri che restituisce un dizionario con i valori rilevati) e attivando l'irrigazione (tramite il metodo attivaIrrigazione che attiva tutti i dispositivi di tipo irrigatore presenti nella sezione specificata)_.

# esercizio svolto

```mermaid
classDiagram
    class Serra {
        +str nome
        +float superficie
        +list[Sensore] sensori
        +list[Sezione] sezioni
        +list[Dispositivo] dispositivi
        +list[Coltivazione] coltivazioni
        +monitoraParametri() dict
        +attivaIrrigazione(str nome_sezione) bool
    }

    class Sensore {
        +str tipo
        +str posizione
        +float valore
        +str unitaMisura
        +bool attivo
        +Sezione sezione
        +Serra serra
    }

    class Sezione {
        +str nome
        +float superficie
        +Coltivazione coltivazione
        +list[Sensore] sensori
        +list[Dispositivo] dispositivi
        +Serra serra
    }

    class Dispositivo {
        +str nome
        +str tipo
        +str stato
        +Serra serra
        +Sezione sezione
        +attiva() None
        +disattiva() None
        +verificaStato() bool
    }

    class Coltivazione {
        +str specie
        +datetime dataInizio
        +datetime dataRaccoltoPrevista
        +float quantitaPrevista
        +str stato
        +Serra serra
        +Sezione sezione
    }


    Serra "1" .. "*" Sensore : monitora con
    Serra "1" .. "*" Sezione : suddivisa in
    Serra "1" .. "*" Dispositivo : controlla
    Serra "1" .. "*" Coltivazione : gestisce
    Sezione "1" -- "*" Sensore : contiene
    Sezione "1" -- "*" Dispositivo : utilizza
    Sezione "1" -- "1" Coltivazione : ospita
```

Spiegazione Passo-Passo

Identificazione delle Classi:

Serra: Contiene più sezioni e ha metodi per monitorare i parametri e attivare l'irrigazione.

Sezione: Contiene informazioni sulle colture e ha metodi per calcolare la crescita e stimare il raccolto.

Dispositivo: Può essere acceso o spento.

Sensore: Misura parametri ambientali e restituisce il valore rilevato.

Definizione delle Relazioni:

Una serra contiene più sezioni.

Ogni sezione ha più dispositivi e sensori.

Metodi Importanti:

monitoraParametri(): Restituisce i valori ambientali rilevati dai sensori.

attivaIrrigazione(id_sezione): Attiva tutti gli irrigatori in una specifica sezione.

calcolaStadioCrescita(): Determina lo stato attuale della coltivazione.

stimaRaccolto(): Fornisce una stima della quantità di raccolto attesa.

attiva() e disattiva(): Controllano i dispositivi.

rileva(): Restituisce il valore misurato da un sensore.

Con questo esercizio hai un esempio chiaro di modellazione di un sistema con classi e relazioni, utile per la verifica!



# Esercizio Svolto: Sistema di Gestione di una Biblioteca

#### Testo dell'esercizio

Una biblioteca moderna vuole automatizzare la gestione del proprio catalogo e del prestito dei libri. Ogni biblioteca possiede un ampio archivio di libri disponibili per il prestito.

I libri possono essere presi in prestito dagli utenti, i quali devono registrarsi nel sistema. Ogni utente può prendere in prestito più libri contemporaneamente, ma ogni libro può essere prestato a un solo utente alla volta.

Il sistema deve tenere traccia di chi ha preso in prestito un determinato libro e della data di scadenza del prestito. Deve inoltre permettere di verificare la disponibilità di un libro e segnalare i ritardi nei prestiti.

### Soluzione con Diagramma UML in **Mermaid**

```mermaid
classDiagram
    class Biblioteca {
        +List<Libro> catalogo
        +List<Utente> utenti
        +verificaDisponibilita(titolo: string): bool
        +gestisciPrestiti(): void
    }
    class Libro {
        +string titolo
        +string autore
        +bool disponibile
        +assegnaA(Utente): void
        +restituisci(): void
    }
    class Utente {
        +string nome
        +List<Libro> prestiti
        +prendiInPrestito(Libro): bool
        +restituisciLibro(Libro): void
    }
    Biblioteca "1" -- "*" Libro : contiene
    Biblioteca "1" -- "*" Utente : registra
    Utente "1" -- "*" Libro : prende in prestito
```

#### Spiegazione Passo-Passo

1. **Identificazione delle Classi**:
   - **Biblioteca**: Contiene una lista di libri e utenti registrati, con metodi per verificare la disponibilità e gestire i prestiti.
   - **Libro**: Contiene titolo, autore e stato di disponibilità, con metodi per assegnare il libro a un utente o restituirlo.
   - **Utente**: Ha un elenco di libri in prestito e metodi per prendere in prestito o restituire un libro.

2. **Definizione delle Relazioni**:
   - Una **biblioteca** contiene più **libri** e più **utenti**.
   - Un **utente** può prendere in prestito più **libri**, ma ogni **libro** può essere assegnato a un solo **utente** alla volta.

3. **Metodi Importanti**:
   - `verificaDisponibilita(titolo)`: Controlla se un libro è disponibile nel catalogo.
   - `gestisciPrestiti()`: Verifica lo stato dei prestiti e segnala ritardi.
   - `assegnaA(utente)`: Assegna un libro a un utente se disponibile.
   - `restituisci()`: Rende nuovamente disponibile un libro.
   - `prendiInPrestito(libro)`: Permette a un utente di prendere in prestito un libro disponibile.
   - `restituisciLibro(libro)`: Permette a un utente di restituire un libro in prestito.


# Metodi nelle Classi

I metodi rappresentano le operazioni che una classe può eseguire. Possono essere semplici o più complessi.

### Metodi di Accesso
- **getNome()**: Restituisce il nome di un oggetto.

```mermaid
classDiagram
    class Persona {
        +string nome
        +getNome(): string
    }
```

### Metodi di Calcolo
- **calcolaMediaVoti()**: Restituisce la media dei voti di uno studente.

```mermaid
classDiagram
    class Studente {
        +List<int> voti
        +calcolaMediaVoti(): float
    }
```

### Metodi Booleani
- **haSuperatoEsame()**: Restituisce `true` se il voto è sopra la soglia di sufficienza.

```mermaid
classDiagram
    class Studente {
        +int voto
        +haSuperatoEsame(): bool
    }
```

### Metodi con Parametri
- **aggiungiLibro(Libro libro)**: Aggiunge un libro alla lista di un autore.

```mermaid
classDiagram
    class Autore {
        +List<Libro> libri
        +aggiungiLibro(Libro libro): void
    }
```

### Metodi di Gestione
- **attivaDispositivo()** e **disattivaDispositivo()**: Cambiano lo stato di un dispositivo.

```mermaid
classDiagram
    class Dispositivo {
        +bool stato
        +attivaDispositivo(): void
        +disattivaDispositivo(): void
    }
```

### Metodi Complessi
- **prenotaVisita(Paziente paziente, Date data)**: Permette a un dottore di prenotare una visita per un paziente.

```mermaid
classDiagram
    class Dottore {
        +string nome
        +prenotaVisita(Paziente paziente, Date data): void
    }
```

- **verificaDisponibilitaLibro(String titolo)**: Controlla se un libro è disponibile nella biblioteca.

```mermaid
classDiagram
    class Biblioteca {
        +List<Libro> catalogo
        +verificaDisponibilitaLibro(String titolo): bool
    }
```

- **generaReportPresenze()**: Un corso può generare un report degli studenti iscritti.

```mermaid
classDiagram
    class Corso {
        +List<Studente> studenti
        +generaReportPresenze(): string
    }
```

Con questi esempi hai una guida completa su come interpretare e progettare i metodi nelle classi UML!

