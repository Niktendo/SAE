def Main():
    mac_adressen = [
        "00:1A:2B:3C:4D:5E",
        "00:1A:2B:3C:4D:5F",
        "00:1A:2B:3C:4D:5G",        
    ]
    gefunden = SucheMAC(mac_adressen, "00:1A:2B:3C:4D:5X")
    return gefunden

def SucheMAC(mac_adressen, mac):
    return mac in mac_adressen
#
#    i = 0
#    while i < len(mac_adressen):
#        i += 1
#        if mac_adressen[i-1] == mac:
#            return True
#        else:
#            return False
#
#    i = 0
#    while i < len(mac_adressen) - 1 and mac != mac_adressen[i]:
#        i += 1
#    return mac == mac_adressen[i]

print(Main())