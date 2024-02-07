# Größte aus Dreien

# a = 3
# b = 3
# c = 5
# 
# if a > b and a > c:
#     print(a)
# elif b > c:
#     print(b)
# else:
#     print(c)


jahr = 2000

if jahr % 4 == 0 and jahr % 100 != 0 or jahr % 400 == 0:
    print("Schaltjahr")
else:
    print("Kein Schaltjahr")