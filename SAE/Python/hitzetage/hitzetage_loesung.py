def berechne_mittelwert(liste):
    summe = 0
    for element in liste:
        summe = summe + float(element)
    return str(summe / len(liste))
    
# "Test" der Funktion:
print(berechne_mittelwert([1, 2, 3]))
print(berechne_mittelwert(["12", "8", "10"]))
print(berechne_mittelwert(["1", "2"]))


with open("hitzetage.txt", "r") as datei:
    inhalt = datei.read()

with open("hitzetage_erweitert.txt", "w") as datei:
    datei.write(inhalt)
    
jahre = inhalt.split("\n")

for jahr in jahre[1::]:
    jahr = jahr.split(";")
    #jahr.pop()
    jahr.append(berechne_mittelwert(jahr[1:-1])) # Debuggen
# A) 4.
    ";".join(jahr)