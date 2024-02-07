geheimnis = "IWHH ndqq doohv zdv vlh hfkw nöqqhq zloo!"
alphabet = "abcdefghijklmnopqrstuvwxyz"

maximum = 0
max_char = None
for char in alphabet:
    current = geheimnis.lower().count(char)
    if current > maximum:
        maximum = current
        max_char = char

print(max_char)

key = ord(max_char) - ord("e")

botschaft = ""
for zeichen in geheimnis:
    botschaft += chr(ord(zeichen) - key)
    
print(botschaft)
