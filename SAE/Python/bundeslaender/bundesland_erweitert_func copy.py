def bundeslaender(file, id1, id2, id3, id4):
    with open(file) as datei:
        inhalt = datei.read()

    if id1 == "1":

        daten_liste = inhalt.split("\n")
        erste_zeile = daten_liste.pop(0)

        coloum = erste_zeile.split(",")
        coloum.append("Einwohner je qkm")
        erste_zeile_neu = ",".join(coloum)

        neue_liste = []
        rechnung = 0

        for eintrag in daten_liste:
            zeile = eintrag.split(",")
            rechnung = int(zeile[2]) / int(zeile[1])
            zeile.append(str(rechnung))
            string_neu = ",".join(zeile)
            neue_liste.append(string_neu)

        neue_liste.insert(0, erste_zeile_neu)
        inhalt = "\n".join(neue_liste)

    if id2 == "1":

        daten_liste = inhalt.split("\n")
        erste_zeile = daten_liste.pop(0)

        coloum = erste_zeile.split(",")
        coloum.append("Anteil an Gesamtfläche")
        erste_zeile_neu = ",".join(coloum)

        neue_liste = []
        rechnung = 0
        ges_flaeche = 0

        for eintrag in daten_liste:
            zeile = eintrag.split(",")
            ges_flaeche += int(zeile[1])

        for eintrag in daten_liste:
            zeile = eintrag.split(",")
            flaeche = int(zeile[1])
            rechnung = (flaeche / ges_flaeche) * 100
            zeile.append(str(rechnung) + "%")
            string_neu = ",".join(zeile)
            neue_liste.append(string_neu)
        

        neue_liste.insert(0, erste_zeile_neu)
        inhalt = "\n".join(neue_liste)

    if id3 == "1":

        daten_liste = inhalt.split("\n")
        erste_zeile = daten_liste.pop(0)

        coloum = erste_zeile.split(",")
        coloum.append("Anteil an Gesamtbevölkerung")
        erste_zeile_neu = ",".join(coloum)

        neue_liste = []
        rechnung = 0
        ges_einwohner = 0

        for eintrag in daten_liste:
            zeile = eintrag.split(",")
            ges_einwohner += int(zeile[2])

        for eintrag in daten_liste:
            zeile = eintrag.split(",")
            einwohner = int(zeile[2])
            rechnung = (einwohner / ges_einwohner) * 100
            zeile.append(str(rechnung) + "%")
            string_neu = ",".join(zeile)
            neue_liste.append(string_neu)
        

        neue_liste.insert(0, erste_zeile_neu)
        inhalt = "\n".join(neue_liste)    

    if id4 == "1":

        daten_liste = inhalt.split("\n")
        erste_zeile = daten_liste.pop(0)

        coloum = erste_zeile.split(",")
        coloum.append("Bevölkerungsdichte")
        erste_zeile_neu = ",".join(coloum)

        neue_liste = []
        rechnung = 0
        i = 0

        for eintrag in daten_liste:
            zeile = eintrag.split(",")
            rechnung += float(zeile[3])
            i += 1
        bevoelkerungsdichte_brd = rechnung / i

        for eintrag in daten_liste:
            zeile = eintrag.split(",")
            if float(zeile[3]) < bevoelkerungsdichte_brd:
                zeile.append("gering")
            else:
                zeile.append("hoch")
            string_neu = ",".join(zeile)
            neue_liste.append(string_neu)

        neue_liste.insert(0, erste_zeile_neu)
        inhalt = "\n".join(neue_liste)


    with open("./bundeslaender/bundeslaender_erweitert.csv", "w") as datei:
        datei.write(inhalt)


bundeslaender("./bundeslaender/bundeslaender.csv", "1", "1", "1", "1")