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

Lokale Variablen:

Variablen gelten immer in dem Kontext, in dem sie definiert wurden.
Nachdem eine Funktion terminiert (beendet) ist, existieren ihre
Variablen nicht weiter.

Umgekehrt "sieht" eine Funktion in Python aber die Variablen, die im Kontext
ihres Aufrufs existiert haben.

Lokal überdeckt Global
Haben Variablen dieselben Namen, überdecken lokale Variablen globale Variablen.



'''
summe = 12
# Funktion addiere
def addiere(a, b):
# Definiere Funktion mit dem Namen addiere und den Parametern a, b
    summe = a + b
    return summe
    # Gib den Wert von summe an die Aufrufstelle zurück
print(addiere(1, 2))
    
def multipliziere(a, b):
    return a + b

def ist_palindrom(wort):
    wort = wort.lower().replace(" ", "")
    return wort == wort[::-1]

def ist_palindrom_while(wort):    
    links = 0
    rechts = len(wort) - 1
    while links < rechts and wort[links] == wort[rechts]:
        links = links + 1
        rechts = rechts - 1
    return links >= rechts

print(ist_palindrom("dreh mal am Herd"))

testvariable = "keintest"

def werde_aufgerufen():
    print(testvariable)

def definiere_rufe_auf():
    testvariable = "test"
    werde_aufgerufen()
    
definiere_rufe_auf()
    

# Schreibe eine Funktion, die die größte Ziffer aus einem String liefert


def maximum(zahl):
    gemerkt = 0
    i = 0
    while i < len(zahl):
        if int(zahl[i]) > gemerkt:
            gemerkt = int(zahl[i])
        i = i + 1
    return gemerkt



def maximum(zahl):
    return max(zahl)

print(maximum("0449007"))



