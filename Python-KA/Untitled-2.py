einkommen = int(input("Monatliches Einkommen: ")) * 12

if einkommen < 30000:
    print("Einkommen ist: 21", einkommen * 100 * 0.21)
elif einkommen <= 62800:
    print("Einkommen ist: 35", einkommen * 100 * 0.35)
else:
    print("Einkommen ist: 42", einkommen * 100 * 0.42)