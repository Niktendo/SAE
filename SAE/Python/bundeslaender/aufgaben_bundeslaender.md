1. Ein Programm soll die Daten in der Datei bundeslaender.csv um die Spalte "Einwohner je qkm" mit den entsprechenden Daten für jedes Bundesland erweitern. Speichere das Ergebnis in der Datei bundeslaender_erweitert.csv
   1. Nenne alle nötigen Teilschritte
   2. Nenne zu jedem Teilschritt die benötigten Python-Werkzeuge
   3. Implementiere das Programm
2. Als nächstes sollen folgende Spalten für jedes Bundesland berechnet und angefügt werden: "Anteil an Gesamtfläche", "Anteil an Gesamtbevölkerung", "Bevölkerungsdichte"
   1. Überlege dir, welche Programmteile des bestehenden Programms in Funktionen ausgelagert werden sollten.
   2. Markiere die Programmteile, die du in Funktionen auslagern würdest mit Kommentaren.
   3. Implementiere das Anfügen der neuen Spalten. Die Bevölkerungsdichte eines Bundeslands bekommt das Attribut "hoch", wenn sie über der Bevölkerungsdichte der Bundesrepublik Deutschland liegt, sonst "gering".