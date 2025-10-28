class Viereck:
    def __init__(self, a, b, c, d):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
    
    def set_a(self, a):
        self.__a = a

    def set_b(self, b):
        self.__b = b

    def set_c(self, c):
        self.__c = c

    def set_d(self, d):
        self.__d = d

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b
    
    def get_c(self):
        return self.__c
    
    def get_d(self):
        return self.__d

    def get_umfang(self):
        return self.__a + self.__b + self.__c + self.__d

v = Viereck()
v.set_a(6)
v.set_b(5)
v.set_c(6)
v.set_d(6)
print(v.get_d())
print(v.get_umfang())
def analysiere_viereck(v):
#    if v.get_a() == v.get_b() == v.get_c() == v.get_d():
#        return "Quadrat oder Rhombus"
#    else:
#        return "Weder Quadrat noch Rhombus"

# Unvollständig!!!
    if v.get_a() == v.get_b() == v.get_c() == v.get_d():
        return "Quadrat oder Rhombus"
    elif v.get_a() == v.get_c() and v.get_b() == v.get_d():
        return "Parallelogramm, Rechteck oder Rhombus"
    elif v.get_a() == v.get_b() and v.get_c() == v.get_d():
        return "Drachenviereck"
    elif v.get_a() == v.get_b() and v.get_c() == v.get_d():
        return "Drachenviereck"
    elif v.get_a() == v.get_b() and v.get_c() == v.get_d():
        return "Drachenviereck"
    elif v.get_a() == v.get_b() and v.get_c() == v.get_d():
        return "Drachenviereck"
print(analysiere_viereck(v))