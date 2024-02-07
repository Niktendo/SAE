# 1. Forme sämtliche while-Übungen in Funktionen um.

# 2.
# Reutlingen ist berühmt für seine Wintermode, gesunden Bürger und exkuisiten Speisen.
# Die wertvollen Felle, Omega-3-Fette und Filets müssen aber erst mit viel Mühe aus den Robben in den Echazauen herausgeholt werden.
# Reutlinger Geschäftsleute scheuen diese Mühen nicht und jagen jedes Jahr genug Graue Echazrobben, damit ihre Kunden glücklich und zufrieden sind.
# Die Population der Grauen Echazrobbe sinkt jedes Jahr auf drei Viertel des Vorjahresbestands. Derzeit gibt es 740 Individuen.
# Da Reutlingen auch für seine Nachhaltigkeit berühmt ist, möchte es die Robbe erhalten. Du erhältst folgenden Auftrag der Robbenjägerei-Innung:
# 2 a)
# Schreibe eine Funktion, die die Anzahl der Individuen als Parameter bekommt und die Anzahl der Jahre berechnet, bis noch zwei Echazrobben übrig sind.des
# Vorjahres).
# 

def jahre_bis_schwellwert(anzahl_robben):
    jahre = 0
    while anzahl_robben >= 3: # robben >= 3, weil 2/3 von 3 den Schwellwert von 2 ergeben! Bei robben >= 2 würde der Schwellwert von 2 unterschritten
        anzahl_robben = (anzahl_robben / 3) * 2
        jahre = jahre + 1
        # print(anzahl_robben, jahre)
    return jahre

#print(jahre_bis_schwellwert(450))

#2 b)
# Schreibe die Funktion so allgemein, dass sie auch für den Achalmfuchs (Population von 12, sinkt jährlich auf die Hälfte, wird bis
# zu drei Individuen gejagt) angewendet werden kann.

def jahre_bis_schwellwert(population, rate, schwellwert):
    jahre = 0
    while population >= schwellwert / rate: # schwellwert / rate liefert den letzten erlaubten Schritt. Z.B. Robben: 2 / 0.6666 = 3.0003, Füchse: 3 / 0.5 = 6
        population = population * rate
        jahre = jahre + 1
        # print(population, jahre)
    return jahre

#print(jahre_bis_schwellwert(12, 0.5, 3))


#3
# Jede Erzieherin in einer bayrischen Kita betreut 4 Kinder (Betreuungschlüssel = 4). Im Ort Kuhflading gibt es derzeit 40 Kinder und entsprechend 10 Erzieherinnen.
# Jedes Jahr werden mehr Kinder geboren. Die Wachstumsrate der Bevölkerung durch Geburten liegt voraussichtlich noch sehr lange stabil bei 5% (* 0.05).
# Schreibe eine Funktion die berechnet, in wie vielen Jahren sich die Anzahl der Erzieherinnen verdoppelt hat.
# Übergabeparameter: Anzahl Kinder, Wachstumsrate, Betreuungschluessel
# Beispiel: Für den Ort Facking mit (Kinder: 100, Wachstumsrate = 0.10, Betreuungschlüssel: 4) wäre das Ergebnis 8 Jahre.

def jahre_bis_verdoppelt(anzahl_kinder, wachstumsrate, betreuungsschluessel):
    anzahl_erzieherinnen = anzahl_kinder / betreuungsschluessel
    doppelte_anzahl_erzieherinnen = anzahl_erzieherinnen * 2
    jahre = 0
    while anzahl_erzieherinnen < doppelte_anzahl_erzieherinnen:
        anzahl_kinder = anzahl_kinder + anzahl_kinder * wachstumsrate
        anzahl_erzieherinnen = anzahl_kinder / betreuungsschluessel
        jahre += 1
        print(anzahl_erzieherinnen, jahre)
    return jahre

#print(jahre_bis_verdoppelt(40, 0.05, 4))

#4
# Du entwickelst eine App zur Reiseplanung.

# 4 a)
# Schreibe eine Funktion, die eine Geschwindigkeitsangabe in km/h nach folgenden Kriterien klassifiziert und die Klassifikation als
# String zurückliefert.
# Unter 100 km/h:
#     „Du fährst sehr langsam.“
# 100 bis 130 km/h:
#     „Du fährst mit der idealen Geschwindigkeit.“
# Über 130 km/h:
#     „Du fährst zu schnell!“

# 4 b)
# Schreibe eine weitere Funktion, die Distanz, Geschwindigkeit und Pausenzeit übergeben bekommt
# und die Reisedauer in Stunden zurückgibt. Diese wird wie folgt berechnet:
# reisedauer = distanz/geschwindigkeit + pausenzeit/60

# 4 c)
# Schreibe eine Funktion, Distanz, Geschwindigkeit und Pausenzeit über die Tastatur
# einliest und die Funktionen aus 4 a) und 4 b) benutzt um sowohl die Klassifikation
# als auch die Reisedauer auf der Konsole auszugeben.

#4 a)
def klassifiziere_geschwindigkeit(geschwindigkeit):
    klassifikation = "" # In diesem Fall unnötig
    if geschwindigkeit < 100:
        klassifikation = "Du fährst sehr langsam."
    elif geschwindigkeit > 130:
        klassifikation = "Du fährst zu schnell!"
    else:
        klassifikation = "Du fährst mit der idealen Geschwindigkeit"
    return klassifikation

#4 b)
def reisedauer(distanz, geschwindigkeit, pausenzeit):
    return distanz/geschwindigkeit + pausenzeit/60

#4 c)
def plane_reise():
    distanz = int(input("Gib die Distanz (in km) an: "))
    geschwindigkeit = int(input("Gib die Geschwindigkeit (in km/h) an: "))
    pausenzeit = int(input("Gib die Pausenzeit (in Minuten) an:"))
    
    print(klassifiziere_geschwindigkeit(geschwindigkeit))
    print("Die Reisedauer beträgt", reisedauer(distanz, geschwindigkeit, pausenzeit), "Stunden")
    
plane_reise()
