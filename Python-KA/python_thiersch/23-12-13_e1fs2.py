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

sparbetrag = 0
jahr = 0
while sparbetrag != 10000:
    sparbetrag = sparbetrag + 400
    zins = sparbetrag * 0.03
    sparbetrag = sparbetrag + zins
    jahr = jahr + 1
print(jahr)

# Ermittle die Quersumme einer gegebenen Zahl
# mit Hilfe einer while-Schleife.
# Tipps:
# Beginne von hinten.
# Die letzte Ziffer bekommst du mit zahl % 10
# Die letzte Ziffer eliminierst du mit zahl // 10



 
 