# Guida allo Sviluppo - Portfolio Samuel Gentile

Questa guida ti aiuta a comprendere e modificare il tuo portfolio personale. È scritta per sviluppatori principianti/intermedi.

---

## 📁 Struttura del Progetto

```
portfolio/
├── index.html              → Homepage principale
├── about.html              → Pagina "Chi sono"
├── services.html           → Pagina Servizi
├── projects.html           → Pagina Tutti i Progetti
├── contact.html            → Pagina Contatti
├── 404.html                → Pagina errore 404
├── robots.txt              → Istruzioni per motori di ricerca
├── sitemap.xml             → Mappa del sito per SEO
├── README.md               → Documentazione generale
├── README_DEV.md           → Questa guida (per sviluppatori)
│
├── css/                    → Fogli di stile
│   ├── variables.css       → Colori, font, spaziature (design system)
│   ├── style.css           → Stili base e componenti
│   ├── animations.css      → Animazioni e keyframes
│   └── responsive.css      → Media query per mobile/tablet
│
├── js/                     → File JavaScript
│   ├── main.js             → Entry point, orchestratore
│   ├── cursor.js           → Cursore personalizzato
│   ├── navbar.js           → Navbar sticky + menu mobile
│   ├── scroll.js           → Reveal, progress bar, back-to-top
│   ├── animations.js       → Particelle hero + typing effect
│   └── config.js           → Configurazione (Formspree, ecc.)
│
├── assets/                 → Immagini e risorse
│   ├── images/             → Immagini progetti e generali
│   ├── icons/              → Favicon e icone
│   ├── videos/             → Video (se presenti)
│   └── fonts/              → Font locali (opzionale)
│
└── projects/               → Pagine dettaglio progetti
    ├── lucifero.html
    ├── toolkit.html
    ├── training.html
    └── molinari.html
```

---

## 🚀 Come Avviare il Server Locale (macOS)

### Avvio

Apri il Terminale e naviga nella cartella del progetto:

```bash
cd /Users/samu/Downloads/portfolio
python3 -m http.server 8000
```

Il sito sarà disponibile all'indirizzo:
**http://localhost:8000**

### Arresto

Per fermare il server:
1. Apri il Terminale dove è in esecuzione il server
2. Premi `Ctrl + C`

---

## ✏️ Come Modificare le Pagine in Sicurezza

### Regole Generali

1. **Fai sempre un backup** prima di modificare file importanti
2. **Usa un editor di codice** (VS Code, Sublime Text, ecc.)
3. **Salva spesso** mentre lavori
4. **Testa le modifiche** nel browser locale dopo ogni cambiamento importante

### Modificare Testi

Cerca il testo che vuoi cambiare direttamente nel file HTML corrispondente:

- **Homepage**: `index.html`
- **About**: `about.html`
- **Servizi**: `services.html`
- **Progetti**: `projects.html`
- **Contatti**: `contact.html`

Esempio: per cambiare il titolo nella homepage, apri `index.html` e cerca:

```html
<h1 class="hero__title">
  Samuel Gentile<br>
  <span class="text-gradient" data-typing="Web Developer, Digital Solutions, Technology"></span>
</h1>
```

### Modificare Immagini

1. **Posiziona l'immagine** nella cartella `assets/images/`
2. **Usa un formato web** (JPG per foto, PNG per grafica, WebP per performance)
3. **Ottimizza le immagini** (consiglio: compressione < 500KB per foto)
4. **Aggiorna il percorso** nel file HTML:

```html
<img src="assets/images/tua-immagine.jpg" alt="Descrizione dell'immagine">
```

### Modificare Link

Cerca i tag `<a href="...">` e cambia l'URL:

```html
<a href="https://github.com/tuo-username" target="_blank" rel="noopener">GitHub</a>
```

**Nota**: `target="_blank"` apre il link in una nuova tab, `rel="noopener"` è per sicurezza.

### Modificare Colori e Stili

I colori e le spaziature sono definiti in `css/variables.css`. Esempio:

```css
:root {
  --color-primary: #6366f1;      /* Colore principale */
  --color-secondary: #8b5cf6;    /* Colore secondario */
  --color-background: #0f172a;   /* Sfondo */
  --color-text: #f8fafc;         /* Testo */
}
```

