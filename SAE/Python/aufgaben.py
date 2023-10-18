def aufgabe1():
    #Aufgabe 1: Name einlesen
    print("\nAufgabe 1")
    name = input("Gebe den Namen ein: ")
    print("OUTPUT:", name)

def aufgabe2():
    #Aufgabe 2: Name einlesen und Begrüßen
    print("\nAufgabe 2")
    name = input("Gebe den Namen ein: ")
    print("OUTPUT:", "Hallo, " + name)

def aufgabe3():
    #Aufgabe 3: Gib zwei Zahlen ein
    print("\nAufgabe 3")
    i1 = 0
    i2 = 0
    i1 = input("Gebe die erste Zahl ein: ")
    i2 = input("Gebe die zweite Zahl ein: ")
    print("OUTPUT:", (int(i1)) + (int(i2)))

def aufgabe4():
    #Aufgabe 4: Exponenten u.a.
    print("\nAufgabe 4")
    basis = float(input("Basis: "))
    exponent = float(input("Exponent: "))
    #print(basis**exponent) # oder andere Methode                
    print(f"{basis**exponent:.2f}") # .2f steht für float also Kommazahlen                

def aufgabe5():
    #Aufgabe 5: Datum ausgeben, mehrere Methoden
    print("\nAufgabe 5")
    tag = input("Tag: ")
    monat = input("Monat: ")
    jahr = input("Jahr: ")
    #print(tag, monat, jahr, sep=".")
    #print(tag + "." + monat + "." + jahr) # Andere Methode
    print(f"{tag:0>2}.{monat:0>2}.{jahr}") # Müssen wir nicht wissen

def aufgabe6():
    #Aufgabe 6: If-Cases
    '''
    Schreibe ein Programm, welches einen eingegeben Namen
    mit "Hallo" + name beantwortet.
    falls der Name aber "Thiersch" ist, sagt es
    "Hallo Meister".
    '''
    print("\nAufgabe 6")
    #name = input("Name: ")
    #if name == "Niklas":
    #    print("Hallo Meister")
    #else:
    #    print("Hallo", name)
    
    #KÜRZER
    name = input("Name: ")
    if name == "Niklas":
        name = "Meister"
    print("Hallo", name)

aufgabe6()