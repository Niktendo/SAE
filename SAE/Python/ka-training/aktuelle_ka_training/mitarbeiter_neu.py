# Aufgabe 1
'''
Schreibe eine Funktion die einen Dateinamen als Parameter
erhält und den Dateiinhalt als zeilenweise Liste zurückgibt.
Bevor die Liste erstellt wird, soll unnötiger Whitespace
entfernt werden.

Rufe die Funktion mit dem Parameter "mitarbeiter.csv" auf.
'''

def datei_lesen(dateiname):
    with open(dateiname, "r") as datei:
        inhalt = datei.read().strip().split("\n")
    return inhalt

# Aufgabe 2
'''
Schreibe die Funktion extrahiere_mitarbeiter(), die die
Mitarbeiterliste als Parameter erhält und eine Zeichenkette 
zurückgibt, die die Namen durch Komma und Leerzeichen 
getrennt enthält.
'''

def extrahiere_mitarbeiter(inhalt):
    neue_liste = []
    for mitarbeiter in inhalt[1::]:
        mitarbeiter_liste = mitarbeiter.split(";")
        neue_liste.append(mitarbeiter_liste[1])
    megastring = ", ".join(neue_liste)
    return megastring

# Aufgabe 3
'''
Schreibe die Funktion berechne_durchschnittsgehalt(), die das
durchschnittliche Gehalt aller Mitarbeiter einer bestimmten 
Abteilung berechnet. Die Abteilung wird als Parameter übergeben.

Beispielaufruf:
    berechne_durchschnittsgehalt(mitarbeiter, "IT")
Beispielausgabe:
    5100.0
'''

def berechne_durchschnittsgehalt(inhalt, abteilung):
    gehalt = 0
    i = 0
    for mitarbeiter in inhalt[1::]:
        mitarbeiter_liste = mitarbeiter.split(";")
        if mitarbeiter_liste[2] == abteilung:
            gehalt = gehalt + float(mitarbeiter_liste[3])
            i = i + 1
    if i == 0:
        return 0
    else:
        durchschnitt_gehalt = gehalt / i
        return str(durchschnitt_gehalt)

# Aufgabe 4
'''
Schreibe die Funktion erhoehe_gehalt_teilzeit(), die das Gehalt 
aller Mitarbeiter die in Teilzeit arbeiten um 10% erhöht und 
eine aktualisierte Liste zurückliefert.
'''

def erhoehe_gehalt_teilzeit(inhalt):
    neue_liste = []
    for mitarbeiter in inhalt:
        mitarbeiter_liste = mitarbeiter.split(";")
        if mitarbeiter_liste[5].strip().lower() == "ja":
            mitarbeiter_liste[3] = str(float(mitarbeiter_liste[3]) + float(mitarbeiter_liste[3]) * 0.1)
        person_string = ";".join(mitarbeiter_liste)
        neue_liste.append(person_string)
    megastring = "\n".join(neue_liste)
    return megastring

# Aufgabe 5
'''
Erstelle einen String aus den Ergebnissen aller übrigen
Funktionen und schreibe ihn in die Datei gehaltsbericht.txt
'''

inhalt = datei_lesen("./aktuelle_ka_training/mitarbeiter.csv")
bericht = "Mitarbeiterliste:\n" + extrahiere_mitarbeiter(inhalt)
bericht = bericht + "\nDurchschnittsgehalt:\n" + berechne_durchschnittsgehalt(inhalt, "IT")
bericht = bericht + "\nNeues Gehalt:\n" + erhoehe_gehalt_teilzeit(inhalt)

with open("./aktuelle_ka_training/gehaltsbericht.txt", "w") as datei:
    datei.write(bericht)