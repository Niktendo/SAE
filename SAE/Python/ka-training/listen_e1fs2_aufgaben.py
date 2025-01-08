import random
#liste = []

#liste = [1, 2, 2, 2, 3]
# liste = ["tim", "tanja", "thomas"]
# 
# i = 0
# while i < len(liste):
#     print(liste[i])
#     i = i + 1

# for i = 0; i < len(liste); i+= 1:
#     pass

#     
# for element in liste[::2]:
#     print(element)
#     #print(element)
    
# for buchstabe in "thiersch"[2::1]:
#      print(buchstabe)
    
# for zahl in {1, 2, 1, 2, 3}:
#     print(zahl)
    
    
# Entferne Redundanz aus Liste:
# liste = [1, 1, 1, 2, 2, 1, 1, 3, 5, 12, 100, 100, 200]
# 
# print(list(set(liste)))


# Nutze help(list) um folgende Aufgaben
# zu lösen:

# 1. Erstelle eine Liste mit vier
# Klassenmitgliedern, nenne sie gruppe_a

gruppe_a = ["Niklas", "Ozan", "Valentin", "Hannes"]

# 2. Füge ein neues Element an der
# vierten Stelle dazu

gruppe_a.insert(3, "Jeanluca")

# 3. Bilde gruppe_b mit zwei bis drei
# Klassenmitgliedern.

gruppe_b = "Thiersch", "Koch", "Mundt"

# 4. Füge Gruppe B hinten an Gruppe A.

gruppe_a.extend(gruppe_b)

# 5. Sortiere Gruppe A.

gruppe_a.sort()

# 6. Gib alle Klassenmitglieder hintereinander aus,
# ohne die Gruppe zu verändern.

#for schueler in gruppe_a:
#    print(schueler)

# 7. Schreibe ein Programm, das das jeweils letzte
# Element der Liste löscht und ausgibt, bis die Liste
# leer ist.

#while len(gruppe_a) > 0:
#    print(gruppe_a.pop())

# 8.
gruppe_c = ["Jan", "Tim", "David", "Jim", "Max", "Kai", "Eva", "Ute", "Tom"]
# Die Reihenfolge der Liste ist
# zufällig. Füge Ana vor Tom ein.
# Der Index von Ana oder Tom darf nicht hartkodiert
# sein.

gruppe_c.insert(gruppe_c.index("Tom"), "Ana")

# 9.


# Hole David von seinem jetzigen Platz und setze ihn vor Ute.

gruppe_c.remove("David")
gruppe_c.insert(gruppe_c.index("Ute"), "David")

print(gruppe_c)

# todo: fixe obiges problem


# Aufgabe:
# Erkundige dich über die Listenmethode split()
# Erstelle eine Liste aus "Thiersch;Mundt;Koch;Hemmasi"