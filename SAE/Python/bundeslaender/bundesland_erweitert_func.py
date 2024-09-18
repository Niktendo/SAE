def bundeslaender(file, id1, id2, id3, id4):
    with open(file) as datei:
        inhalt = datei.read()

    def einwohner_je_qkm(inhalt):

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
        return inhalt

    def anteil_an_gesamtflaeche(einwohner_je_qkm):

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

        return neue_liste
        return inhalt

    def anteil_an_gesamtbevoelkerung(inhalt, neue_liste):

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

        return neue_liste
        return inhalt

    def bevoelkerungsdichte(inhalt, neue_liste):

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

        return neue_liste
        return inhalt

    if id1 == "1":
        #print(einwohner_je_qkm(inhalt))
        einwohner_je_qkm(inhalt)
    if id2 == "1":
        print(anteil_an_gesamtflaeche(einwohner_je_qkm(inhalt)))
    if id3 == "1":
        anteil_an_gesamtbevoelkerung(inhalt, neue_liste)
    if id4 == "1":
        bevoelkerungsdichte(inhalt, neue_liste)


    with open("./bundeslaender/bundeslaender_erweitert.csv", "w") as datei:
        datei.write(inhalt)


bundeslaender("./bundeslaender/bundeslaender.csv", "1", "1", "0", "0")