"""Programma om de score bij te houden langs het voetbalveld"""

def keep_score():
    # Vraag welke teams er spelen.
    print("Geef de namen van het thuis en uit team")
    thuis_team = input("Wie speelt er thuis?: ")
    uit_team = input("Wie speelt er uit?: ")

    # Start het scorebord
    score_tt = 0
    score_ut = 0
    # Laat de beginstand zien
    tussenstand = f"{thuis_team}: {score_tt} - {uit_team}: {score_ut}"
    print(tussenstand)
    print("Bij doelpunt\nTyp 't' voor thuis\nTyp 'u' voor uit\nTyp 's' als de wedstrijd is afgelopen")

    # Vraag input als er een doelpunt is. Bij thuis is input "t". Bij uit doelpunt input "u"
    
    wedstrijd_bezig = True
    while wedstrijd_bezig:
        gescoord = False
        wie_scoort = input("Wie heeft er gescoord? ")
        if wie_scoort.lower() == "t":
            score_tt += 1
            gescoord = True
        elif wie_scoort.lower() == "u":
            score_ut += 1
            gescoord = True
        elif wie_scoort.lower() == "s":
            wedstrijd_bezig = False    
        else:
            print("Ongeldige invoer, probeer opnieuw")
        # Print de tussenstand alleen als er gescoord is
        if gescoord:
            tussenstand = f"{thuis_team}: {score_tt} - {uit_team}: {score_ut}"
            print(tussenstand)

    # Zeg wie er gewonnen heeft
    if score_tt == score_ut:
        print("Gelijkspel!")
    elif score_tt > score_ut:
        print(f"{thuis_team} heeft gewonnen met {tussenstand}!")
    else:
        print(f"{uit_team} heeft gewonnen met {tussenstand}!")
    totaal_doelpunten = score_tt + score_ut
    print(f"Het totaal aantal doelpunten is: {totaal_doelpunten}")

keep_score()