**Non modificare** direttamente `style.css` per i colori base. Usa sempre `variables.css`.

---

## ➕ Come Aggiungere Nuovi Progetti

### Metodo 1: Aggiungere al sistema JSON (Consigliato)

Il sito ora usa un sistema di configurazione JSON per gestire i progetti. Segui questi passi:

1. **Apri il file** `js/projects.json`
2. **Aggiungi un nuovo oggetto** alla lista `projects`:

```json
{
  "id": "nome-progetto",
  "title": "Titolo del Progetto",
  "description": "Breve descrizione del progetto",
  "technologies": ["HTML", "CSS", "JavaScript"],
  "status": "completed",
  "image": "assets/images/nome-progetto-cover.jpg",
  "externalLink": "https://tuo-sito.com",
  "githubLink": "https://github.com/tuo-username/repo",
  "isPrivate": false,
  "privateNote": ""
}
```

3. **Crea la pagina dettaglio** in `projects/nome-progetto.html` (copia da un progetto esistente e adatta)
4. **Il sito si aggiornerà automaticamente** in `index.html` e `projects.html`

### Metodo 2: Manuale (Senza JSON)

Se preferisci non usare il sistema JSON:

1. **Aggiungi l'immagine** in `assets/images/` (es. `nuovo-progetto-cover.jpg`)
2. **Modifica `index.html`**: cerca la sezione `<!-- PROJECTS -->` e aggiungi:

```html
<article class="card project-card reveal">
  <div class="project-card__media">
    <img src="assets/images/nuovo-progetto-cover.jpg" alt="Nome Progetto" loading="lazy">
  </div>
  <div class="project-card__body">
    <h3 class="service-card__title">Nome Progetto</h3>
    <p>Descrizione breve del progetto.</p>
    <div class="project-card__tags">
      <span class="tag">Tecnologia 1</span>
      <span class="tag">Tecnologia 2</span>
    </div>
    <a href="projects/nuovo-progetto.html" class="btn btn--secondary">Scopri di più</a>
  </div>
</article>
```

3. **Modifica `projects.html`**: aggiungi lo stesso blocco di codice
4. **Crea la pagina dettaglio** in `projects/nuovo-progetto.html` (copia da `projects/lucifero.html` e adatta)

---

## 🔒 Progetti Privati

Il sistema supporta progetti privati senza link pubblici:

### Nel file JSON (`js/projects.json`):

```json
{
  "id": "progetto-privato",
  "title": "Progetto Privato",
  "description": "Descrizione del progetto privato",
  "technologies": ["Python", "Django"],
  "status": "in_development",
  "image": "assets/images/progetto-privato-cover.jpg",
  "externalLink": null,
  "githubLink": null,
  "isPrivate": true,
  "privateNote": "Disponibile per dimostrazione su richiesta"
}
```

### Cosa succede:
- Il progetto viene mostrato professionalmente
- Appare l'etichetta "Progetto Privato"
- Se `privateNote` è presente, mostra "Disponibile per dimostrazione"
- Non ci sono link cliccabili al progetto

---

## 📧 Configurare il Form di Contatto

Il form usa **Formspree** (gratuito per siti statici).

### Passi:

