# Guida al Deploy - Portfolio Samuel Gentile

Questa guida spiega come pubblicare il tuo portfolio online gratuitamente.

---

## 📋 Prerequisiti

Prima di iniziare, assicurati di:

- [ ] Avere un account GitHub
- [ ] Avere completato la configurazione del form di contatto (vedi `README_DEV.md`)
- [ ] Avere aggiunto tutte le immagini in `assets/images/`
- [ ] Avere testato il sito localmente con `python3 -m http.server 8000`
- [ ] Avere aggiornato i meta tags con il tuo dominio reale

---

## 🚀 Opzione A: GitHub Pages (Consigliato)

GitHub Pages è la soluzione più semplice per siti statici. È gratuita, integrata con Git e supporta custom domain.

### Passo 1: Crea una Repository su GitHub

1. Vai su [github.com](https://github.com) e accedi
2. Clicca su **+** in alto a destra → **New repository**
3. Compila i campi:
   - **Repository name**: `portfolio` (o il nome che preferisci)
   - **Description**: `Portfolio personale di Samuel Gentile`
   - **Public/Private**: Scegli **Public** (per GitHub Pages gratuito)
4. Clicca su **Create repository**

### Passo 2: Carica i File del Progetto

#### Opzione 1: Tramite GitHub Web Interface (Semplice)

1. Nella repository appena creata, clicca su **uploading an existing file**
2. Trascina tutta la cartella `portfolio` nel browser
3. Assicurati che tutti i file siano nella root (non in una sottocartella)
4. Scorri in fondo e clicca su **Commit changes**

#### Opzione 2: Tramite Git Command Line (Consigliato per sviluppatori)

Apri il Terminale nella cartella del progetto:

```bash
cd /Users/samu/Downloads/portfolio

# Inizializza Git (se non l'hai già fatto)
git init

# Aggiungi tutti i file
git add .

# Crea il primo commit
git commit -m "Initial commit - Portfolio website"

# Aggiungi la repository remota
git remote add origin https://github.com/tuo-username/portfolio.git

# Push su GitHub
git branch -M main
git push -u origin main
```

### Passo 3: Attiva GitHub Pages

1. Vai sulla tua repository su GitHub
2. Clicca su **Settings** (in alto)
3. Nel menu a sinistra, clicca su **Pages**
4. In **Build and deployment** → **Source**, seleziona:
   - **Deploy from a branch**
   - **Branch**: `main`
   - **Folder**: `/ (root)`
5. Clicca su **Save**

### Passo 4: Attendi il Deploy

- GitHub impiega circa 1-2 minuti per il deploy iniziale
- Vedrai un checkmark verde quando è completato
- Il tuo sito sarà disponibile a: `https://tuo-username.github.io/portfolio/`

### Passo 5: (Opzionale) Connetti un Dominio Personalizzato

Se hai un dominio proprio (es. `samuelgentile.dev`):

1. In **Settings → Pages**, sotto **Custom domain**, inserisci il tuo dominio
2. Clicca su **Save**
3. GitHub ti mostrerà i DNS record da aggiungere nel tuo provider di dominio
4. Aggiungi i record DNS nel tuo provider (GoDaddy, Namecheap, ecc.)
5. Attendi la propagazione DNS (può richiedere fino a 48 ore)

---

## 🌐 Opzione B: Netlify

Netlify è un'altra ottima opzione per siti statici, con funzionalità avanzate come form gratuiti e redirect.

### Vantaggi
- ✅ Deploy automatico da GitHub
- ✅ Form gratuiti integrati (alternativa a Formspree)
- ✅ HTTPS automatico
- ✅ Preview URLs per ogni commit
- ✅ Funzioni serverless (per funzionalità avanzate)

### Svantaggi
- ❌ Richiede account separato da GitHub
- ❌ Interfaccia più complessa per principianti

### Passo 1: Crea Account Netlify

1. Vai su [netlify.com](https://netlify.com) e registrati
2. Puoi usare il tuo account GitHub per l'accesso

### Passo 2: Connetti la Repository GitHub

1. Nel dashboard Netlify, clicca su **Add new site** → **Import an existing project**
2. Seleziona GitHub e autorizza Netlify
3. Scegli la repository `portfolio`
4. Configura le impostazioni di build:
   - **Build command**: (lascia vuoto - è un sito statico)
   - **Publish directory**: (lascia vuoto o metti `.`)
5. Clicca su **Deploy site**

### Passo 3: Configura il Dominio

1. Dopo il deploy, clicca su **Site settings** → **Domain management**
2. Puoi usare il dominio gratuito Netlify (`nome-sito.netlify.app`)
3. Oppure connettere un dominio personalizzato

---

## ⚡ Opzione C: Vercel

Vercel è simile a Netlify, ottimizzato per framework moderni ma funziona anche per siti statici.

### Vantaggi
- ✅ Performance eccellenti
- ✅ Edge network globale
- ✅ Integrazione perfetta con GitHub
- ✅ Preview URLs automatiche

### Svantaggi
- ❌ Interfaccia pensata per framework React/Next.js
- ❌ Alcune funzionalità avanzate sono a pagamento

### Passo 1: Crea Account Vercel

1. Vai su [vercel.com](https://vercel.com) e registrati
2. Usa il tuo account GitHub

### Passo 2: Importa la Repository

1. Clicca su **Add New Project**
2. Seleziona la repository `portfolio` da GitHub
3. Configura:
   - **Framework Preset**: Other
   - **Build Command**: (lascia vuoto)
   - **Output Directory**: (lascia vuoto)
4. Clicca su **Deploy**

---

## 📊 Confronto delle Opzioni

| Caratteristica | GitHub Pages | Netlify | Vercel |
|----------------|--------------|---------|--------|
| **Costo** | Gratis | Gratis (con limiti) | Gratis (con limiti) |
| **Facilità d'uso** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Integrazione GitHub** | Nativa | Eccellente | Eccellente |
| **Form gratuiti** | No (serve Formspree) | Sì | No |
| **Custom domain** | Sì | Sì | Sì |
| **HTTPS** | Sì automatico | Sì automatico | Sì automatico |
| **Preview URLs** | No | Sì | Sì |
| **Performance** | Buona | Eccellente | Eccellente |

### Raccomandazione

**Per principianti**: GitHub Pages
- Più semplice da configurare
- Tutto in un posto (GitHub)
- Perfetto per siti statici

**Per funzionalità avanzate**: Netlify
- Form integrati gratuiti
- Redirect facili
- Funzioni serverless

**Per performance massime**: Vercel
- CDN globale
- Edge computing
- Ottimo per progetti futuri con framework

---

## 🔧 Configurazioni Post-Deploy

### Aggiornare robots.txt

Dopo il deploy, aggiorna `robots.txt` con il tuo dominio reale:

```txt
User-agent: *
Allow: /
Sitemap: https://tuo-dominio.com/sitemap.xml
```

### Aggiornare sitemap.xml

Modifica `sitemap.xml` con il tuo dominio:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://tuo-dominio.com/</loc>
    <lastmod>2026-01-01</lastmod>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>
  <!-- Aggiungi altre pagine... -->
</urlset>
```

### Aggiornare Meta Tags Open Graph

In tutti i file HTML, aggiorna l'URL nei meta Open Graph:

```html
<meta property="og:url" content="https://tuo-dominio.com/">
```

### Testare il Form di Contatto

1. Assicurati che `js/config.js` abbia l'endpoint Formspree corretto
2. Invia un messaggio di test dal sito live
3. Verifica di ricevere l'email

---

## 🚨 Risoluzione Problemi Comuni

### Il sito non appare dopo il deploy su GitHub Pages

- **Attendi 2-3 minuti** - Il deploy iniziale richiede tempo
- **Verifica il branch** - Assicurati di aver selezionato `main`
- **Controlla la cartella** - Deve essere `/ (root)`, non una sottocartella
- **Controlla i log** - In Settings → Pages, vedi se ci sono errori

### Le immagini non appaiono

- **Verifica i percorsi** - Devono essere relativi: `assets/images/nome.jpg`
- **Verifica il maiuscolo/minuscolo** - I file sono case-sensitive su Linux
- **Controlla che i file esistano** - Assicurati di aver caricato tutto

### Il form non invia email

- **Verifica l'endpoint** in `js/config.js`
- **Controlla la console** del browser per errori (F12)
- **Verifica Formspree** - Accedi al dashboard per vedere se i messaggi arrivano

### Il sito appare "rotto" o senza stile

- **Verifica i percorsi CSS** - Devono essere `css/style.css`, non `/css/style.css`
- **Controlla la console** per errori di caricamento file
- **Verifica che i file CSS siano stati caricati** su GitHub

### Custom domain non funziona

- **Attendi la propagazione DNS** - Può richiedere fino a 48 ore
- **Verifica i record DNS** - Devono corrispondere a quelli indicati da GitHub/Netlify
- **Controlla che il dominio sia attivo** - Non scaduto

---

## 📈 Monitoraggio e Analytics

### Google Analytics (Opzionale)

Per tracciare le visite al sito:

1. Crea un account [Google Analytics](https://analytics.google.com)
2. Crea una nuova proprietà per il tuo sito
3. Copia il codice di tracciamento
4. Aggiungilo prima di `</head>` in tutti i file HTML

### Google Search Console

Per indicizzare il sito su Google:

1. Vai su [Search Console](https://search.google.com/search-console)
2. Aggiungi la proprietà per il tuo dominio
3. Verifica la proprietà (tramite DNS o file HTML)
4. Invia la sitemap in `Sitemaps`

---

## 🔄 Aggiornamenti Futuri

Per aggiornare il sito dopo il deploy:

### GitHub Pages
```bash
# Apporta le modifiche localmente
git add .
git commit -m "Descrizione delle modifiche"
git push
```
GitHub Pages farà il deploy automaticamente.

### Netlify/Vercel
- Push su GitHub
- Netlify/Vercel deploy automaticamente
- Riceverai una notifica quando il deploy è completato

---

## 💡 Best Practices

### Sicurezza
- Non caricare credenziali o API keys nel repository
- Usa environment variables per dati sensibili
- Mantieni il repository privato se contiene dati sensibili

### Performance
- Ottimizza le immagini prima del caricamento
- Usa formati moderni (WebP, AVIF)
- Minifica CSS/JS se possibile (non essenziale per siti piccoli)

### SEO
- Usa meta description uniche per ogni pagina
- Mantieni i titoli descrittivi
- Crea contenuti di qualità
- Ottieni backlink da altri siti

### Manutenzione
- Aggiorna regolarmente le dipendenze (se ne aggiungi in futuro)
- Controlla periodicamente i link rotti
- Aggiorna i progetti nel portfolio regolarmente
- Rinnova il dominio annualmente se ne usi uno personalizzato

---

## 📞 Supporto

Se riscontri problemi:

1. **Controlla la documentazione ufficiale**:
   - [GitHub Pages Docs](https://docs.github.com/pages)
   - [Netlify Docs](https://docs.netlify.com)
   - [Vercel Docs](https://vercel.com/docs)

2. **Cerca su Google/Stack Overflow** - Molto probabilmente qualcuno ha già avuto il tuo problema

3. **Controlla i log** - Tutte le piattaforme hanno log di deploy dettagliati

---

Buon deploy! 🚀
