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

def personnelNumberFirst(datensatz, trenner): # datensatz ist Liste
    daten_neu = []
    for person in datensatz:                  # person in datensatz wird String
        person_liste = person.split("|")      # person wird aufgeteilt in Liste
        nummer = person_liste.pop(trenner)
        person_liste.insert(0, nummer)
        person_string = "|".join(person_liste)# person wird String
        daten_neu.append(person_string)       # person wird liste
    return daten_neu

print(personnelNumberFirst(schneider, 3))