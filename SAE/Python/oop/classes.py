class Stift:
    def __init__(self, farbe):
        self.farbe = farbe

    def schreiben(self, text):
            print(f"{self.farbe}-farbener Stift schreibt {text}")

kuli = Stift("schwarz")
kuli.schreiben("Hallo E2FS2")