class Stift:
    def __init__(self):
        self.spitze = "Gerade"
        self.__breite = 8
        self.__breite2 = 9
        self.__dicke = 5
        self.__dicke2 = 4

    def set_dicke(self, dicke):
        self.__dicke = dicke

    def set_dicke2(self, dicke2):
        self.__dicke2 = dicke2

    def get_dicke(self):
        return self.__dicke
    
    def get_dicke2(self):
        return self.__dicke2
    
    def breite_gesamt(self):
        return self.__breite + self.__breite2

niklas = Stift()
print(niklas.spitze, niklas.breite_gesamt())

def berechne_dicke():
    return niklas.get_dicke() + niklas.get_dicke2()
print(berechne_dicke())