# Erzeugt alle Seiten. Aufruf: python3 build.py
import pathlib
R = pathlib.Path(__file__).parent
NAME = "Balkan<span>Wings</span>"
BRAND = "BalkanWings"

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
<p>© 2026 BalkanWings</p></div></footer>
<script src="{p}config.js"></script><script src="{p}app.js"></script></body></html>"""

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
 ("basel","Basel","Schweiz","🇨🇭","BSL","Kulturstadt am Rhein im Dreiländereck Schweiz–Deutschland–Frankreich.","oft ab ~60 €",
  ["Altstadt & Basler Münster","Rheinschwimmen im Sommer","Kunstmuseum & Fondation Beyeler","Basler Fasnacht"],"easyJet, Wizz Air u.a."),
 ("frankfurt","Frankfurt","Deutschland","🇩🇪","FRA","Größter Flughafen Deutschlands – Drehkreuz für fast alle Airlines.","",
  ['Römerberg & Altstadt', 'Skyline & Main Tower', 'Museumsufer'],"Verschiedene Airlines, direkt oder mit Umstieg"),
 ("muenchen","München","Deutschland","🇩🇪","MUC","Bayerns Hauptstadt und zweitgrößter Flughafen Deutschlands.","",
  ['Marienplatz', 'Englischer Garten', 'Oktoberfest (Sept./Okt.)'],"Verschiedene Airlines, direkt oder mit Umstieg"),
 ("stuttgart","Stuttgart","Deutschland","🇩🇪","STR","Schwabens Metropole mit vielen Verbindungen auf den Balkan.","",
  ['Schlossplatz', 'Mercedes-Benz- und Porsche-Museum', 'Weinberge am Neckar'],"Verschiedene Airlines, direkt oder mit Umstieg"),
 ("duesseldorf","Düsseldorf","Deutschland","🇩🇪","DUS","Großer Flughafen in NRW mit vielen Ferienflügen.","",
  ['Altstadt', 'Rheinuferpromenade', 'Königsallee'],"Verschiedene Airlines, direkt oder mit Umstieg"),
 ("koeln","Köln/Bonn","Deutschland","🇩🇪","CGN","Low-Cost-Drehkreuz im Rheinland.","",
  ['Kölner Dom', 'Altstadt am Rhein', 'Karneval'],"Verschiedene Airlines, direkt oder mit Umstieg"),
 ("dortmund","Dortmund","Deutschland","🇩🇪","DTM","Kleiner Flughafen im Ruhrgebiet mit vielen günstigen Balkan-Flügen.","",
  ['Deutsches Fußballmuseum', 'Signal Iduna Park', 'Phoenix-See'],"Verschiedene Airlines, direkt oder mit Umstieg"),
 ("memmingen","Memmingen","Deutschland","🇩🇪","FMM","Allgäu-Airport – günstig für Süddeutschland.","",
  ['Historische Altstadt', 'Allgäuer Alpen', 'Schloss Neuschwanstein (ca. 1,5 Std.)'],"Verschiedene Airlines, direkt oder mit Umstieg"),
 ("hahn","Frankfurt-Hahn","Deutschland","🇩🇪","HHN","Low-Cost-Flughafen im Hunsrück.","",
  ['Mosel-Tal', 'Hunsrück wandern', 'Busverbindung nach Frankfurt'],"Verschiedene Airlines, direkt oder mit Umstieg"),
 ("nuernberg","Nürnberg","Deutschland","🇩🇪","NUE","Frankens Flughafen, nah an der Altstadt.","",
  ['Kaiserburg', 'Christkindlesmarkt', 'Altstadt'],"Verschiedene Airlines, direkt oder mit Umstieg"),
 ("hamburg","Hamburg","Deutschland","🇩🇪","HAM","Größter Flughafen im Norden.","",
  ['Elbphilharmonie', 'Speicherstadt', 'Hafenrundfahrt'],"Verschiedene Airlines, direkt oder mit Umstieg"),
 ("berlin","Berlin","Deutschland","🇩🇪","BER","Hauptstadtflughafen mit Verbindungen in die ganze Welt.","",
  ['Brandenburger Tor', 'Museumsinsel', 'East Side Gallery'],"Verschiedene Airlines, direkt oder mit Umstieg"),
 ("hannover","Hannover","Deutschland","🇩🇪","HAJ","Flughafen für Niedersachsen.","",
  ['Herrenhäuser Gärten', 'Maschsee', 'Neues Rathaus'],"Verschiedene Airlines, direkt oder mit Umstieg"),
 ("karlsruhe","Karlsruhe/Baden-Baden","Deutschland","🇩🇪","FKB","Kleiner Flughafen am Rand des Schwarzwalds.","",
  ['Schloss Karlsruhe', 'Thermen in Baden-Baden', 'Schwarzwald'],"Verschiedene Airlines, direkt oder mit Umstieg"),
 ("bremen","Bremen","Deutschland","🇩🇪","BRE","Stadtnaher Flughafen im Nordwesten.","",
  ['Rathaus & Roland', 'Schnoor-Viertel', 'Bremer Stadtmusikanten'],"Verschiedene Airlines, direkt oder mit Umstieg"),
 ("leipzig","Leipzig","Deutschland","🇩🇪","LEJ","Flughafen für Sachsen und Mitteldeutschland.","",
  ['Völkerschlachtdenkmal', 'Zoo Leipzig', 'Altstadt & Passagen'],"Verschiedene Airlines, direkt oder mit Umstieg"),
]
LAENDER = ["Deutschland","Schweiz","Kosovo","Albanien","Nordmazedonien","Montenegro"]
assert set(LAENDER)=={z[2] for z in ZIELE}
BALKAN = [l for l in LAENDER if l not in ("Deutschland",)]

def opts(default):
    return "".join(f'<optgroup label="{l}">' + "".join(f'<option value="{z[4]}"{" selected" if z[4]==default else ""}>{z[1]} ({z[4]})</option>' for z in ZIELE if z[2]==l) + "</optgroup>" for l in LAENDER)

von_opts = opts("FRA")
nach_opts = opts("PRN")

def card(z,p=""):
    s,n,l,f,c,t,pr,_,_ = z
    return f"""<div class="card"><div class="img" style="background:#e8f1fb">{f}</div><div class="body">
