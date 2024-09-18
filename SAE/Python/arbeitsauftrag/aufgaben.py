# Aufgabe 1: Nutze die Listenmethoden aus help(list)
def aufgabe1():
    # Erstelle eine Liste namens obst, die die Elemente "Apfel", "Banane", "Pflaume" enthält.
    obst = ["Apfel", "Banane", "Pflaume"]
    print(obst)
    # Füge die Elemente der Liste beeren = ["Stachelbeere", "Himbeere", "Heidelbeere"] ans Ende von obst.
    beeren = ["Stachelbeere", "Himbeere", "Heidelbeere"]
    obst.extend(beeren)
    print(obst)
    # Füge am Ende der Liste das Element "Mango" hinzu.
    obst.append("Mango")
    print(obst)
    # Füge zwischen Banane und Pflaume das Element "Kirsche" ein.
    obst.insert((obst.index("Pflaume")), "Kirsche")
    print(obst)
    # Ändere das zweite Element von "Banane" in "Birne".
    obst[1] = "Birne"
    print(obst)
    # Entferne das erste Element aus der Liste.
    obst.pop(1)
    print(obst)
    # Nutze pop() um das letzte Element zu entfernen und auszugeben.
    print(obst.pop())
    # Gib den Index des Elements "Pflaume" auf der Konsole aus.
    print(obst.index("Pflaume"))
    # Gib das größte Element auf der Konsole aus.
    print(obst[len(obst)-1])
    # Gib den Index des größten Elements auf der Konsole aus.
    print(obst.index(obst[len(obst)-1]))
    # Wie viele Stellen ist das größte Element vom Kleinsten entfernt? Gib hierzu die Differenz der
    # Indizes des größten und des kleinsten Elements als positive Zahl aus.
    max_index = obst.index(max(obst))
    min_index = obst.index(min(obst))
    diff = max_index - min_index
    print(abs(diff))
    # Gib die Liste auf der Konsole aus.
    print(obst)
    # Sortiere die Liste alphabetisch aufsteigend.
    obst.sort()
    print(obst)
    # Gib die einzelnen Elemente der Liste zeiilenweise auf der Konsole aus (for-each-Schleife)
    for frucht in obst:
        print(frucht)

#Aufgabe 2: Slicing
def aufgabe2():
    # Erstelle eine Liste zahlen die die Zahlen von 1 bis 100 enthält. Nutze hierzu for i in range()
    # und füge jedes einzelne Element hinten an deine Liste.
    # liste[start:stop:step]
    liste = []
    for i in range (1, 101):
        liste.append(i)
    # Gib die Anzahl der Elemente aus.
    print(len(liste))
    # Gib die gesamte Liste aus.
    print(liste[0:100:1])
    # Gib die Liste bis zum vorletzten Element aus.
    print(liste[:-1:])
    # Gib die Liste bis zum fünften Element von Hinten aus.
    print(liste[:-5:])
    # Gib alle Elemente zwischen den Indizes 25 und 35 (inklusive) aus.
    print(liste[25:36:])
    # Gib jedes zweite Element aus.
    print(liste[::2])
    # Gib jedes fünfte Element bis zum Index 80 (exklusive) aus.
    print(liste[:80:5])
    # Gib die Liste rückwärts aus.
    print(liste[::-1])

# Aufgabe 3: Listen durchlaufen
def aufgabe3():
    # Erstelle die Liste messwerte = [22.86, 20.39, 23.76, 21.34, 24.32]
    messwerte = [22.86, 20.39, 23.76, 21.34, 24.32]
    # Durchlaufe die Liste ein Mal und ermittle dabei minimum, maximum und summe.
    # Nutze dabei NICHT die Funktionen min(), max(), sum().
    # Gib Minimum, Maximum, Summe und Durchschnitt aus.
    minimum = messwerte[0]
    maximum = messwerte[0]
    summe = 0

    for wert in messwerte:
        summe = summe + wert

        if wert < minimum:
            minimum = wert
        if wert > maximum:
            maximum = wert

    durchschnitt = summe / len(messwerte)

    print(minimum, maximum, summe, durchschnitt)

# Aufgabe 4: Listen und Strings
def aufgabe4():
    # Zerschneide den String "Schneider;Fischer;Seemann;Schmied;Müller" in eine Liste berufe.
    berufe = "Schneider;Fischer;Seemann;Schmied;Müller".split(";")
    # Sortiere die Liste berufe.
    berufe.sort
    # Füge die Liste zu einem String mit dem Trennzeichen | zusammen.
    ergebnis = "|".join(berufe)
    print(ergebnis)

# Aufgabe 5: Verschachtelte Listen
def aufgabe5():
    # Gegeben ist die verschachtelte Liste matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
    # Schreibe eine Funktion, die die Summe aller Zahlen in der Matrix berechnet. Hierzu bekommt sie
    # die Matrix als Parameter und liefert die Summe zurück.
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    summe = 0

    for liste in matrix:
        for element in liste:
            summe = summe + element

    #for liste in matrix:
    #    summe = summe + sum(liste)

    print(summe)

aufgabe5()