# liste = [1, 2, 3]
# liste.append(4)
# print(liste)

def aufgabe1():
    #Aufgabe 1: Erstelle eine Liste mit vier Klassenmitgliedern, nenne sie gruppe_a

    gruppe_a = ["Niklas", "Louis", "Hannes", "Ozan"]

def aufgabe2():
    #Aufgabe 2: Füge ein neues Element an der vierten Stelle hinzu
    gruppe_a = ["Niklas", "Louis", "Hannes", "Ozan"]
    gruppe_a.insert(3, "Anonym")

def aufgabe3():
    #Aufgabe 3: Bilde gruppe_b mit zwei bis drei Klassenmitgliedern
    
    gruppe_b = ["Koch", "Thiersch", "Mundt"]

def aufgabe4():
    #Aufgabe 4: Füge Gruppe B hinten an Gruppe A
    gruppe_a = ["Niklas", "Louis", "Hannes", "Ozan"]
    gruppe_b = ["Koch", "Thiersch", "Mundt"]
    gruppe_a.extend(gruppe_b)

def aufgabe5():
    #Aufgabe 5: Sortiere Gruppe A
    gruppe_a = ["Niklas", "Louis", "Hannes", "Ozan"]
    gruppe_a.sort()

def aufgabe6():
    #Aufgabe 6: Gib alle Klassenmitglieder hintereinander aus, ohne die Grupep zu verändern
    gruppe_a = ["Niklas", "Louis", "Hannes", "Ozan"]
    for schueler in gruppe_a:
        print(schueler)

def aufgabe7():    
    #Aufgabe 7: Schreibe ein Programm, dass das jeweils letzte Element in der Liste löscht und ausgibt, bis die Liste leer ist
    gruppe_a = ["Niklas", "Louis", "Hannes", "Ozan"]
    while len(gruppe_a) > 0:
        print(gruppe_a.pop())

def aufgabe8():
    #Aufgabe 8: Die Reihenfolge der Liste ist zufällig. Füge Anna vor Tom ein.
    gruppe_c = ["Jan", "Tim", "David", "Jim", "Max", "Kai", "Eva", "Ute", "Tom"]
    gruppe_c.insert(gruppe_c.index("Tom"), "Ana")
    gruppe_c.pop(gruppe_c.index("David"))
    gruppe_c.insert(gruppe_c.index("Ute"), "David")

def aufgabe9():
    # Aufgabe 9:
    # Erkundige dich über die Listenmethode split()
    # Erstelle eine Liste aus "Thiersch;Mundt;Koch;Hemmasi"

    #lehrer_csv = "Thiersch;Mundt;Koch;Hemmasi"
    #lehrer_liste = lehrer_csv.split(";")
    #print(lehrer_liste)
    # Kürzer:
    print("Thiersch;Mundt;Koch;Hemmasi".split(";"))

aufgabe9()