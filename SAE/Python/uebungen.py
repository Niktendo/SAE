def aufgabe1():
    # Türsteher-Programm. welches die Volljährigkeit überprüft
    alter = int(input("Gebe dein Alter ein:"))

    if alter >= 18:
        print("Willkommen")
    else:
        print("Nicht Willkommen")

def aufgabe2():
    zahl = float(input("Gebe eine Zahl ein: "))

    if zahl < 13:
        print("Kleiner 13")
    elif zahl > 13:
        print("Größer 13")
    else:
        print("Zahl ist 13")

def aufgabe3():
    f1 = float(input("Erste Zahl: "))
    f2 = float(input("Zweite Zahl: "))

    if f1 > f2:
        print(f1, "ist größer.")
    else:
        print(f2, "ist größer.")

def aufgabe4():
    f1 = float(input("Erste Zahl: "))
    f2 = float(input("Zweite Zahl: "))
    f3 = float(input("Dritte Zahl: "))

    if f1 > f2:
        if f1 > f2:
            print(f1, "ist die Größte.")
    elif f2 > f3:
        print(f2, "ist die Größte.")
    else:
        print(f3, "ist die Größte.")

aufgabe4()