def berechne_mittelwert(liste):
    summe = 0
    for element in liste:
        summe += float(element)
    return str(summe / len(liste))
# Test der Funktion:
#print(berechne_mittelwert([1,2,3]))

# A) 2.
with open("./hitzetage/hitzetage.txt", "r") as datei:
    inhalt = datei.read()
    inhalt.replace(" ", "") # Leerzeichen weg

with open("./hitzetage/hitzetage_erweitert.txt", "w") as datei:
    datei.write(inhalt)

# A) 3.
jahre = inhalt.split("\n")
jahre_strings = []

for jahr in jahre[1::]:
    jahr = jahr.split(";")
    #jahr.pop()
    berechne_mittelwert(jahr[1:-1])
    jahr.append(berechne_mittelwert(jahr[1:-1]))
# A) 4.
    jahre_strings.append(";".join(jahr))
# A) 5.
jahre[0] = jahre[0] + "Mittel" + "\n".join(jahre_strings)

print(jahre)