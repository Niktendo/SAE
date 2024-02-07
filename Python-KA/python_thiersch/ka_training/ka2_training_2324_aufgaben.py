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

def jahre_bis_ausgerottet(anzahl_robben):
    i = 0

    while anzahl_robben >= 2:
        anzahl_robben = anzahl_robben * 2/3
        i += 1
    return i

#print("Es dauert", jahre_bis_ausgerottet(450), "Jahre")




#2 b)
# Schreibe die Funktion so allgemein, dass sie auch für den Achalmfuchs (Population von 12, sinkt jährlich auf die Hälfte, wird bis
# zu drei Individuen gejagt) angewendet werden kann.


def jahre_bis_ausrottung(population, sink_rate, grenze):
    i = 0

    while population >= grenze / sink_rate:
        population *= sink_rate
        i += 1
    return i

#print("Es dauert", jahre_bis_ausrottung(12, 0.5, 3), "Jahre.")





#3
# Jede Erzieherin in einer bayrischen Kita betreut 4 Kinder (Betreuungschlüssel = 4). Im Ort Kuhflading gibt es derzeit 40 Kinder und entsprechend 10 Erzieherinnen.
# Jedes Jahr werden mehr Kinder geboren. Die Wachstumsrate der Bevölkerung durch Geburten liegt voraussichtlich noch sehr lange stabil bei 5% (* 0.05).
# Schreibe eine Funktion die berechnet, in wie vielen Jahren sich die Anzahl der Erzieherinnen verdoppelt hat.
# Übergabeparameter: Anzahl Kinder, Wachstumsrate, Betreuungschluessel
# Beispiel: Für den Ort Facking mit (Kinder: 100, Wachstumsrate = 0.10, Betreuungschlüssel: 4) wäre das Ergebnis 8 Jahre.


def erzieher_verdoppelt(kinder, wachstumsrate, betreuungsschluessel):
    i = 0

    anzahl_erzieher = kinder / betreuungsschluessel
    doppelte_anzahl_erzieher = anzahl_erzieher * 2
    while anzahl_erzieher < doppelte_anzahl_erzieher:
        kinder += kinder * wachstumsrate
        anzahl_erzieher = kinder / betreuungsschluessel
        i += 1
        #print(anzahl_erzieher)
    return i

#print("Es dauert", erzieher_verdoppelt(40, 0.05, 4), "Jahre.")




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


def klassifiziere_geschwindigkeit(geschwindigkeit):
    out = "Du fährst sehr langsam."

    if 100 <= geschwindigkeit <= 130:
        out = "Du fährst ideal."
    elif geschwindigkeit > 130:
        out = "Du fährst zu schnell!"
    return out

#print(klassifiziere_geschwindigkeit(131))

# 4 b)
# Schreibe eine weitere Funktion, die Distanz, Geschwindigkeit und Pausenzeit übergeben bekommt
# und die Reisedauer in Stunden zurückgibt. Diese wird wie folgt berechnet:
# reisedauer = distanz/geschwindigkeit + pausenzeit/60

def reisedauer_in_stunden(distanz, geschwindigkeit, pausenzeit):
    reisedauer = distanz / geschwindigkeit + pausenzeit / 60
    return reisedauer


# 4 c)
# Schreibe eine Funktion, Distanz, Geschwindigkeit und Pausenzeit über die Tastatur
# einliest und die Funktionen aus 4 a) und 4 b) benutzt um sowohl die Klassifikation auf der Konsole auszugeben
# als auch die Reisedauer zu berechnen.

def reisemonitor():
    distanz = int(input("Gib die Distanz (in km) an: "))
    geschwindigkeit = int(input("Gib die Geschwindigkeit (in km/h) an: "))
    pausenzeit = int(input("Gib die Pausenzeit (in Minuten) an:"))
    
    print(klassifiziere_geschwindigkeit(geschwindigkeit))
    print("Deine Reisedauer beträgt", reisedauer_in_stunden(distanz, geschwindigkeit, pausenzeit), "Stunden.")

reisemonitor()