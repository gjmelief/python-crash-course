"""Tweede Python Oefening: Eenvoudige Rekenmachine
Bouw een eenvoudige rekenmachine die het volgende doet:
Opdracht:
Vraag de gebruiker om twee getallen
Vraag de gebruiker welke bewerking ze willen doen (+, -, *, /)
Voer de berekening uit en toon het resultaat
Vraag of ze nog een berekening willen doen
Blijf herhalen totdat ze 'nee' zeggen
Concepten die je gebruikt:
Variabelen
Input van de gebruiker
While loops
If/else statements (voor de verschillende bewerkingen)
Print statements
Vergelijkingsoperatoren
Extra uitdaging: Zorg ervoor dat je programma niet crasht als iemand door nul probeert te delen!"""

def calculator():
    print("Dit is een rekenmachine\nGeef eerst twee getallen op.\nEn hierna de bewerking +, -, *, /\nDelen door 0 mag niet\n") # Uitleg voor de gebruiker

    gebruiker_klaar = False

    while gebruiker_klaar == False: # Flag om te controleren of gebruiker klaar is
        # Vraag om de te berekenen getallen
        getal1 = input("Getal 1: ")
        getal2 = input("Getal 2: ")

        # Vraag om de bewerking
        bewerking = input("Welke bewerking? ")

        # converteer alle input naar floats
        getal1 = float(getal1)
        getal2 = float(getal2)

    # Voer de bewerking uit
        if bewerking == "+":
            antwoord = getal1 + getal2
            # Laat het antwoord zien
            print(f" Het antwoord is: {antwoord}!")
        elif bewerking == "-":
            antwoord = getal1 - getal2
            # Laat het antwoord zien
            print(f" Het antwoord is: {antwoord}!")
        elif bewerking == "*":
            antwoord = getal1 * getal2
            # Laat het antwoord zien
            print(f" Het antwoord is: {antwoord}!")
        elif bewerking == "/" and getal2 == 0:
            print("Kan niet delen door nul!")
        elif bewerking == "/":
            antwoord = getal1 / getal2
            # Laat het antwoord zien
            print(f" Het antwoord is: {antwoord}!")
        else:
            print("Foutieve bewerking!")

        doorgaan = input("Nog een som? Ja of Nee ")
        if doorgaan == "Nee":
            gebruiker_klaar = True
        else:
            gebruiker_klaar = False
    
calculator()