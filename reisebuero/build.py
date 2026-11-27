# Erzeugt alle Seiten. Aufruf: python3 build.py
import pathlib
R = pathlib.Path(__file__).parent
NAME = "Fernweh<span>Flug</span>"

def page(title, desc, body, depth=0):
    p = "../" * depth
    return f"""<!doctype html><html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="stylesheet" href="{p}style.css"></head><body>
<header><div class="wrap"><a class="logo" href="{p}index.html">{NAME}</a>
<nav><a href="{p}index.html#ziele">Reiseziele</a><a href="{p}index.html#extras">Hotels &amp; Mehr</a><a href="{p}reiseziele/index.html">Reiseführer</a></nav></div></header>
{body}
<footer><div class="wrap"><p><a href="{p}impressum.html">Impressum</a><a href="{p}datenschutz.html">Datenschutz</a></p>
<p class="note">* Werbehinweis: Links auf dieser Seite sind Affiliate-Links. Buchst du darüber, erhalten wir eine Provision – für dich ändert sich der Preis nicht. Buchung und Vertrag erfolgen direkt beim jeweiligen Anbieter.</p>
<p>© 2026 FernwehFlug</p></div></footer>
<script src="{p}config.js"></script><script src="{p}app.js"></script></body></html>"""

ZIELE = [
  ("barcelona","Barcelona","🏖️","BCN","Strand, Gaudí und Tapas – ideal für 4–5 Tage.","ab ~60 €",
   ["Sagrada Família (Tickets vorab buchen!)","Park Güell & Gràcia","Barceloneta-Strand","Montjuïc bei Sonnenuntergang"],"April–Juni, September–Oktober"),
  ("mallorca","Mallorca","🌴","PMI","Die Lieblingsinsel der Deutschen: Buchten, Berge, Palma.","ab ~50 €",
   ["Altstadt von Palma & Kathedrale","Serra de Tramuntana wandern","Cala Mondragó baden","Valldemossa"],"Mai–Juni, September"),
  ("lissabon","Lissabon","🚋","LIS","Hügel, Tram 28, Pastéis de Nata und Atlantik.","ab ~70 €",
   ["Alfama & Tram 28","Belém-Turm & Pastéis","Tagesausflug nach Sintra","Surfen in Cascais"],"März–Juni, September–Oktober"),
  ("rom","Rom","🏛️","FCO","2.000 Jahre Geschichte an jeder Ecke.","ab ~55 €",
   ["Kolosseum & Forum (Skip-the-line)","Vatikanische Museen","Trastevere am Abend","Trevi-Brunnen früh morgens"],"April–Mai, Oktober"),
  ("antalya","Antalya","☀️","AYT","All-inclusive, türkisches Meer, Sonne bis Oktober.","ab ~80 €",
   ["Altstadt Kaleiçi","Düden-Wasserfälle","Antike Stadt Perge","Bootstour an der Küste"],"Mai–Oktober"),
  ("dubai","Dubai","🌆","DXB","Winter-Sonne mit Wüste, Malls und Skyline.","ab ~250 €",
   ["Burj Khalifa Aussichtsplattform","Wüstensafari","Dubai Marina & JBR-Strand","Altstadt & Gold-Souk"],"November–März"),
]

cards = "".join(f"""<div class="card"><div class="img" style="background:#e8f1fb">{e}</div><div class="body">
<h3>{n}</h3><p>{t}</p><span class="price">Flüge {pr}</span>
<button class="btn" onclick="flugZiel('FRA','{c}')">Flüge ansehen*</button>
<a href="reiseziele/{s}.html">Reiseführer lesen →</a></div></div>""" for s,n,e,c,t,pr,_,_ in ZIELE)

index = f"""<div class="hero"><div class="wrap">
<h1>Günstige Flüge finden. Mehr erleben.</h1><p>Wir vergleichen hunderte Airlines & Portale – du buchst zum besten Preis.</p>
<form class="search" onsubmit="flugSuche(event)">
<div><label>Von (Code)</label><input name="von" value="FRA" maxlength="3" required></div>
<div><label>Nach (Code)</label><input name="nach" placeholder="z.B. BCN" maxlength="3" required></div>
<div><label>Hinflug</label><input type="date" name="hin" required></div>
<div><label>Rückflug (optional)</label><input type="date" name="rueck"></div>
<div><label>Personen</label><select name="pax"><option>1</option><option>2</option><option>3</option><option>4</option></select></div>
<div><button class="btn" type="submit">Flüge suchen*</button></div></form>
<p class="note" style="color:#fff;margin-top:10px">Codes: FRA Frankfurt · MUC München · BER Berlin · HAM Hamburg · DUS Düsseldorf · CGN Köln · STR Stuttgart</p>
</div></div>
<section id="ziele"><div class="wrap"><h2>Beliebte Reiseziele</h2><div class="grid">{cards}</div></div></section>
<section id="extras"><div class="wrap"><h2>Alles für deine Reise</h2><div class="usp">
<div><h3>🏨 Hotels</h3><p>Unterkünfte weltweit vergleichen.</p><a class="btn" data-partner="hotelLink" href="#">Hotels finden*</a></div>
<div><h3>🎟️ Aktivitäten</h3><p>Touren & Tickets ohne Anstehen.</p><a class="btn" data-partner="aktivitaetenLink" href="#">Erlebnisse buchen*</a></div>
<div><h3>🚗 Mietwagen</h3><p>Mietwagen inkl. Vollkasko vergleichen.</p><a class="btn" data-partner="mietwagenLink" href="#">Mietwagen suchen*</a></div>
<div><h3>🛡️ Reiseversicherung</h3><p>Auslandskranken- & Reiseschutz.</p><a class="btn" data-partner="versicherungLink" href="#">Versicherung prüfen*</a></div>
</div></div></section>"""
(R/"index.html").write_text(page("FernwehFlug – Günstige Flüge, Hotels & Reiseführer","Günstige Flüge vergleichen, Hotels und Aktivitäten finden – plus ehrliche Reiseführer für Barcelona, Mallorca, Lissabon und mehr.",index))

