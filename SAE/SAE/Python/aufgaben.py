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
    #Aufgabe 3: Typumwandlung
    print("\nAufgabe 3")
    '''
    Typumwandlung
    Automatische / Implizite Typkonversion
    Eine Operation mit unterschiedlichen aber kompatiblen Typen liefert ein Ergebnis des  mächtigeren Typs
    '''
    #print(1 + 1.0) # Zwei Zahlen funktioniert
    #print("1" + 1.0) # String + Zahl funktioniert nicht
    '''
    Erzwungene / Explizite Typkonversion
    Schreibt man Datentyp (Wert), versucht Python Wert mit dem gewünschten Datentyp  zu liefern.
    '''
    #print(int("1") + 0.0)
    #print(str(1) + "1")
    '''
    Eingaben von der Tastatur sind IMMER erstmal Strings, sie müssen zunächst mit der erzw. Typumwandung behandelt werden.
    '''
    eingabe = input("Gib eine Zahl ein:\n")
    print((int(eingabe)) + 88)

def aufgabe4():
    #Aufgabe 4: Gib zwei Zahlen ein
    print("\nAufgabe 4")
    i1 = 0
    i2 = 0
    i1 = input("Gebe die erste Zahl ein: ")
    i2 = input("Gebe die zweite Zahl ein: ")
    print("OUTPUT:", (int(i1)) + (int(i2)))

def aufgabe5():
    #Aufgabe 5: Exponenten u.a.
    print("\nAufgabe 5")
    basis = float(input("Basis: "))
    exponent = float(input("Exponent: "))
    #print(basis**exponent) # oder andere Methode                
    print(f"{basis**exponent:.2f}") # .2f steht für float also Kommazahlen                

def aufgabe6():
    #Aufgabe 6: Datum ausgeben, mehrere Methoden
    print("\nAufgabe 6")
    tag = input("Tag: ")
    monat = input("Monat: ")
    jahr = input("Jahr: ")
    #print(tag, monat, jahr, sep=".")
    #print(tag + "." + monat + "." + jahr) # Andere Methode
    print(f"{tag:0>2}.{monat:0>2}.{jahr}") # Müssen wir nicht wissen

def aufgabe7():
    #Aufgabe 7: If-Cases
    '''
    Schreibe ein Programm, welches einen eingegeben Namen
    mit "Hallo" + name beantwortet.
    Falls der Name aber "Thiersch" ist, sagt es "Hallo Meister".
    '''
    print("\nAufgabe 7")
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
    '''
    Mit if wird ein Vergleich eingeleitet. Ergiebt dieser "true", so wird der folgende Codeblock ausgeführt.
    Wenn nicht, wird dieser übersprungen.
    '''
def aufgabe8():
    #Aufgabe 8: Größte Zahl ausgeben
    print("\nAufgabe 8")
    '''
    Aufgabe:
    Schreibe ein Programm, das zwei Zahlen einliest und
    die Größte ausgibt.
    '''
    imax = ''
    i1 = float(input("Zahl 1: "))
    i2 = float(input("Zahl 2: "))
    print("OUTPUT:")
    if i1 == i2:
        print("Beide Zahlen sind gleich groß.")
    elif i1 < i2:
        imax = i2
    else:
        imax = i1
    print(imax)

    imax = 0
    i1 = float(input("Zahl 1: "))
    i2 = float(input("Zahl 2: "))
    i3 = float(input("Zahl 3: "))
    if i1 > i2:
        if i1 > i3:
            imax = i1
        else:
            if i3 > i2:
                imax = i3
    else:
        if i2 > i3:
            imax = i2
        else:
            imax = i3
    print("OUTPUT:")
    print(imax)

'''
Die Verschachtelung im unteren Beispiel lässt sich durch else if (elif) lösen.
'''

def aufgabe9():
    #Aufgabe 9: Größte aus drei Zahlen mit if, and, or
    print("\nAufgabe 9")
    '''
    Aufgabe:
    Schreibe ein Programm, das drei Zahlen einliest und
    die Größte ausgibt.
    '''

    i1 = 1
    i2 = 3
    i3 = 2
    imax = i3

    if i1 > i2 and i1 > i3:
            imax = i1
    elif not i1 > i2 and i2 > i3:
            imax = i2
    #elif i1 > i2 and not i1 > i3 or not i1 > i2 and not i2 > i3:
    #        imax = i3

    print("OUTPUT:")
    print(imax)

def aufgabe10():
    #Aufgabe 10: Schaltjahr mit einem if/else
    print("\nAufgabe 10")

    ergebnis = "Kein Schaltjahr"
    jahr = 2020

    if jahr % 4 == 0 and jahr % 100 == 0 and jahr % 400 == 0 or jahr % 4 == 0 and jahr % 100 != 0:
        ergebnis = "Schaltjahr"

    print("OUTPUT:")
    print(f"{jahr} ist {ergebnis}")

def aufgabe11():
    #Aufgabe 11: Prüfen von geometrischen Eigenschaften
    print("\nAufgabe 11")

    a = 15
    b = 10
    c = 10
    d = 15

    ergebnis = list()

    if a == b == c == d:
        ergebnis.append("Quadrat, Raute")
    
    if a == c and b == d:
        ergebnis.append("Rechteck, Paralellogram")

    if a == b and c == d or b == c and d == a:
        ergebnis.append("Drachen")

    print("OUTPUT:")
    print("Eigenschaften von", ", ".join(ergebnis))

def aufgabe12():
    #Aufgabe 12: While-Schleife bis 100
    print("\nAufgabe 12")

    i = 0

    while i < 100:
        i += 1
        if i % 2 == 1:
            print(i)

aufgabe12()