<h3>{n}</h3><p>{l} · {t}</p>{f'<span class="price">Flüge {pr}</span>' if pr else ""}
<button class="btn" onclick="flugZiel('FRA','{c}')">Flüge ab Frankfurt*</button>
<a href="{p}reiseziele/{s}.html">Alle Abflughäfen & Tipps →</a></div></div>"""

sektionen = "".join(f'<h3 style="margin:28px 0 12px">{l}</h3><div class="grid">' + "".join(card(z) for z in ZIELE if z[2]==l) + "</div>" for l in BALKAN)
sektionen += '<h3 style="margin:28px 0 12px">Deutschland – auch als Ziel, z.B. für den Rückflug</h3><p>' + " · ".join(f'<a href="reiseziele/{z[0]}.html">{z[1]} ({z[4]})</a>' for z in ZIELE if z[2]=="Deutschland") + "</p>"

index = f"""<div class="hero"><div class="wrap">
<h1>Günstige Flüge zwischen Deutschland, der Schweiz und dem Balkan</h1>
<p>Nach Hause, zur Familie, in den Urlaub – und wieder zurück. Kosovo, Albanien, Nordmazedonien, Montenegro, Schweiz und Deutschland: Jeder Flughafen ist Abflug und Ziel. Wir vergleichen alle Airlines für dich.</p>
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
<div><h3>🏨 Hotels</h3><p>Unterkünfte in Tirana, Pristina, Ohrid, Zürich, Basel oder an der Albanischen Riviera.</p><a class="btn" data-partner="hotelLink" href="#">Hotels finden*</a></div>
<div><h3>🛡️ Reiseversicherung</h3><p>Wichtig: Kosovo, Albanien, Montenegro und Nordmazedonien sind nicht in der EU – die EU-Krankenversicherungskarte gilt dort nur eingeschränkt oder gar nicht.</p><a class="btn" data-partner="versicherungLink" href="#">Versicherung prüfen*</a></div>
<div><h3>🎟️ Ausflüge</h3><p>Touren nach Prizren, Kotor, zum Ohridsee oder zur Albanischen Riviera.</p><a class="btn" data-partner="aktivitaetenLink" href="#">Ausflüge buchen*</a></div>
</div></div></section>"""
(R/"index.html").write_text(page(f"{BRAND} – Günstige Flüge Deutschland, Schweiz, Kosovo, Albanien, Nordmazedonien & Montenegro","Günstige Flüge hin und zurück zwischen Deutschland, der Schweiz und Pristina, Tirana, Skopje, Ohrid und Podgorica im Vergleich.",index))

liste = "".join(f'<h2>{l}</h2><ul>' + "".join(f'<li><a href="{z[0]}.html">Flüge nach {z[1]} ({z[4]})</a></li>' for z in ZIELE if z[2]==l) + "</ul>" for l in LAENDER)
(R/"reiseziele/index.html").write_text(page(f"Alle Ziele – {BRAND}","Übersicht aller Flughäfen – jeder ist Abflug und Ziel.",f'<section><div class="wrap"><h1>Alle Flughäfen</h1>{liste}</div></section>',1))

for z in ZIELE:
    s,n,l,f,c,t,pr,tipps,air = z
    li = "".join(f"<li>{x}</li>" for x in tipps)
    btns = "".join(f'<p><b>{lv}:</b> ' + " ".join(f"""<button class="btn" style="margin:4px 0" onclick="flugZiel('{v[4]}','{c}')">ab {v[1]}</button>""" for v in ZIELE if v[2]==lv and v[4]!=c) + "</p>" for lv in (BALKAN+['Deutschland'] if l=='Deutschland' else LAENDER) if any(v[2]==lv and v[4]!=c for v in ZIELE))
    body = f"""<section><div class="wrap"><article>
