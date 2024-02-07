# Typumwandlung

# Automatische Typumwandlung
# Implizite Typkonversion
# Eine Operation mit unterschiedlichen
# aber kompatiblen Typen liefert
# ein Ergebnis des mächtigeren Typs
# print(1 + 0.0) # zwei Zahlen funktioniert
# print("1" + 1) # String + Zahl (int oder float) funktioniert nicht

# Erzwungene Typumwandlung
# Explizite Typkonversion
# Schreibt man datentyp(wert), versucht Python
# wert mit dem gewünschten Datentyp zu liefern.
# print(int("1") + 1)
# print(str(1) + "1")


# Eingaben von der Tastatur sind IMMER erst einmal Strings.
# Wenn man eine Zahl haben möchte, muss man die Eingabe zuerst
# umwandeln (erzwungene Typumwandlung).

eingabe = input("Gib eine Zahl ein ")
print(int(eingabe) + 7)

'''
Besprechen am 18.10.23:

a = input()
b = input()
print(int(a + b)) <- lolwut
'''
