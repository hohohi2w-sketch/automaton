# Erzeugt alle Seiten. Aufruf: python3 build.py
import pathlib
R = pathlib.Path(__file__).parent
NAME = "Balkan<span>Flug</span>"
BRAND = "BalkanFlug"

def page(title, desc, body, depth=0):
    p = "../" * depth
    return f"""<!doctype html><html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="stylesheet" href="{p}style.css"></head><body>
<header><div class="wrap"><a class="logo" href="{p}index.html">{NAME}</a>
<nav><a href="{p}index.html#ziele">Flughäfen</a><a href="{p}index.html#extras">Mietwagen &amp; Mehr</a><a href="{p}reiseziele/index.html">Alle Ziele</a></nav></div></header>
{body}
<footer><div class="wrap"><p><a href="{p}impressum.html">Impressum</a><a href="{p}datenschutz.html">Datenschutz</a></p>
<p class="note">* Werbehinweis: Links auf dieser Seite sind Affiliate-Links. Buchst du darüber, erhalten wir eine Provision – für dich ändert sich der Preis nicht. Buchung und Vertrag erfolgen direkt beim jeweiligen Anbieter.</p>
<p>© 2026 BalkanFlug</p></div></footer>
<script src="{p}config.js"></script><script src="{p}app.js"></script></body></html>"""

# Deutsche Abflughäfen (inkl. Low-Cost-Basen, die viel auf den Balkan fliegen)
VON = [("FRA","Frankfurt"),("MUC","München"),("STR","Stuttgart"),("DUS","Düsseldorf"),("CGN","Köln/Bonn"),
       ("DTM","Dortmund"),("FMM","Memmingen"),("HHN","Frankfurt-Hahn"),("NUE","Nürnberg"),("HAM","Hamburg"),
       ("BER","Berlin"),("HAJ","Hannover"),("FKB","Karlsruhe/Baden-Baden"),("BRE","Bremen"),("LEJ","Leipzig"),("ZRH","Zürich (Schweiz)")]

# (slug, Stadt, Land, Flagge, Code, Text, Preis, Tipps, Airlines)
ZIELE = [
 ("pristina","Pristina","Kosovo","🇽🇰","PRN","Der wichtigste Flughafen für die Diaspora im Kosovo.","oft ab ~70 €",
  ["Newborn-Denkmal","Altstadt Prizren (1 Std.)","Rugova-Schlucht"],"Eurowings, Condor, Chartergesellschaften u.a."),
 ("skopje","Skopje","Nordmazedonien","🇲🇰","SKP","Hauptstadt Nordmazedoniens mit Altem Basar und Matka-Schlucht.","oft ab ~30 €",
  ["Alter Basar","Matka-Schlucht","Festung Kale"],"vor allem Wizz Air"),
 ("ohrid","Ohrid","Nordmazedonien","🇲🇰","OHD","Ohridsee – Sommerurlaub und Familienbesuch.","oft ab ~60 €",
  ["Kirche Sveti Jovan Kaneo","Bootsfahrt auf dem See","Kloster Sveti Naum"],"saisonal"),
 ("tirana","Tirana","Albanien","🇦🇱","TIA","Albaniens Drehkreuz – und Start zur albanischen Riviera.","oft ab ~40 €",
  ["Skanderbeg-Platz","Bunk'Art","Riviera: Ksamil & Himara"],"Wizz Air, Ryanair, Eurowings u.a."),
 ("podgorica","Podgorica","Montenegro","🇲🇪","TGD","Montenegros Hauptstadt, nah an Budva und Skutarisee.","oft ab ~70 €",
  ["Skutarisee","Budva","Kloster Ostrog"],"Direkt- und Umsteigeflüge"),
 ("zuerich","Zürich","Schweiz","🇨🇭","ZRH","Größte Stadt der Schweiz – Altstadt, Zürichsee und Alpen in der Nähe.","oft ab ~60 €",
  ["Altstadt & Bahnhofstrasse","Zürichsee-Schifffahrt","Uetliberg","Rheinfall (40 Min.)"],"Swiss, Lufthansa, Eurowings u.a."),
]
LAENDER = []
for z in ZIELE:
    if z[2] not in LAENDER: LAENDER.append(z[2])

von_opts = "".join(f'<option value="{c}">{n} ({c})</option>' for c,n in VON)
nach_opts = "".join(f'<optgroup label="{l}">' + "".join(f'<option value="{z[4]}">{z[1]} ({z[4]})</option>' for z in ZIELE if z[2]==l) + "</optgroup>" for l in LAENDER)

