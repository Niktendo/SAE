
# Begriffe

Wir kennen Bereits die Begriffe Datentyp und Datum (Objekt). 

```python
class Stift:
    def __init__(self, farbe):
        self.farbe = farbe

    def schreibe(self, text):
        print(f"Der {self.farbe}farbene Stift schreibt: {text}")

# Erstellen von Objekten (Exemplaren) der Klasse Stift
roter_stift = Stift("rot")
blauer_stift = Stift("blau")
gruener_stift = Stift("grün")

# Aufrufen der Methode der Objekte
roter_stift.schreibe("Hallo Welt!")
blauer_stift.schreibe("Python ist toll.")
gruener_stift.schreibe("Noch ein Satz.")

# Zugriff auf die Attribute der Objekte
print(f"Der rote Stift ist: {roter_stift.farbe}")
print(f"Der blaue Stift ist: {blauer_stift.farbe}")
```

1. `class Stift:`: Hier definieren wir eine Klasse namens `Stift`. Eine Klasse ist wie eine Bauanleitung oder eine Vorlage für die Erstellung von Objekten.
2. `def __init__(self, farbe):`: Dies ist der Konstruktor der Klasse. Er wird automatisch aufgerufen, wenn ein neues `Stift`-Objekt erstellt wird.
   - `self` ist eine Konvention und repräsentiert die Instanz des Objekts, das gerade erstellt wird.
   - `farbe` ist ein Parameter, der beim Erstellen eines neuen `Stift`-Objekts übergeben wird.
   - `self.farbe = farbe` speichert die übergebene Farbe als Attribut (eine Eigenschaft) des Stift-Objekts. Jedes `Stift`-Objekt hat seine eigene `farbe`.
3. `def schreibe(self, text):`: Dies ist eine Methode der Klasse `Stift`. Methoden definieren die Fähigkeiten oder Aktionen, die ein Objekt dieser Klasse ausführen kann.
   - `self` bezieht sich wieder auf das spezifische `Stift`-Objekt, auf dem die Methode aufgerufen wird.
   - `text` ist ein Parameter, der den Text enthält, den der Stift schreiben soll.
   - Die `print`-Anweisung simuliert das Schreiben, indem sie die Farbe des Stifts und den geschriebenen Text ausgibt.
4. `roter_stift = Stift("rot")`: Hier erstellen wir ein *Objekt* (auch Instanz genannt) der Klasse `Stift`. Wir rufen den Konstruktor `__init__` auf und übergeben die Farbe `"rot"`. Das neue `Stift`-Objekt wird der Variablen `roter_stift` zugewiesen.
5. `blauer_stift = Stift("blau")` und `gruener_stift = Stift("grün")`: Auf ähnliche Weise erstellen wir zwei weitere `Stift`-Objekte mit den Farben "blau" und "grün".
6. `print(f"Der rote Stift ist: {roter_stift.farbe}")`: Hier greifen wir auf das Attribut `farbe` des Objekts `roter_stift` zu, um seine Farbe auszugeben.
7. `roter_stift.schreibe("Hallo Welt!")`: Hier rufen wir die Methode `schreibe()` des Objekts `roter_stift` auf und übergeben den Text "Hallo Welt!". Die Methode verwendet die Farbe des spezifischen `roter_stift`-Objekts.

**Zusammenfassend lässt sich sagen:**

- Die **Klasse** `Stift` ist der Bauplan, der definiert, wie ein Stift aussieht (er hat eine Farbe) und was er tun kann (er kann schreiben).
- Die Variablen `roter_stift`, `blauer_stift` und `gruener_stift` sind **Objekte** oder Instanzen dieser Klasse. Jedes Objekt ist ein konkreter Stift mit einer bestimmten Farbe und der Fähigkeit zu schreiben.