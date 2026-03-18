voorbeeld_speelveld = [
    [8,10,6,5,3],
    [5,8,-5,3,-10],
    [0,5,14,8,22],
    [7,7,7,7,7],
    [3,7,12,4,5]
]

#backtracking
def beginpositie(speelveld):
    return (len(speelveld)-1,0)

def mogelijke_bewegeingen(speelveld,positie):#positie = tupel
    breedte = len(speelveld[0])
    mogelijke_bewegeingen = []
    if positie[0] -1 >= 0:
        mogelijke_bewegeingen.append('omhoog')
    if positie[1] +1 < breedte:
        mogelijke_bewegeingen.append('rechts')
   
    return mogelijke_bewegeingen

def beweeg (positie, optie):
    if optie == 'omhoog':
        return (positie[0]-1, positie[1])
    elif optie == 'rechts':
        return (positie[0],positie[1]+1)

def punten_op_positie(speelveld,positie):
    return speelveld[positie[0]][positie[1]]

def is_beter(a,b):
    return a>b

def punten (speelveld, positie = None):
    #begintoestand initialiseren
    if positie == None:
        positie = beginpositie(speelveld)

    #mogelijke opties
    opties = mogelijke_bewegeingen(speelveld,positie)

    #startvariabele score
    beste_score = 0
    #proberen elke optie
    for optie in opties:
        nieuwe_positie = beweeg(positie,optie)
        nieuwe_score = punten(speelveld,nieuwe_positie)
        if is_beter(nieuwe_score,beste_score):
            beste_score = nieuwe_score

    return beste_score + punten_op_positie(speelveld,positie)


print("De maximale score is", punten(voorbeeld_speelveld))
 