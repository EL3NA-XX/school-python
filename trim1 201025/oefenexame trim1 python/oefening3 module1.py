#3.    maak een programma die aangeeft of je pizza vervallen is. Je pizza vervalt over 2 dagen. 
#Het programma vraagt hoeveel dagen je de pizza al bewaart en gaat dan aan de hand van je antwoord: 'eetbaar' of 'vervallen' printen
#code:

a = int(input("hoeveel dagen bewaar je je pizza al? "))
if a > 2:
    print("je pizza is al vervallen")
else: 
    print("je pizza is nog niet vervallen, eet hem snel op zolang die nog eetbaar is. ")