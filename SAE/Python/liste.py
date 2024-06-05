# liste = [1, 2, 3]
# liste.append(4)
# print(liste)

#Aufgabe 1: Erstelle eine Liste mit vier Klassenmitgliedern, nenne sie gruppe_a

gruppe_a = ["Niklas", "Louis", "Hannes", "Ozan"]

#Aufgabe 2: Füge ein neues Element an der vierten Stelle hinzu

gruppe_a.insert(3, "Anonym")

#Aufgabe 3: Bilde gruppe_b mit zwei bis drei Klassenmitgliedern

gruppe_b = ["Koch", "Thiersch", "Mundt"]

#Aufgabe 4: Füge Gruppe B hinten an Gruppe A

gruppe_a.extend(gruppe_b)

#Aufgabe 5: Sortiere Gruppe A

gruppe_a.sort()

#Aufgabe 6: Gib alle Klassenmitglieder hintereinander aus, ohne die Grupep zu verändern

for schueler in gruppe_a:
    print(schueler)
    
#Aufgabe 7: Schreibe ein Programm, dass das jeweils letzte Element in der Liste löscht und ausgibt, bis die Liste leer ist

while len(gruppe_a) > 0:
    print(gruppe_a.pop())

#Aufgabe 8: Die Reihenfolge der Liste ist zufällig. Füge Anna vor Tom ein.
gruppe_c = ["Jan", "Tim", "David", "Jim", "Max", "Kai", "Eva", "Ute", "Tom"]
gruppe_c.insert(gruppe_c.index("Tom"), "Ana")
gruppe_c.pop(gruppe_c.index("David"))
gruppe_c.insert(gruppe_c.index("Ute"), "David")