<h1>{f} Günstige Flüge nach {n} ({c})</h1><p>{t} {('Flugpreise: '+pr+' (je nach Saison und Abflughafen).') if pr else 'Die Preise hängen von Saison und Abflughafen ab.'}</p>
<h2>Flüge nach {n} – wähle deinen Abflughafen</h2>{btns}
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
    (R/f"reiseziele/{s}.html").write_text(page(f"Günstige Flüge nach {n} ({c}) | {BRAND}",f"Billigflüge nach {n}, {l}: alle Abflughäfen, Airlines und Spartipps im Vergleich.",body,1))

legal = '<section><div class="wrap"><article><h1>{h}</h1>{b}</article></div></section>'
(R/"impressum.html").write_text(page("Impressum – BalkanWings","Impressum",legal.format(h="Impressum",b="""
<p><b>⚠️ PFLICHT: Vor Veröffentlichung ausfüllen (§ 5 DDG)!</b></p>
<p>Angaben gemäß § 5 DDG:<br>[Vor- und Nachname]<br>[Straße Hausnummer]<br>[PLZ Ort]<br>Deutschland</p>
<p>Kontakt: E-Mail: [z.B. info@balkanwings.com]</p>
<p>Umsatzsteuer: [Kleinunternehmer gem. § 19 UStG / USt-IdNr.]</p>
<p>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV: [Name, Anschrift]</p>
<p>BalkanWings ist ein Vergleichs- und Informationsportal und kein Reiseveranstalter. Verträge kommen ausschließlich mit den verlinkten Anbietern zustande.</p>""")))
(R/"datenschutz.html").write_text(page("Datenschutz – BalkanWings","Datenschutzerklärung",legal.format(h="Datenschutzerklärung",b="""
<p><b>⚠️ Vorlage – bitte mit einem Generator (z.B. e-recht24.de oder datenschutz-generator.de) vervollständigen.</b></p>
<h2>Verantwortlicher</h2><p>[Name, Anschrift, E-Mail wie im Impressum]</p>
<h2>Hosting</h2><p>Diese Website wird bei Netlify, Inc. gehostet. Beim Aufruf werden technisch notwendige Daten (z.B. IP-Adresse, Zeitpunkt) verarbeitet (Art. 6 Abs. 1 lit. f DSGVO).</p>
<h2>Affiliate-Links</h2><p>Klickst du auf einen Partnerlink, wirst du zum Anbieter (z.B. Aviasales/Travelpayouts) weitergeleitet. Dieser kann Cookies setzen, um die Vermittlung zuzuordnen. Es gelten die Datenschutzbestimmungen des Anbieters.</p>
<h2>Cookies</h2><p>Diese Seite selbst setzt keine Tracking-Cookies.</p>
<h2>Deine Rechte</h2><p>Auskunft, Berichtigung, Löschung, Einschränkung, Widerspruch, Datenübertragbarkeit sowie Beschwerde bei einer Aufsichtsbehörde.</p>""")))
# Domain, Canonical-Links, Sitemap, robots.txt
DOMAIN = "https://balkanwings.com"
seiten = []
for f in sorted(R.rglob("*.html")):
    rel = f.relative_to(R).as_posix().replace("index.html", "")
    html = f.read_text()
    if 'rel="canonical"' not in html:
        f.write_text(html.replace("<link rel=\"stylesheet\"", f'<link rel="canonical" href="{DOMAIN}/{rel}">\n<link rel="stylesheet"', 1))
    if rel not in ("impressum.html", "datenschutz.html"):
        seiten.append(rel)
urls = "".join(f"<url><loc>{DOMAIN}/{x}</loc></url>" for x in seiten)
(R/"sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
(R/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
print("ok", len(seiten), "Seiten in der Sitemap")