1. **Crea un account** su [formspree.io](https://formspree.io)
2. **Crea un nuovo form** e ottieni il tuo endpoint (es. `https://formspree.io/f/tuo-id`)
3. **Apri il file** `js/config.js`
4. **Inserisci il tuo endpoint**:

```javascript
const CONFIG = {
  formspreeEndpoint: 'https://formspree.io/f/tuo-id'
};
```

5. **Il form è pronto** per inviare email reali

### Funzionalità incluse:
- ✅ Invio email reale
- ✅ Messaggio di successo
- ✅ Messaggio di errore
- ✅ Prevenzione invio vuoto
- ✅ Stato di caricamento durante l'invio

---

## ⚠️ Errori Comuni da Evitare

### 1. Percorsi Immagini Sbagliati

❌ **Sbagliato**:
```html
<img src="/images/foto.jpg">  <!-- Percorso assoluto, non funziona localmente -->
<img src="images/foto.jpg">   <!-- Manca la cartella assets -->
```

✅ **Giusto**:
```html
<img src="assets/images/foto.jpg">
```

### 2. Modificare File CSS Sbagliati

❌ **Non modificare** `style.css` per cambiare colori base
✅ **Modifica** `css/variables.css` per colori e spaziature

### 3. Dimenticare di Salvare

Salva sempre i file prima di ricaricare il browser!

### 4. Link Rotti

Dopo aver aggiunto una nuova pagina, verifica tutti i link che puntano ad essa.

### 5. Immagini Non Ottimizzate

Usa immagini troppo pesanti rallenta il sito. Consiglia:
- Foto: < 500KB
- Grafica: < 200KB
- Usa formati WebP quando possibile

### 6. Non Testare su Mobile

Testa sempre il sito su:
- Desktop (Chrome, Firefox, Safari)
- Mobile (simulazione nel browser F12)
- Tablet

### 7. Modificare Troppe Cose Contemporaneamente

Fai una modifica alla volta, testala, poi procedi alla successiva.

---

## 🛠️ Strumenti Utili

### Editor di Codice
- **VS Code** (raccomandato) - Gratuito, con estensioni
- **Sublime Text** - Leggero e veloce

### Estensioni VS Code Consigliate
- Live Server - Anteprima live
- Prettier - Formattazione codice
- HTML CSS Support - Autocompletamento

### Ottimizzazione Immagini
- TinyPNG - Comprimi PNG/JPG online
- Squoosh - Compressione Google (gratuito)

### Validazione
- W3C Validator - Controlla HTML/CSS
- Lighthouse - Audit performance (in Chrome DevTools)

---

## 📝 Checklist Prima del Deploy

- [ ] Tutte le immagini caricate in `assets/images/`
- [ ] Favicon presente in `assets/icons/`
- [ ] Link social aggiornati (LinkedIn, GitHub)
- [ ] Form di contatto configurato con Formspree
- [ ] Testato su desktop, tablet e mobile
- [ ] Nessun errore nella console del browser (F12)
- [ ] Tutti i link funzionano
- [ ] Meta tags aggiornati con dominio reale
- [ ] Sitemap.xml aggiornato
- [ ] Robots.txt configurato

---

## 🔧 Risoluzione Problemi

### Il sito non si vede localmente
- Controlla che il server sia attivo
- Verifica di essere su `http://localhost:8000` (non `file://`)
- Controlla che i percorsi dei file siano corretti

### Le animazioni non funzionano
- Verifica che JavaScript sia abilitato nel browser
- Controlla la console per errori (F12)
- Assicurati che i file JS siano caricati nell'ordine corretto

### Le immagini non appaiono
- Verifica il percorso dell'immagine
- Controlla che il file esista in `assets/images/`
- Verifica il nome del file (maiuscolo/minuscolo)

### Il form non invia
- Verifica che l'endpoint Formspree sia corretto in `js/config.js`
- Controlla la console per errori
- Assicurati di aver creato il form su Formspree

---

## 📚 Risorse per Imparare

### HTML/CSS
- MDN Web Docs - Documentazione ufficiale
- CSS Tricks - Guide e trucchi CSS
- freeCodeCamp - Corsi gratuiti

### JavaScript
- JavaScript.info - Guida completa
- Eloquent JavaScript - Libro gratuito online

### Web Development
- web.dev - Guide best practices Google
- A List Apart - Articoli sul web design

---

## 💡 Consigli per Sviluppatori Principianti

1. **Non aver paura di sperimentare** - Fai backup e prova
2. **Usa la console del browser** (F12) per debug
3. **Cerca su Google/Stack Overflow** prima di chiedere
4. **Leggi il codice esistente** per capire come funziona
5. **Inizia con modifiche piccole** e gradualmente aumenta la complessità
6. **Testa spesso** - Non aspettare di aver fatto tutto per testare

---

## 🆘 Hai Bisogno di Aiuto?

Se riscontri problemi:
1. Controlla la sezione "Risoluzione Problemi" sopra
2. Cerca nella console del browser (F12) errori
3. Verifica che i percorsi dei file siano corretti
4. Controlla di aver salvato tutti i file

---

Buon lavoro con il tuo portfolio! 🚀
