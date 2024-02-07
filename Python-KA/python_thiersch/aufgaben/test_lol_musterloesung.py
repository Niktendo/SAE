basis = float(input("Gib Basisangriffsgeschwindigkeit ein: "))
bonus = float(input("Gib Bonus pro Level ein: "))
level = float(input("Gib Level ein: "))
 
bonusgeschwindigkeit = bonus / 100 * (level -1)
angriffsgeschwindigkeit = basis * (1 + bonusgeschwindigkeit)

print(f"Der Champion erhält auf Level 10 einen Bonus von {100 * bonusgeschwindigkeit:.2f} Prozent")
print(f"Der Aotoangriff erfolgt {angriffsgeschwindigkeit:.7f} mal in der Sekunde")