def card(z,p=""):
    s,n,l,f,c,t,pr,_,_ = z
    return f"""<div class="card"><div class="img" style="background:#e8f1fb">{f}</div><div class="body">
<h3>{n}</h3><p>{l} · {t}</p><span class="price">Flüge {pr}</span>
<button class="btn" onclick="flugZiel('FRA','{c}')">Flüge ab Frankfurt*</button>
<a href="{p}reiseziele/{s}.html">Alle Abflughäfen & Tipps →</a></div></div>"""

sektionen = "".join(f'<h3 style="margin:28px 0 12px">{l}</h3><div class="grid">' + "".join(card(z) for z in ZIELE if z[2]==l) + "</div>" for l in LAENDER)

index = f"""<div class="hero"><div class="wrap">
<h1>Günstige Flüge auf den Balkan</h1>
<p>Nach Hause, zur Familie oder in den Urlaub – Kosovo, Albanien, Nordmazedonien, Montenegro und Zürich. Ab Deutschland und ab Zürich. Wir vergleichen alle Airlines für dich.</p>
<form class="search" onsubmit="flugSuche(event)">
<div><label>Von</label><select name="von">{von_opts}</select></div>
<div><label>Nach</label><select name="nach">{nach_opts}</select></div>
<div><label>Hinflug</label><input type="date" name="hin" required></div>
<div><label>Rückflug (optional)</label><input type="date" name="rueck"></div>
<div><label>Personen</label><select name="pax"><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option><option>6</option></select></div>
<div><button class="btn" type="submit">Flüge suchen*</button></div></form>
<p class="note" style="color:#fff;margin-top:10px">Mirë se vini · Добредојдовте · Dobrodošli · Grüezi</p>
</div></div>
<section><div class="wrap"><div class="usp">
<div><h3>✈️ Alle Airlines</h3><p>Wizz Air, Eurowings, Condor, Swiss, Ryanair und mehr im Vergleich.</p></div>
<div><h3>🏠 Heimatflüge</h3><p>Sommerferien und Weihnachten früh buchen – dann sind die Preise am niedrigsten.</p></div>
<div><h3>🧳 Tipp Gepäck</h3><p>Bei Low-Cost-Airlines Koffer gleich mitbuchen, am Flughafen kostet es oft das Doppelte.</p></div>
</div></div></section>
<section id="ziele"><div class="wrap"><h2>Unsere Ziele</h2>{sektionen}</div></section>
<section id="extras"><div class="wrap"><h2>Alles für deine Reise</h2><div class="usp">
<div><h3>🚗 Mietwagen</h3><p>Mietwagen direkt am Flughafen – praktisch für Familienbesuche auf dem Land.</p><a class="btn" data-partner="mietwagenLink" href="#">Mietwagen suchen*</a></div>
<div><h3>🏨 Hotels</h3><p>Unterkünfte in Tirana, Pristina, Ohrid, Zürich oder an der Albanischen Riviera.</p><a class="btn" data-partner="hotelLink" href="#">Hotels finden*</a></div>
<div><h3>🛡️ Reiseversicherung</h3><p>Wichtig: Kosovo, Albanien, Montenegro und Nordmazedonien sind nicht in der EU – die EU-Krankenversicherungskarte gilt dort nur eingeschränkt oder gar nicht.</p><a class="btn" data-partner="versicherungLink" href="#">Versicherung prüfen*</a></div>
<div><h3>🎟️ Ausflüge</h3><p>Touren nach Prizren, Kotor, zum Ohridsee oder zur Albanischen Riviera.</p><a class="btn" data-partner="aktivitaetenLink" href="#">Ausflüge buchen*</a></div>
</div></div></section>"""
(R/"index.html").write_text(page(f"{BRAND} – Günstige Flüge nach Kosovo, Albanien, Nordmazedonien, Montenegro & Zürich","Günstige Flüge ab Deutschland und Zürich nach Pristina, Tirana, Skopje, Ohrid, Podgorica – und nach Zürich – im Vergleich.",index))

liste = "".join(f'<h2>{l}</h2><ul>' + "".join(f'<li><a href="{z[0]}.html">Flüge nach {z[1]} ({z[4]})</a></li>' for z in ZIELE if z[2]==l) + "</ul>" for l in LAENDER)
(R/"reiseziele/index.html").write_text(page(f"Alle Ziele – {BRAND}","Übersicht aller Ziele mit günstigen Flügen ab Deutschland und Zürich.",f'<section><div class="wrap"><h1>Alle Flughäfen</h1>{liste}</div></section>',1))

