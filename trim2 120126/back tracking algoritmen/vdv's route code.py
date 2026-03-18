voorbeeld_speelveld = [
  [8, 10, 6, 5, 3],
  [5, 8, -5, 3, -10],
  [0, 5, 14, 8, 22],
  [7, 7, 7, 7, 7],
  [3, 7, 12, 4, 5]
]

#backtracking
def beginpositie(speelveld):
    return (len(speelveld)-1,0)

def mogelijke_bewegingen(speelveld,positie):#positie = tupel
    breedte = len(speelveld[0])
    mogelijke_bewegingen = []
    if positie[0] -1 >= 0:
        mogelijke_bewegingen.append('omhoog')
    if positie[1] +1 < breedte:
        mogelijke_bewegingen.append('rechts')
   
    return mogelijke_bewegingen

def beweeg (positie, optie):
    if optie == 'omhoog':
        return (positie[0]-1, positie[1])
    elif optie == 'rechts':
        return (positie[0],positie[1]+1)

def punten_op_positie(speelveld,positie):
    return speelveld[positie[0]][positie[1]]

def is_beter(a,b):
    return a>b

def punten(speelveld, positie = None):
 
  if positie == None:
    positie = beginpositie(speelveld)            
  opties = mogelijke_bewegingen(speelveld, positie)
  beste_score = 0
  beste_bewegingen = []
  for optie in opties:
    nieuwe_positie = beweeg(positie, optie)
    (nieuwe_score, nieuwe_bewegingen) = punten(speelveld, nieuwe_positie)
    if is_beter(nieuwe_score, beste_score):
      beste_score = nieuwe_score
      beste_bewegingen = [optie] + nieuwe_bewegingen

  return (beste_score + punten_op_positie(speelveld, positie), beste_bewegingen)


print("De maximale score is", punten(voorbeeld_speelveld))
 