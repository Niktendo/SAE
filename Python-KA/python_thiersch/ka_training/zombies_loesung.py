# Day Z:

# Grundalgorithmus, der ordentlich reinfrisst, aber
# zu viele Zombies und negative Anzahl Reutlinger produziert.

def tage_bis_zombifiziert(menschen, zombies, inzidenz):
    tage = 1
    while menschen > 0:
        print(zombies, menschen)
        gebissene = zombies * inzidenz
        menschen = menschen - gebissene
        zombies = zombies + gebissene
        tage = tage + 1
    print(zombies, menschen)
    return tage

#print("Tage", tage_bis_zombifiziert(116033, 1, 1.5))

# Es gibt Möglichkeiten, den Endstand zu fixen.

# Beste Möglichkeit: if und else einbauen
# damit nur Zombies hinzugefügt werden, wenn es auch
# entsprechende Reutlinger gibt und die Anzahl
# Reutlinger nicht negativ wird

def tage_bis_alle_zombies(menschen, zombies, bissquote):
    tage = 1
    while (menschen > 0):
        print ("Zombies:", zombies, "\t\t\t\tMenschen:", menschen)
        gebissene = zombies * bissquote
        if menschen - gebissene >= 0:
            menschen = menschen - gebissene
            zombies = zombies + gebissene
        else:
            zombies = zombies + menschen
            menschen = 0        
        tage = tage + 1
    print("Endstand")
    print ("Zombies:", zombies, "\t\t\t\tMenschen:", menschen)
    return tage
tage_bis_alle_zombies(116033, 1, 1.5)

# 2. Eine schlechte Möglichkeit wäre, bei der Ausgabe
# des Endstands zu lügen, also einfach 0 auszugeben.
# Die Aufgabe erfordert jedoch, dass die Anzahl nie negativ
# sein darf.