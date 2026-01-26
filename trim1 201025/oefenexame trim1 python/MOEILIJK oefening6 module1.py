#6.    Schrijf een functie die controleert of een lijst een rekenkundige reeks is. 
# Een rekenkundige reeks heeft een constant verschil tussen opeenvolgende getallen (bijvoorbeeld 2, 5, 8, 11 heeft steeds +3 als verschil).
#Stappen:
	#Input en Validatie: Vraag de gebruiker om een lijst met ten minste drie getallen.
	#Verschil berekenen: Bereken het verschil tussen de eerste twee getallen en controleer of dit verschil hetzelfde is voor alle opeenvolgende paren in de reeks.
	#Lus en controle: Gebruik een for-lus om elk paar te vergelijken en bepaal of de reeks rekenkundig is.
	#Output: Print een bericht of de reeks rekenkundig is of niet.

#Laat de functie het verschil printen als het een rekenkundige reeks is.

def is_rekenkundige_reeks():
    aantal = int(input("Hoeveel getallen wil je ingeven? "))

    if aantal < 3:
        print("Minstens drie getallen aub.")
        return

    nums = []

    # getallen één voor één vragen
    for i in range(aantal):
        getal = float(input(f"Getal {i+1}: "))
        nums.append(getal)

    # basisverschil
    diff = nums[1] - nums[0]

    # vlag
    is_reeks = True

    # check differences
    for i in range(1, len(nums) - 1):
        if nums[i+1] - nums[i] != diff:
            is_reeks = False
            break  # kan stoppen als het al fout is

    # output
    if is_reeks:
        print("Yesss, rekenkundige reeks! Verschil =", diff)
    else:
        print("Nope, geen rekenkundige reeks.")

is_rekenkundige_reeks()

