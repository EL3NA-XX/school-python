#Welkom op het eerste examen informaticawetenschappen
#Naam:
#daatum:
#klas:

#/////Je gebruikt op dit examen geen enkele ingebouwde functie (tenzij anders aangegeven)/////
#om je code te isoleren mag een extra tab openen in vs code.
#Als je klaar ben mag je het examen uploaden op smartschool

#Module 1
#VOOR DE OPGAVEN 1,3,7  MAAK JE EEN FLOWCHART 
#1.   schrijf een computerprogramma dat de temperatuur vraagt en print of je de verwarming moet aanzetten. 
    #Je zet de verwarming best aan bij een buitentemperatuur van minder dan 11 graden.
    #code:


#2.    Druk alle oneven getallen af van 1 tot en met 101.
#code:

#3.    maak een programma die aangeeft of je pizza vervallen is. Je pizza vervalt over 2 dagen. 
#Het programma vraagt hoeveel dagen je de pizza al bewaart en gaat dan aan de hand van je antwoord: 'eetbaar' of 'vervallen' printen
#code:


#4.    Definieer een functie berekenSomOneven(x) dat de som van alle oneven getallen van 1 tot en met x geeft.




#5.    Bij een online winkel mag je draaien aan een rad om te bepalen hoeveel korting je krijgt. 
#Schrijf een programma dat de gebruiker om zijn aankoopbedrag vraagt, dan een willekeurig korting tussen de 0% en 25% bepaald, en het nieuwe bedrag print. 
#Tips:
#Gebruik de module random om een willekeurige getal tussen de 0 en 25 te maken.




#6.    Schrijf een functie die controleert of een lijst een rekenkundige reeks is. Een rekenkundige reeks heeft een constant verschil tussen opeenvolgende getallen (bijvoorbeeld 2, 5, 8, 11 heeft steeds +3 als verschil).
#Stappen:
	#Input en Validatie: Vraag de gebruiker om een lijst met ten minste drie getallen.
	#Verschil berekenen: Bereken het verschil tussen de eerste twee getallen en controleer of dit verschil hetzelfde is voor alle opeenvolgende paren in de reeks.
	#Lus en controle: Gebruik een for-lus om elk paar te vergelijken en bepaal of de reeks rekenkundig is.
	#Output: Print een bericht of de reeks rekenkundig is of niet.

#Laat de functie het verschil printen als het een rekenkundige reeks is.



#7.    Schrijf een functie die een wachtwoord vraagt en controleert of het voldoet aan de criteria: 
# minstens 8 karakters, minstens één hoofdletter, en één cijfer. Geef feedback aan de gebruiker over wat nog ontbreekt.


#8:    Priemgetallen ontdekken.
#Je maakt een programma die aangeeft of het getal dat je ingegeven hebt een priemgetal is. Als het een priemgetal is zegt het programma: 
#“een priemgetal”. 
#Als het ingegeven getal geen priemgetal is, dan toont het programma een berekening die aangeeft waarom het geen priemgetal is (product).  
#Een priemgetal is een natuurlijk getal groter dan 1 die 1 en zichtzelf als deler heeft.
#code:


#Module 2


#9.    Reuzenbamboe is een van de snelst groeiende planten. Met de klas zetten we een experiment op om dit vast te stellen. 
#Op dag 1 planten we een stek van 2 cm. Af en toe meten we op hoe lang de plant is geworden. Bijvoorbeeld, op dag 3 is de plant 15 cm, op dag 7 al 25 cm, enz.
#Welke datastructuur gebruik je om de metingen bij te houden? Leg je keuze ook kort uit.



#10.   Implementeer het volgende scenario:

#op een dag beslist Anke om handtekeningen van bekende mensen te gaan verzamelen.

#In het begin is haar verzameling natuurlijk leeg.
#Dan krijgt ze van 'Pommelien' de eerste handtekening voor haar verzameling.
#Op vakantie in Engeland ontmoet ze 'Ed Sheeran'. Dat levert haar een nieuwe handtekening op.
#Weer thuis geeft ze de handtekening van 'Ed Sheeran' aan Elias.
#In ruil krijgt ze van Elias een handtekening van 'Miley Cyrus'.

# a. In het begin is haar verzameling natuurlijk leeg.
handtekeningen =
# b. Dan krijgt ze van `'Pommelien'` de eerste handtekening voor haar verzameling.
# c. Op vakantie in Engeland ontmoet ze `'Ed Sheeran'`. Dat levert haar een nieuwe handtekening op.
# d. Weer thuis geeft de ze handtekening van `'Ed Sheeran'` aan Elias.
# e. In ruil krijgt ze van Elias een handtekening van `'Miley Cyrus'`.
print(handtekeningen)



#11.   Sam gaat op reis met het vliegtuig en heeft daarvoor zijn tas gepakt. Bij de controle op de luchthaven houdt de douane hem tegen en zegt hem welke spullen hij mag meenemen op het vliegtuig.

#Schrijf een programma dat alle voorwerpen in tas overloopt. Print telkens het voorwerp als het niet in de verboden verzameling zit.

