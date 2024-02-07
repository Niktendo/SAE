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


# name = input("Name: ")
# if name == "niklas":
#     name = "Meister"
# print("Hallo,", name)
# 
# name = input("Name: ")
# if name == "Niklas":		# falls
#     print("Hallo, Meister")
# else:						# sonst
#     print("Hallo,", name)
    
# Aufgabe:
# Schreibe ein Programm, das zwei Zahlen einliest und
# die Größte ausgibt

# a = float(input("Gib Zahl: "))
# b = float(input("Gib noch ne Zahl: "))
# if a > b:
#     print(a)
# else:
#     print(b)

# Erweitere das Programm so, das wenn beide Zahlen gleich sind,
# "die Zahlen sind gleich" ausgegeben wird.

a = float(input("Gib Zahl: "))
b = float(input("Gib noch ne Zahl: "))
  
if a > b:
    print(a)
else:
    if a < b:
        print(b)
    else:
        print("gleich")

# Der untere Code ist äquivalent zum oberen Code.
# elsif ist eine Abkürzung für "else: if"

a = float(input("Gib Zahl: "))
b = float(input("Gib noch ne Zahl: "))
  
if a > b:
    print(a)
elif a < b:
    print(b)
else:
    print("gleich")


# Mermaid
'''
flowchart TD
    A[Eingabe a] --> B[Eingabe B]
    B --> C{a > b}
    C -->|True| D[a]
    C -->|False| E[b]
'''


