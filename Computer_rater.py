# Das ist ein sogenanntes Spiel mit dem Computer,
# wo er deine gewünschte Zahl raten muss



import random


mensch = int(input("Denk dir eine Zahl von 1 bis 100 aus: "))

low = 1
high = 100
versuch = 0

while True:
    summe = (low + high) // 2  
    versuch += 1
    print(f"Computer rät: {summe}")
    
    if summe < mensch:
        print("Mehr!")
        low = summe + 1  
    elif summe > mensch:
        print("Weniger!")
        high = summe - 1  
    else:
        print(f"Super! Der Computer hat die Zahl {summe} nach {versuch} Versuchen erraten!")
        break