tas = ['mes', 'pen', 'papier', 'water', 'boterhammen', 'mes', 'pen']
verboden = {'mes', 'pistool', 'kruisboog', 'katapult', 'water'} 
# vul hier aan







#12.   De cafetaria heeft een aantal maaltijden bereid en in volgorde van populariteit gerangschikt. Wie eerst komt, krijgt de eerste maaltijd. Wie daarna komt de volgende, enzovoort.

#Ruifeng is dol op spaghetti en komt als eerste eten. Verwijder het eerste element uit de lijst.
#Jesse komt als tweede toe. Verwijder het nieuwe eerste element uit de lijst. Doe dit op een andere manier dan bij Ruifeng.
maaltijden = ['spaghetti', 'lasagne', 'witloof', 'spruitjes', 'lever met uitjes']
# 1. verwijder de eerste maaltijd
# 2. verwijder de nieuwe eerste maaltijd
print(maaltijden)





#13.   vervang de while-lus door een for-lus. Zorg dat je programma geen index meer gebruikt.
rassen = ['Bengaal', 'Britse korthaar', 'Maine Coon', 'Scottish fold', 'Sibeer', 'Siamees']
index = 0
while index < len(rassen):
   print(rassen[index])
   index += 1



#14.   Combineer meerdere concepten.
#Laat de gebruiker een lijst invoeren. bv [3,7,9,2,,1,8]
#Schrijf functies voor:
    #Het vinden van het grootste getal in de lijst.
    #Het tellen van het aantal even getallen in de lijst.
    #Het berekenen van het gemiddelde van de lijst.







#15.   Nero speelt poker. Hij heeft 5 kaarten getrokken en ze op kleur gesorteerd in de map kaarten. In het kaartspel zijn de kleuren niet rood en zwart, maar harten, ruiten, schoppen en klaveren.
#Voor elke kleur (harten, ruiten, schoppen, klaveren) waarvan Nero kaarten heeft, bevat de map een sleutel. De waarde bij elke kleur is een verzameling met de waarden van de kaarten in die kleur (1,...,10, boer, dame, heer).
#Schrijf de code die nagaat of Nero de harten dame in zijn hand heeft. Sla de waarde op in de variabele hartendame.
kaarten = {'harten': {1, 5}, 'ruiten': {7,'dame'}, 'schoppen': {'boer', 'heer'}}
hartendame = 
print(hartendame)


#16.    Schrijf een programma dat alle kaarten van een kaartendeck afdrukt.
#kleurLijst = ["Harten", "Schoppen", "Klaveren", "Ruiten"]
#waardeLijst = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Boer", "Vrouw", "Heer", "Aas"]


#17.    Schrijf een programma dat nagaat hoe vaak elke letter voorkomt in het woord voorbereidingswerkzaamheden. Sla het aantal op in de map letters.

woord = 'voorbereidingswerkzaamheden'
# In het begin is de map leeg.
letters =
for letter in woord:
  # vul aan

print(letters)


#18.   Schrijf een functie vertaal(woordenlijst,woordenboek) die een vertaling (in de vorm van een lijst) teruggeeft 
#van alle woorden in de woordenlijst aan de hand van het gegeven woordenboek (een map). 
#Indien een woord niet terug te vinden is in het woordenboek, wordt het niet meegenomen in de vertaling.



#19.   Janneke hield voor de maand Februari dagelijks bij hoeveel regen er gevallen is. 
#Wat was het meeste regen dat er op een dag gevallen was en op welke datum was dat? 
#Je moet hiervoor een of twee for-loops gebruiken.
#Aanwijzingen:
#             Doorloop de lijst met een for-loop en bepaal wat het meeste regen is dat er gevallen is.
#             Doorloop de lijst met een for-loop en zoek op welke index die voorkomt.
#             Pas de index aan naar een datum.
#regenlijst = [ 0, 10, 15, 20, 18, 15, 13, 14, 16, 34, 12, 10, 0, 0, 0, 1, 2, 0, 4, 8, 0, 0, 1, 2, 1, 10, 8, 1 ]


  
    

#20.   Maak een programma die een kerstboom print zoals in de les gezien. 
#Vraag a:
#Pas de functie zo aan dat de stam altijd even breed is, ongeacht de hoogte van de kerstboom. Bijvoorbeeld, als de hoogte van de kerstboom 5 is, moet de stam 4 sterretjes breed zijn. Maak de juiste aanpassing in de code.

#Vraag b:
#Voeg versiering toe aan de kerstboom! In plaats van alleen sterretjes, moeten de sterretjes worden afgewisseld met plustekens (+). Zorg ervoor dat de versiering alleen in de top van de boom komt, niet op de stam.


#21:   Schrijf een functie minstens(x,lijst,verz) die aangeeft of er minstens x elementen uit lijst in de verzameling verz zitten.
#Indien de lijst dubbele elementen bevat die in de verzameling zitten, dan tellen die voor twee! 
#Bijvoorbeeld,
#minstens(3,[1,2,3,4,5,1,4,2,1,5],{1,3,7}) == True

