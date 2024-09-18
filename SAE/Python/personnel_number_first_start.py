wirth = [
    "Mueller|Josef|FR_1112|Freiburg",
    "Maier|Fritz|ST_1114|Vaihingen",
    "Heinze|Maria|ST_5525|Bad Cannstatt",
    "Herrman|Georg|FR_2536|Merzhausen"
    ]

schneider = [
    "Schneider|Wolfgang|Heidelberg|HE_20011",
    "Bartels|Martina|Sandhausen|HE_15436",
    "Beck|Hans|Neckarsteinach|HE_5436"
    ]

def personnelNumberFirst(daten, index_persnr):
    daten_neu = []

    for person in daten:
        person_liste = person.split("|")
        personalnummer = person_liste.pop(index_persnr)
        person_liste.insert(0, personalnummer)
        person_string = "|".join(person_liste)
        daten_neu.append(person_string)

    return daten_neu

print(personnelNumberFirst(wirth, 2))

'''
index = 2

#test = "".join(wirth)
#print(test)
for eintrag in wirth:
    liste = eintrag.split("|")
    liste.insert(0, liste[2])
    liste.pop(liste[2])

print(liste)

'''