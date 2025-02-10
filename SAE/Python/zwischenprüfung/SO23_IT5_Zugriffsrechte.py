import random

def DB_Abfrage(user, pw):
    return (random.randint(0,2))
def LoginUeberpruefung(user, pw):
    ergebnis = DB_Abfrage(user, pw)
    if ergebnis == 0:
        return True
    else:
        return False, "Daten nicht korrekt"

print(LoginUeberpruefung("A", "H"))