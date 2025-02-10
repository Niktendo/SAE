# def flugpreise(pnutzlast, pentfernung):
#     if pentfernung <= 25 and pnutzlast <=12:
#         if pnutzlast <= 6:
#             preis_nutzlast = 3
#         else:
#             preis_nutzlast = 7
#         gesamtpreis = preis_nutzlast + pentfernung * 0.4

#         print(f"Gesamtpreis des Transportes: {gesamtpreis:.2f}€")
#     else:
#         print("Mit diesen Angaben ist ein Drohnentransport nicht möglich.")

def flugpreise(pnutzlast, pentfernung): print(f"Gesamtpreis des Transportes: {3 + pentfernung * 0.4:.2f}€" if pentfernung <= 25 and pnutzlast <= 6 else f"Gesamtpreis des Transportes: {7 + pentfernung * 0.4:.2f}€" if pentfernung <= 25 and pnutzlast <= 12 else "Mit diesen Angaben ist ein Drohnentransport nicht möglich.")

flugpreise(12, 25)