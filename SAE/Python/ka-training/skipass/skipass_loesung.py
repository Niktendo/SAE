daten = '''Jan 09 2016|09:15:17|30201|1|SL02|650
Jan 09 2016|09:15:18|43097|1|SL01|945
Jan 09 2016|09:15:19|28774|2|SB03|1389
Jan 09 2016|09:16:21|00788|1|SL02|650
Jan 09 2016|09:17:25|03361|3|SL01|945
Jan 09 2016|09:17:33|08385|1|SL02|650
Jan 09 2016|09:18:43|10234|1|SL01|945
Jan 09 2016|09:21:55|00788|1|SL02|650
Jan 09 2016|09:24:43|03361|3|SB03|1389
Jan 09 2016|09:26:01|30201|1|SB03|1389
Jan 09 2016|09:26:21|28774|2|SL02|650
Jan 09 2016|09:26:25|00788|1|SL02|650
Jan 09 2016|09:27:21|28774|2|SL02|650
Jan 09 2016|09:29:32|30201|1|SL01|945
Jan 09 2016|09:30:12|34032|1|SB03|1389
Jan 09 2016|09:30:15|08767|3|SL02|650'''

zeilen = daten.split("\n")

summe = 0
for zeile in zeilen:
    bloecke = zeile.split("|")
    if bloecke[2] == "30201":
        summe = summe + int(bloecke[5])  
print(summe)

summe = 0
for zeile in zeilen:
    if zeile.split("|")[2] == "30201":
        summe = summe + int(zeile.split("|")[5])     
print(summe)