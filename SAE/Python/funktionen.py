'''
FUNKTIONEN
Funktionen haben einen Namen.
Auf den Namen folgen runde Klammern.
In den Klammern können Parameter stehen.
Mehrere Parameter werden durch Komma getrennt.

Die Parameter in den Klammern bilden den Funktionseingang.

Das Ergebnis der Funktion wird an die
AUFRUFSTELLE geliefert.
Der Aufruf löst sich zum Ergebniswert auf.

Funktionen sind Fragen an das Programm, die nach ihrem
Ablauf durch ihre Antwort ersetzt werden.

Für Aufrufer bedeutet
laenge = len("hallo")
das selbe wie
laenge = 5

Eine Funktion ist ein Programmstück, das anderen
Programmstücken dient. Es kann jederzeit von ihnen bentzt.
Im Deutschen auch "Unterprogramm" genannt.

Sich wiederholende Programmteile können in Funktionen
zusammengefasst werden. Das reduziert Redundanz.

Funktionsnamen bennenen entweder das Ergebnis der
Funktion oder sind ein Befehl, das Ergebnis zu erreichen.

Beispiele:
durchschnitt(1, 4, 9)
berechne_durchschnitt(1, 4, 9)
summe(4, 6, 8)
addiere(4, 6, 8)
produkt(1, 2, 3)
multiplizere(2, 4, 5)

Funktionen die Wahrheitswerte (True, False) liefern,
werden in der Regel als Frage formuliert, indem ein
is_ oder ist_ vorangestellt wird.

ist_palindrom("anna")

Wie Variablen, schreiben wir auch Funktionen
in den meisten Programmiersprachen klein.

Idealerweise lösen Funktionen genau ein Problem.
Daumenregel: Funktion sollte "auf einen Bildschirm" passen.

'''

def addiere(a, b):
    summe = a + b
    return summe
#print(addiere(3, 5))

def multipliziere(a, b):
    return a * b
#print(multipliziere(3, 5))


def is_palindrome(wort):
    wort = wort.lower().replace(' ', '')
    return wort == wort[::-1]
#print(is_palindrome_while("dreh mal am herd"))

def is_palindrome_while(wort):
    wort = wort.lower().replace(' ', '')
    i = 0
    while i < (len(wort) // 2) and wort[i] == wort[(len(wort) - 1) - i]:
            i += 1
    return wort[i] == wort[(len(wort) - 1) - i]

#print(is_palindrome_while("Anna"))

#Ermittle die größte Ziffer aus einem String
def groesste_ziffer(str):
    ziffer = int(str[0])
    i = 1
    while i < len(str):
        if ziffer < int(str[i]):
            ziffer = int(str[i])
        i += 1
    return ziffer

# Thiersch-Methode
# gemerkt = 0
# zahl = "0913378001"
# i = 0
# while i < len(zahl):
#     if int(zahl[i]) > gemerkt:
#         gemerkt = int(zahl[i])
#     i = i + 1
# print(gemerkt)
print(groesste_ziffer("45748757124359"))