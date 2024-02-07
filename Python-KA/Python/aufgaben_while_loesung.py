#Aufgaben: Schreibe jeweils ein Programm, in dem du mit while-Schleifen folgende Aufgaben löst:

# Aufgabe 1
# Gib alle Zahlen zwischen 0 und 100 aus (0 bis 100).

# Aufgabe 2
# Gib alle geraden Zahlen zwischen 0 und 100 aus (0 bis 100).

# Aufgabe 3
# Gib alle ungeraden Zahlen zwischen 0 und 100 aus (1 bis 99).

# Aufgabe 4
# Gib die Summe aller Zahlen von 0 bis 100 aus.

# zahl = 0
# summe = 0
# while zahl < 100:
#     summe = summe + zahl
#     zahl = zahl + 1
# print(summe)

# Aufgabe 5
# Gib den Durchschnitt aller Zahlen von 0 bis 100 aus.

# Aufgabe 6
# Gib das Produkt aller Zahlen von 1 bis 100 aus.

# Aufgabe 7
# Gib die Summe aller Zahlen zwischen 0 und einer eingegebenen positiven Zahl aus.

# Aufgabe 8
# Gib die Summe aller Zahlen zwischen zwei gegebenen Zahlen aus. Grundannahme: die zweite Zahl ist größer als die erste. Bonus: Erweitere das Programm so, dass es egal ist, ob die zweite Zahl größer ist oder nicht.

# Aufgabe 9
# Implementiere das FizzBuzz-Spiel in einer while-Schleife. Das Programm soll Zahlen von 1 bis 100 ausgeben, wobei es "Fizz" für Vielfache von 3, "Buzz" für Vielfache von 5 und "FizzBuzz" für Vielfache von 3 und 5 ausgibt.

# Aufgabe 10
# Schreibe ein Passwort-Prüfprogramm. Es fragt Benutzer so lange nach einem Passwort, bis das richtige eingegeben wurde. Danach kommt die Ausgabe: "Login erfolgreich".

# Aufgabe 11
# In ein Sparkonto werden jährlich im Januar 400 Euro eingezahlt. Im Dezember gibt es drei Prozent Zinsen. Schreibe ein Programm, das errechnet, in wie vielen Jahren 10.000 Euro angespart sind.

# Aufgabe 12
# Ermittle die Anzahl der Ziffern einer gegebenen Zahl. Tipp: Mit ```zahl // 10``` eliminierst du die letzte Ziffer.

# Aufgabe 13
# Gib die Quersumme einer gegebenen Zahl aus. Tipp: Beginne von hinten. Mit ```zahl % 10``` bekommst du die letzte Ziffer. Mit ```zahl // 10``` eliminierst du die letzte Ziffer.

# Aufgabe 14
# Drehe eine gegebene Zahl um. Tipp: Beginne von hinten. Mit ```zahl % 10``` bekommst du die letzte Ziffer. Mit ```zahl // 10``` eliminierst du die letzte Ziffer. Mit ```zahlenstring + str(ziffer)``` kannst du eine Ziffer mit einem Zahlenstring konkatenieren.

# Aufgabe 15
# Gib alle Zeichen eines Strings einzeln aus. Nutze dazu eine while-Schleife. Hinweise mit der Voraussetzung ```wort = "hallo"```: ```wort[0]``` liefert das erste Zeichen eines Strings, ```wort[1]``` das zweite Zeichen usw. Die Länge des Strings liefert ```len(wort)```. Das letzte Zeichen bekommst du zum Beispiel mit ```wort[len(wort)-1]```.

# i = 0
# wort = "blubber"
# while i < len(wort):
#     print(wort[i])
#     i = i + 1

# Aufgabe 16
# Bilde die Quersumme einer ganzen Zahl, indem du sie zuerst zu einem String konvertierst und diesen anschließend mit einer while-Schleife durchläufst. Hinweis: Damit du die einzelnen Ziffern addieren kannst, musst du sie wieder in eine Ganzzahl konvertieren.

# zahl = str(1337)
# i = 0
# quersumme = 0
# while i < len(zahl):
#     quersumme = quersumme + int(zahl[i])
#     i = i + 1
# print(quersumme)

# Aufgabe 17
# Wenn ein String ein gesuchtes Zeichen enthält, gibt das Programm ```True``` aus. Sonst ```False```.

gesucht = "x"
wort = "hanswurst"
i = 0
while i < len(wort) and wort[i] != gesucht:
    i = i + 1
#print(i < len(wort))
   


# Aufgabe 18
# Ermittle die höchste Ziffer in einem String, der nur aus Ziffern besteht. Zum Beispiel "1337", "1231235123".

def hoechste_ziffer(zahl):
    i = 1
    groesste_ziffer = int(zahl[0])
    while i < len(zahl):
        if int(zahl[i]) > groesste_ziffer:
            groesste_ziffer = int(zahl[i])
        i += 1
    return groesste_ziffer
print("Die größte Ziffer ist:", hoechste_ziffer("176281"))

# Aufgabe 19
# Wenn ein String ein Palindrom ist, gibt das Programm ```True``` aus. Sonst ```False```. Löse das Problem mit einer while-Schleife. Ein Palindrom klingt gleich, egal ob es vorwärts oder rückwärts gelesen wird. Beispiele: ehe, anna, kajak, rentner, reliefpfeiler. Bonus: Erweitere dein Programm so, dass es auch Satzpalindrome erkennen kann. Beispiele für Satzpalindrome: "anna hetzte hanna", "dreh mal am herd", "ein eis esse sie nie". Tipp: ```wort.replace('ae', 'ä')``` ersetzt alle 'ae' in Wort durch 'ä'.
