with open("./bundeslaender/bundeslaender.csv") as datei:
    inhalt = datei.read()

daten_liste = inhalt.split("\n")
erste_zeile = daten_liste.pop(0)

coloum = erste_zeile.split(",")
coloum.append("Einwohner je qkm")
erste_zeile_neu = ",".join(coloum)

neue_liste = []

for eintrag in daten_liste:
    zeile = eintrag.split(",")
    rechnung = int(zeile[2]) / int(zeile[1])
    zeile.append(str(rechnung))
    string_neu = ",".join(zeile)
    neue_liste.append(string_neu)

neue_liste.insert(0, erste_zeile_neu)
inhalt_neu = "\n".join(neue_liste)

with open("./bundeslaender/bundeslaender_erweitert.csv", "w") as datei:
    datei.write(inhalt_neu)