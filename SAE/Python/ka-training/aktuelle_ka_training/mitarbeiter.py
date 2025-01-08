# Aufgabe 1
'''
Schreibe eine Funktion die einen Dateinamen als Parameter
erhält und den Dateiinhalt als zeilenweise Liste zurückgibt.
Bevor die Liste erstellt wird, soll unnötiger Whitespace
entfernt werden.

Rufe die Funktion mit dem Parameter "mitarbeiter.csv" auf.
'''

def open_file(filename):
    with open(filename, "r") as file:
        content = file.read().strip().split("\n")
    
    return content
#    print(content)
#    extrahiere_mitarbeiter(content)
#    berechne_durchschnittsgehalt(content, "IT")
#    erhoehe_gehalt_teilzeit(content)

# Aufgabe 2
'''
Schreibe die Funktion extrahiere_mitarbeiter(), die die
Mitarbeiterliste als Parameter erhält und eine Zeichenkette 
zurückgibt, die die Namen durch Komma und Leerzeichen 
getrennt enthält.
'''

def extrahiere_mitarbeiter(content):
    neue_liste = []
    content.pop(0)
    for person in content:
        person_liste = person.split(";")
        neue_liste.append(person_liste[1])
    megastring = ", ".join(neue_liste)

    return megastring
    #print(megastring)

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

def berechne_durchschnittsgehalt(content, abteilung):
    content.pop(0)
    gehalt = 0
    i = 0
    for person in content:
        person_liste = person.split(";")
        if person_liste[2] == abteilung:
            gehalt = gehalt + int(person_liste[3])
            i = i + 1
    durchschnitt_gehalt = str(gehalt / i)

    return durchschnitt_gehalt
    #print(durchschnitt_gehalt)


# Aufgabe 4
'''
Schreibe die Funktion erhoehe_gehalt_teilzeit(), die das Gehalt 
aller Mitarbeiter die in Teilzeit arbeiten um 10% erhöht und 
eine aktualisierte Liste zurückliefert.
'''

def erhoehe_gehalt_teilzeit(content):
    neue_liste = []
    content.pop(0)
    for person in content:
        person_liste = person.split(";")
        if person_liste[-1] == "Ja":
            gehalt = int(person_liste[3]) + int(person_liste[3]) * 0.1
            person_liste[3] = str(gehalt)
        person_string = ";".join(person_liste)
        neue_liste.append(person_string)
    megastring = "\n".join(neue_liste)
    return megastring
    #print(megastring)

# Aufgabe 5
'''
Erstelle einen String aus den Ergebnissen aller übrigen
Funktionen und schreibe ihn in die Datei gehaltsbericht.txt
'''
content = open_file("./aktuelle_ka_training/mitarbeiter.csv")
bericht = "Mitarbeiterliste: " + extrahiere_mitarbeiter(content)
bericht = bericht + "\nDurchschnittsgehalt IT: " + berechne_durchschnittsgehalt(content, "IT")
bericht = bericht + "\nErhöhtes Teilzeitgehalt:\n" + erhoehe_gehalt_teilzeit(content)

with open("./aktuelle_ka_training/bericht.txt", "w") as datei:
    datei.write(bericht)