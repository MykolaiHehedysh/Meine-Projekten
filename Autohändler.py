# Der Preis vom Auto 




Auto = int (input("gib die Summe vom Auto ein:"))
print(Auto, "ohne Aufschläge")

Steuer = int (input("\nGib die Prozentsteuer ein:"))
print (Steuer,"%")

Anmeldegebühr = int(input("\nGib das Anmeldegebühr ein:"))
print(Anmeldegebühr)

Agenturgebühr = int(input("Gib das Agenturgebühr auch ein:"))
print(Agenturgebühr)

Lieferung = int(input("Gib die Lieferung vom Auto ein:"))
print(Lieferung)


summe = Auto + Steuer + Anmeldegebühr + Agenturgebühr  + Lieferung
print ("Das ist die ganze Summe:", summe)