liste = "".join(f'<li><a href="{s}.html">{n} – Reiseführer & günstige Flüge</a></li>' for s,n,*_ in ZIELE)
(R/"reiseziele/index.html").write_text(page("Reiseführer – FernwehFlug","Alle Reiseführer von FernwehFlug.",f'<section><div class="wrap"><h1>Reiseführer</h1><ul>{liste}</ul></div></section>',1))

for s,n,e,c,t,pr,tipps,zeit in ZIELE:
    li = "".join(f"<li>{x}</li>" for x in tipps)
    body = f"""<section><div class="wrap"><article>
<h1>{e} {n}: Reiseführer & günstige Flüge</h1><p>{t}</p>
<h2>Beste Reisezeit</h2><p>{zeit}. Außerhalb der Ferien sind Flüge oft 30–50 % günstiger.</p>
<h2>Top-Sehenswürdigkeiten</h2><ul>{li}</ul>
<p><a class="btn" data-partner="aktivitaetenLink" href="#">Tickets & Touren in {n}*</a></p>
<h2>Günstige Flüge nach {n}</h2><p>Flugpreise {pr}. Tipp: Dienstag/Mittwoch fliegen und 6–8 Wochen vorher buchen.</p>
<p><button class="btn" onclick="flugZiel('FRA','{c}')">Ab Frankfurt</button> <button class="btn" onclick="flugZiel('MUC','{c}')">Ab München</button> <button class="btn" onclick="flugZiel('BER','{c}')">Ab Berlin</button></p>
<h2>Unterkunft</h2><p>Vergleiche Hotels und Apartments – zentrale Lage spart Zeit und Transportkosten.</p>
<p><a class="btn" data-partner="hotelLink" href="#">Hotels in {n}*</a> <a class="btn" data-partner="mietwagenLink" href="#">Mietwagen*</a></p>
</article></div></section>"""
    (R/f"reiseziele/{s}.html").write_text(page(f"{n} Reiseführer 2026 – Tipps & günstige Flüge | FernwehFlug",f"{n}: beste Reisezeit, Top-Sehenswürdigkeiten und günstige Flüge ab Deutschland.",body,1))

legal = '<section><div class="wrap"><article><h1>{h}</h1>{b}</article></div></section>'
(R/"impressum.html").write_text(page("Impressum – FernwehFlug","Impressum",legal.format(h="Impressum",b="""
<p><b>⚠️ PFLICHT: Vor Veröffentlichung ausfüllen (§ 5 DDG)!</b></p>
<p>Angaben gemäß § 5 DDG:<br>[Vor- und Nachname]<br>[Straße Hausnummer]<br>[PLZ Ort]<br>Deutschland</p>
<p>Kontakt: E-Mail: [deine@email.de]</p>
<p>Umsatzsteuer: [Kleinunternehmer gem. § 19 UStG / USt-IdNr.]</p>
<p>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV: [Name, Anschrift]</p>
<p>FernwehFlug ist ein Vergleichs- und Informationsportal und kein Reiseveranstalter. Verträge kommen ausschließlich mit den verlinkten Anbietern zustande.</p>""")))
(R/"datenschutz.html").write_text(page("Datenschutz – FernwehFlug","Datenschutzerklärung",legal.format(h="Datenschutzerklärung",b="""
<p><b>⚠️ Vorlage – bitte mit einem Generator (z.B. e-recht24.de oder datenschutz-generator.de) vervollständigen.</b></p>
<h2>Verantwortlicher</h2><p>[Name, Anschrift, E-Mail wie im Impressum]</p>
<h2>Hosting</h2><p>Diese Website wird bei Netlify, Inc. gehostet. Beim Aufruf werden technisch notwendige Daten (z.B. IP-Adresse, Zeitpunkt) verarbeitet (Art. 6 Abs. 1 lit. f DSGVO).</p>
<h2>Affiliate-Links</h2><p>Klickst du auf einen Partnerlink, wirst du zum Anbieter (z.B. Aviasales/Travelpayouts) weitergeleitet. Dieser kann Cookies setzen, um die Vermittlung zuzuordnen. Es gelten die Datenschutzbestimmungen des Anbieters.</p>
<h2>Cookies</h2><p>Diese Seite selbst setzt keine Tracking-Cookies.</p>
<h2>Deine Rechte</h2><p>Auskunft, Berichtigung, Löschung, Einschränkung, Widerspruch, Datenübertragbarkeit sowie Beschwerde bei einer Aufsichtsbehörde.</p>""")))
print("ok")
