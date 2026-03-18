# gegeven is een dictionary waarin de sleutels de namen van studenten zijn, en de waarde hun cijfers. Je programma moet:
# 1) de gemiddelde score berekenen.
# 2) de student met het hoogste cijfer tonen.
# 3) de studenten met het laagste cijfer tonen.

studenten = {"Emma": 8.5, "Lars": 7.2, "Sara": 9.0, "Noah": 6.8}

# gemiddelde score berekenen
totaal_cijfers = sum(studenten.values())
aantal_studenten = len(studenten)
gemiddelde_score = totaal_cijfers / aantal_studenten
print('De gemiddelde score is', gemiddelde_score)

# de student(en) met het hoogste cijfer tonen
# de student(en) met het hoogste cijfer tonen
#de studenten met het hoogste cijfer tonen
hoogste_cijfer = max(studenten.values())
studenten_hoogste = []
for naam in studenten:
    if studenten[naam] == hoogste_cijfer:
        studenten_hoogste.append(naam)
print("Student met het hoogste cijfer is", studenten_hoogste, "met een score van", hoogste_cijfer)
# de studenten met het laagste cijfer tonen
laagste_cijfer = min(studenten.values())    

studenten_laagste = []
for naam in studenten:
    if studenten[naam] == laagste_cijfer:
        studenten_laagste.append(naam)              
print("Student met het laagste cijfer is", studenten_laagste, "met een score van", laagste_cijfer)  
