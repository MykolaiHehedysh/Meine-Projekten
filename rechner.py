

# Rechner 

zahl_1 = int(input("Tippe die erste Zahl!"))
zahl_2 = int (input("Tippe die zweite Zahl!"))
zeichen = input("Wähle das Rechnungseichen (+,-,*,:)")

if zeichen not in ["+", "-", "*", ":"]:
    print("Falsches Rechnungszeichen!")
else:
    if zeichen == "+":
        summe = zahl_1 + zahl_2
    elif zeichen == "-":
        summe = zahl_1 - zahl_2
    elif zeichen == "*":
        summe = zahl_1 * zahl_2
    elif zeichen == ":":
        summe = zahl_1 / zahl_2
    
    print(summe)
