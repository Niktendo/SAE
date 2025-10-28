from math import sqrt
class Wuerfel:
    def __init__(self):
        self.seite = 0
        self.oberflaeche = 0
        self.raumdiagonale = 0

    def set_seite(self, seite):
        if seite >= 0:
                self.seite = seite
                self.oberflaeche = seite * seite * 6
                self.raumdiagonale = seite * sqrt(3)

    def get_seite(self):
        return self.seite
    
    def set_oberflaeche(self, oberflaeche):
        if oberflaeche >= 0:
                self.oberflaeche = oberflaeche
                self.seite = sqrt(oberflaeche / 6)
                self.raumdiagonale = sqrt(oberflaeche / 6) * sqrt(3)

    def get_oberflaeche(self):
        return self.oberflaeche

    def set_raumdiagonale(self, raumdiagonale):
        if raumdiagonale >= 0:
                self.raumdiagonale = raumdiagonale
                self.oberflaeche = raumdiagonale / sqrt(3) * raumdiagonale / sqrt(3) * 6
                self.seite = raumdiagonale / sqrt(3)

    def get_raumdiagonale(self):
        return self.raumdiagonale
    
hannes = Wuerfel()
hannes.set_seite(3)
print(hannes.get_oberflaeche())