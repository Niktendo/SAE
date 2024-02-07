v_basis = float(input())
bonus = float(input())
level = float(input())

v_bonus = (bonus / 100) * (level - 1)
v_angriff = v_basis * (1 + v_bonus)

print("Bonusangriffsgeschwindigkeit:", format(v_bonus, ".2f"), sep="")
print("Angriffsgeschwindigkeit", format(v_angriff, ".7f"))