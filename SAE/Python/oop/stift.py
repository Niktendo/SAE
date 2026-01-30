class Stift:
    def __init__(self, breite = "10cm"):
        self.__breite = breite
        self.__farbe = "weiss"
    
    def schreiben(self, text):
        print(f"{self.__farbe}-Stift mit {self.__breite} schreibt: {text}")

    def get_farbe(self):
        return self.__farbe

    def set_farbe(self, farbe):
        self.__farbe = farbe

Stift1 = Stift("12cm")
Stift1.set_farbe("schwarz")
print(Stift1.get_farbe())
Stift1.schreiben("Ich bin Stift1")

Stift2 = Stift()
print(Stift2.get_farbe())
Stift2.schreiben("Ich bin Stift2")