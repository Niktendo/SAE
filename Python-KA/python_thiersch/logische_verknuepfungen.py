# a = 10
# b = 10
# 
# if not a != 10:
#     print("irgendwas")

# # not dreht einen Wahrheitswert (True, False)
# # um. Aus False wird True und aus True wird
# # False. Wahrheitswerte nennen wir auch
# # boolesche Werte (boolean)
# 
# # Mit type(True), type(False) können wir zeigen,
# # dass True und False den Typ "bool" haben.

# a = False
# b = False
# 
# if a and b:
#     print("ballert")


# # a = True
# # b = False
# # 

#     
# '''
# Wahreitstabelle
# 
# a		b		a and b		a or b
# True	True	True		True
# True	False	False		True
# False	True	False		True
# False	False	False		False
# 
# '''
# 
# '''
# Exkurs Bitweises UND
#     101
# &   001
# =	  001 
# 
# '''

# a = True
# b = False
# 
# if a or b or True:
#     print("ballert")


# 
# if Bedingung1:
#     # Dieser Code wird ausgeführt
#     # wenn Bedingung1 True ist.
#     if Bedingung2:
#         # Dieser Code wird ausgeführt 
#         # wenn Bedingung1 und Bedingung2 True sind.
#         
# if Bedingung1 and Bedingung2:
#     # Dieser Code wird ausgeführt 
#     # wenn Bedingung1 und Bedingung2 True sind.  
# 

#Aufgaben:
# Größter aus Dreien mit not, and, or

# Schaltjahr mit not, and, or

a = 1
b = 3
c = 4
d = 5
e = 1

if a == b or a == c or a == d or a == e:
    print("irgendwas")

if a in (b, c, d, e):
    print("irgendwas")
    
if "m" in "emma":
    print("ja")
