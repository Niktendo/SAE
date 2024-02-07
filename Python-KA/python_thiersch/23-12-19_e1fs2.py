# nadel = 7
# b = 6
# c = 7
# d = 5
# 
# if nadel == b or nadel == c or nadel == d:
#     print("gefunden")
# else:
#     print("nicht gefunden")
# 
# 
# if nadel in (b, c, d):
#     print("gefunden")
# else:
#     print("nicht gefunden")
#     
# if "x" in "hanswurscht":
#     print("drin")
# else:
#     print("nicht drin")

# mitte = 5
# if 2 < mitte and mitte < 8:
#     print("dazwischen")
# 
# if 2 < mitte < 8:
#     print("dazwischen")

# a = 2
# b = 2
# c = 2
# d = 2
# if a == b == c == d:
#     print("alle gleich")


# a = 0 # Initialisierung der Schleifenvariable
# while a < 10: # Überprüfung der Schleifenvariable
#     a = a + 1 # Veränderung der Schleifenvariable
#     
# for (a = 0; a < 10; a = a + 1)

# Alle geraden Zahlen zwischen 0 und 100

# zahl = 0
# while zahl <= 100:
#     print(zahl)
#     zahl = zahl + 2

# Alle ungeraden Zahlen zwischen 0 und 100
# zahl = 1
# while zahl <= 100:
#     print(zahl)
#     zahl = zahl + 2

# Summe aller Zahlen zwischen 0 und 100


# Ein Programm fragt Benutzer so lange nach ihrem Passwort,
# bis das richtige eingegeben wurde.

# richtiges_pw = "verdansk"
# eingegebenes_pw = input("Gib Passwort: ")
# while eingegebenes_pw != richtiges_pw:
#     print("Falsches Passwort!")
#     eingegebenes_pw = input("Gib Passwort: ")
# print("Richtiges Passwort")


# In ein Sparkonto werden jährlich im Januar 400
# Euro eingezahlt. Im Dezember gibt es drei Prozent
# Zinsen. Schreibe ein Programm, das errechnet in wie
# vielen Jahren 10.000 Euro angespart sind.

# sparbetrag = 0
# jahr = 0
# while sparbetrag < 10000:
#     sparbetrag = sparbetrag + 400
#     zins = sparbetrag * 0.03
#     sparbetrag = sparbetrag + zins
#     jahr = jahr + 1
# print(jahr)

# Ermittle die Quersumme einer gegebenen Zahl
# mit Hilfe einer while-Schleife.
# Tipps:
# Beginne von hinten.
# Die letzte Ziffer bekommst du mit zahl % 10
# Die letzte Ziffer eliminierst du mit zahl // 10

# Lösung:
# while zahl != 0:
#     letzteziffer = zahl % 10
#     quersumme = quersumme + letzteziffer
#     zahl = zahl // 10
# print(quersumme)

# Lösung für vorzeichenbehaftete Zahlen
# zahl = -11
# zahl_original = zahl
# quersumme = 0
# 
# if zahl < 0: # Mach Zahl positiv, falls sie negativ ist
#     zahl = zahl * -1
# 
# while zahl != 0:
#     letzteziffer = zahl % 10
#     quersumme = quersumme + letzteziffer
#     zahl = zahl // 10
# 
# if zahl_original < 0: # Mach Ergebnis negativ, falls Zahl negativ war
#     quersumme = quersumme * - 1 
# 
# print(quersumme)

# Vertausche die Werte der Variablen a und b
# a = 2
# b = 7
# temp = a
# a = b
# b = temp
# print(a, b)

# Lösung nur für Python:
# a = 2
# b = 7
# a, b = b, a
# print(a, b)


#wort = "szutenberg"
# Mit wort[0] bekommen wir das erste Zeichen
# Mit wort[1] bekommen wir das zweite Zeichen
# Mit len(wort) bekommen wir die Länge
# Mit wort[len(wort) - 1] bekommen wir das letzte Zeichen

# Aufgabe: Durchlaufe das Wort mit einer while-Schleife
# und gib jedes Zeichen aus.

# wort = "janka"
# i = 0
# 
# while i < len(wort):
#     print(wort[i])
#     i = i + 1
    
# Aufgabe:
# Dein Programm soll True ausgeben, wenn
# ein Zeichen in einem Wort ist, sonst False.
# Löse das Problem mit einer while-Schleife.

# Beispiel ohne while:
# gesucht = "a"
# wort = "koffer"
# if gesucht in wort:
#     print(True)
# else:
#     print(False)
    
# Lösung
def aufgabe2():
    i = 0
    gesucht = "ö"
    wort = "arifiö"

    while i < len(wort) - 1 and wort[i] != gesucht:
        i = i + 1
    print(wort[i] == gesucht)

aufgabe2()

# 
# if i < len(wort):
#     print(True)
# else:
#     print(False)
