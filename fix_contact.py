from pathlib import Path

file = Path("contact.html")

html = file.read_text()

start = html.index('<form class="contact-form reveal">')
end = html.index('</form>', start)

new_form = r'''
<form class="contact-form reveal">

  <div class="form-group">
    <label for="message">Messaggio</label>
    <textarea id="message" name="message" required placeholder="Raccontami del tuo progetto..."></textarea>
  </div>

  <div class="form-group">
    <label for="type">Tipo di progetto</label>
    <select id="type" name="type">
      <option value="Sito web">Sito web</option>
      <option value="Landing page">Landing page</option>
      <option value="Restyling">Restyling sito</option>
      <option value="Applicazione web">Applicazione web</option>
      <option value="Altro">Altro</option>
    </select>
  </div>

  <div class="form-group">
    <label for="company">Attività / Azienda</label>
    <input type="text" id="company" name="company" placeholder="Nome attività (opzionale)">
  </div>

  <div class="form-group">
    <label for="name">Nome</label>
    <input type="text" id="name" name="name" required placeholder="Il tuo nome">
  </div>

  <div class="form-group">
    <label for="email">Email</label>
    <input type="email" id="email" name="email" required placeholder="tuaemail@esempio.com">
  </div>

  <div class="form-group">
    <label for="details">Dettagli</label>
    <textarea id="details" name="details" required placeholder="Descrivi la tua attività, il tuo obiettivo e cosa vorresti migliorare..."></textarea>
  </div>

  <button type="submit" class="btn btn--primary">
    Richiedi una consulenza
  </button>

</form>
'''

html = html[:start] + new_form + html[end+7:]

file.write_text(html)


# CSS fix
css = Path("css/style.css")
style = css.read_text()

extra = """

/* CONTACT FORM IMPROVEMENTS */

.contact-form select {
  width:100%;
  min-height:56px;
  padding:0 18px;
  border-radius:14px;
  background:#1b1e26;
  color:#fff;
  border:1px solid rgba(255,255,255,.12);
  font-size:1rem;
}

.contact-form textarea,
.contact-form input {
  background:#1b1e26;
  color:#fff;
}

.contact-form textarea::placeholder,
.contact-form input::placeholder {
  color:#9ca3af;
}

.contact-form select option {
  background:#1b1e26;
  color:white;
}

.contact-form .btn--primary {
  margin-top:25px;
  margin-bottom:40px;
}

"""

if "CONTACT FORM IMPROVEMENTS" not in style:
    css.write_text(style + extra)


print("✅ Contact sistemato correttamente")
