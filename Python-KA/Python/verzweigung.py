# name = input("Name: ")
# if name.lower() == "niklas":
#     name = "Meister"
# print("Hallo,", name)


# Verzweigung
## if
# Mit 'if' wird ein Vergleich eingeleitet.
# Ergibt dieser True (wahr), wird der
# folgende Codeblock (eingerückte Zeilen) ausgeführt.
# Ergibt er aber False (falsch), wird der folgende
# Codeblock übersprungen.

# if True:
#     print("Bedingung ist wahr")
# print("Fertig")


name = input("Name: ")
if name == "niklas":
    name = "Meister"
print("Hallo,", name)

name = input("Name: ")
if name == "Niklas":		# falls
    print("Hallo, Meister")
else:						# sonst
    print("Hallo,", name)
    
# Aufgabe:
# Schreibe ein Programm, das zwei Zahlen einliest und
# die Größte ausgibt

