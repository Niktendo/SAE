class Stift:
    
    def __init__(self, farbe):
        self.farbe = farbe
        
    def schreiben(self, text):
        print(f"{self.farbe}-farbener Stift schreibt {text}")
        
#kuli = Stift("schwarz")
#kuli.schreiben("Hallo E2FS2")
    
'''
Erstelle eine Klasse Tier.
Sie hat das Attribut laut.
Sie hat die Methode gib_laut().

Beim Aufruf der Methode macht die Kuh "Muh", das Schaf "Mäh".

'''

class Tier:
    def __init__(self, laut):
        self.laut = laut

    def gib_laut(self):
        print(self.laut)

schaf = Tier("Mäh")
schaf.gib_laut()

kuh = Tier("Muh")
kuh.gib_laut()