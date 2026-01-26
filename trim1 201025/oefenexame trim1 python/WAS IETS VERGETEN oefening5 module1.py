#5.    Bij een online winkel mag je draaien aan een rad om te bepalen hoeveel korting je krijgt. 
#Schrijf een programma dat de gebruiker om zijn aankoopbedrag vraagt, dan een willekeurig korting tussen de 0% en 25% bepaald, en het nieuwe bedrag print. 
#Tips:
#Gebruik de module random om een willekeurige getal tussen de 0 en 25 te maken.

import random

a = int(input("wat is jouw aankoopbedrag? "))
b = random.randint(0, 25)
korting = a * (b/100) #dit is hoe j er procent van maakt
korting = round(korting, 2) #niet vergeten dat dit een mogelijkheid is 
print("je hebt €", korting, "korting")