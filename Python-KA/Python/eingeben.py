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