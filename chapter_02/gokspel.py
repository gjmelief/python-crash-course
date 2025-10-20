"""Oefening 1: Gokspel Raad het Getal
Maak een gokspel waarbij de computer een willekeurig getal tussen 1 en 100 kiest, en de speler moet raden wat het is.

Specificaties:
Willekeurig getal: Gebruik import random en random.randint(1, 100) om een getal te kiezen
Input van speler: Vraag de speler om een getal te raden
Feedback geven: Zeg of het geraden getal te hoog, te laag, of correct is
Herhalen: Blijf vragen totdat het juiste getal is geraden
Teller: Houd bij hoeveel pogingen de speler heeft gedaan
Functie: Maak een functie speel_spel() die het hele spel bevat
Extra uitdaging:
Geef een compliment als ze het in ≤5 pogingen raden
Geef een aanmoediging als het meer dan 10 pogingen duurt"""

import random

def speel_spel():
    random.seed(1) # voor debugging
    getal = random.randint(1, 100) # Getal wat de speler moet raden
    print("Ik heb een getal gekozen tussen 1 en 100. Raad het!")
    gok = input("Jouw gok, alleen hele getallen!: ") # Laat speler getal invullen
    gok = int(gok) # converteer input naar integer
    teller = 1 # start de teller

    aanmoediging_gegeven = False

    while gok != getal: # start de gok loop
        if gok > getal: 
            print("Te hoog! Probeer nog een keer.")
        elif gok < getal:
            print("Te laag! Probeer nog een keer")
        gok = input("Jouw gok: ") # Loop de gok
        gok = int(gok)
        teller += 1
        print(f"Teller is nu {teller}")
        if teller > 10 and not aanmoediging_gegeven:
            print("Kom op, je kan het!")
            aanmoediging_gegeven = True

    print(f"Goed! Je hebt het geraden in {teller} keer")

    if teller <= 5:
        print("Lekker bezig!")
    elif teller > 10:
        print("Moeilijk!")
        
speel_spel()