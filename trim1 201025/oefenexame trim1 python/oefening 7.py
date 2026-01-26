#7.    Schrijf een functie die een wachtwoord vraagt en controleert of het voldoet aan de criteria: 
# minstens 8 karakters, minstens één hoofdletter, en één cijfer. Geef feedback aan de gebruiker over wat nog ontbreekt.

def controleer_wachtwoord():
    ww = input("Voer hier je wachtwoord in: ")

    heeft_hoofdletter = False
    heeft_cijfer = False

    if len(ww) < 8:
        print("Te kort")

    for letter in ww:
        if letter.isupper():
            heeft_hoofdletter = True
        if letter.isdigit():
            heeft_cijfer = True

    if not heeft_hoofdletter:
        print("Geen hoofdletter")
    if not heeft_cijfer:
        print("Geen cijfer")

    if len(ww) >= 8 and heeft_hoofdletter and heeft_cijfer:
        print("Goed wachtwoord")


controleer_wachtwoord()