for z in ZIELE:
    s,n,l,f,c,t,pr,tipps,air = z
    li = "".join(f"<li>{x}</li>" for x in tipps)
    btns = " ".join(f"""<button class="btn" style="margin:4px 0" onclick="flugZiel('{vc}','{c}')">ab {vn}</button>""" for vc,vn in VON if vc!=c)
    body = f"""<section><div class="wrap"><article>
<h1>{f} Günstige Flüge nach {n} ({c})</h1><p>{t} Flugpreise ab Deutschland bzw. Zürich: {pr} (je nach Saison und Abflughafen).</p>
<h2>Flüge nach {n} – wähle deinen Abflughafen</h2><p>{btns}</p>
<p class="note">Nicht jeder Flughafen hat Direktflüge, der Vergleich zeigt dir auch Verbindungen mit Umstieg.</p>
<h2>Welche Airlines fliegen nach {n}?</h2><p>{air}. Der Flugplan ändert sich je nach Saison, der Vergleich zeigt immer die aktuellen Verbindungen.</p>
<h2>Spartipps für Flüge nach {n}</h2><ul>
<li>Für Sommerferien und Weihnachten 2–4 Monate vorher buchen, dann steigen die Preise stark.</li>
<li>Flexibel sein: Dienstag und Mittwoch sind oft am günstigsten.</li>
<li>Nahe Flughäfen vergleichen – manchmal ist ein Nachbarland deutlich billiger.</li>
<li>Bei Low-Cost-Airlines Gepäck direkt bei der Buchung dazunehmen.</li></ul>
<h2>Vor Ort in {n}</h2><ul>{li}</ul>
<p><a class="btn" data-partner="mietwagenLink" href="#">Mietwagen in {n}*</a> <a class="btn" data-partner="hotelLink" href="#">Hotels*</a> <a class="btn" data-partner="versicherungLink" href="#">Reiseversicherung*</a></p>
</article></div></section>"""
    (R/f"reiseziele/{s}.html").write_text(page(f"Günstige Flüge nach {n} ({c}) | {BRAND}",f"Billigflüge nach {n}, {l}: alle Abflughäfen in Deutschland und Zürich, Airlines und Spartipps im Vergleich.",body,1))

legal = '<section><div class="wrap"><article><h1>{h}</h1>{b}</article></div></section>'
(R/"impressum.html").write_text(page("Impressum – BalkanFlug","Impressum",legal.format(h="Impressum",b="""
<p><b>⚠️ PFLICHT: Vor Veröffentlichung ausfüllen (§ 5 DDG)!</b></p>
<p>Angaben gemäß § 5 DDG:<br>[Vor- und Nachname]<br>[Straße Hausnummer]<br>[PLZ Ort]<br>Deutschland</p>
<p>Kontakt: E-Mail: [deine@email.de]</p>
<p>Umsatzsteuer: [Kleinunternehmer gem. § 19 UStG / USt-IdNr.]</p>
<p>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV: [Name, Anschrift]</p>
<p>BalkanFlug ist ein Vergleichs- und Informationsportal und kein Reiseveranstalter. Verträge kommen ausschließlich mit den verlinkten Anbietern zustande.</p>""")))
(R/"datenschutz.html").write_text(page("Datenschutz – BalkanFlug","Datenschutzerklärung",legal.format(h="Datenschutzerklärung",b="""
<p><b>⚠️ Vorlage – bitte mit einem Generator (z.B. e-recht24.de oder datenschutz-generator.de) vervollständigen.</b></p>
<h2>Verantwortlicher</h2><p>[Name, Anschrift, E-Mail wie im Impressum]</p>
<h2>Hosting</h2><p>Diese Website wird bei Netlify, Inc. gehostet. Beim Aufruf werden technisch notwendige Daten (z.B. IP-Adresse, Zeitpunkt) verarbeitet (Art. 6 Abs. 1 lit. f DSGVO).</p>
<h2>Affiliate-Links</h2><p>Klickst du auf einen Partnerlink, wirst du zum Anbieter (z.B. Aviasales/Travelpayouts) weitergeleitet. Dieser kann Cookies setzen, um die Vermittlung zuzuordnen. Es gelten die Datenschutzbestimmungen des Anbieters.</p>
<h2>Cookies</h2><p>Diese Seite selbst setzt keine Tracking-Cookies.</p>
<h2>Deine Rechte</h2><p>Auskunft, Berichtigung, Löschung, Einschränkung, Widerspruch, Datenübertragbarkeit sowie Beschwerde bei einer Aufsichtsbehörde.</p>""")))
print("ok")
