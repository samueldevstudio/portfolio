from pathlib import Path

file = Path("contact.html")

html = file.read_text()

# Controlla se esiste già
if '_subject' in html:
    print("✅ Subject Formspree già presente")
else:
    target = 'method="POST">'
    
    if target in html:
        html = html.replace(
            target,
            target + '\n\n<input type="hidden" name="_subject" value="Nuova richiesta dal portfolio Samuel.dev">',
            1
        )
        file.write_text(html)
        print("✅ Subject Formspree aggiunto correttamente")
    else:
        print("❌ Non trovato method POST nel form")

