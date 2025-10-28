1

a) Entwickle die Klasse Viereck. Sie besitzt die gekapselten Attribute (für die vier Seiten): a, b, c, d.

b) Erweitere die Klasse um die Methode get_umfang().

c) Schreibe die Funktion analysiere_viereck(v : Viereck). Sie gibt eine der folgenden Zeichenketten zurück: "Quadrat oder Rhombus" | "Weder Quadrat noch Rhombus".

d) Erweitere die Funktion analysiere_viereck(v : Viereck) so, dass die in der unteren Tabelle aufgeführten Eigenschaften von Vierecken erkannt und zurückgegeben werden.

| **Seitenlängen**                                       | **Mögliche Viereckstypen / Eigenschaften**        |
|----------------------------------------------------|-----------------------------------------------|
| **Vier gleiche Seiten**                                | Quadrat (wenn rechtwinklig), Rhombus          |
| **Zwei Paare gleich langer gegenüberliegender Seiten** | Parallelogramm, Rechteck, Rhombus             |
| **Zwei Paare gleich langer benachbarter Seiten**       | Drachenviereck                                |
| **Alle Seiten unterschiedlich**                        | Allgemeines Viereck                           |
| **Drei gleiche Seiten, eine verschieden**              | Allgemeines Viereck (kein spezieller Typ)     |
| **Eine Seite länger als die Summe der drei anderen**   | ❌ **Kein gültiges Viereck** (schließt sich nicht) |
