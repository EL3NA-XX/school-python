# BELANGRIJKE OEFENING
'''
def geordend(lijst):
    for i in range(len(lijst)-1): #je gebruikt -1 om met het volgend element te vergelijken
        if lijst[i]<lijst[i+1]:
            return False
    return True
lijst= [5,9,3,2,1]
print(geordend(lijst))'''

'''#MAG GEEN DUPLICATEN BEVATTEN
def duplicaten(lijst):
    nieuw = []
    for i in lijst:
        if i not in nieuw: #als i niet in nieuw zit, voeg het toe
            nieuw.append(i)
    return nieuw    
print(duplicaten(lijst))  

lijst = [1,1,2,3,4,4,5,3]'''

lijst = ['j','o','n','a','s']
def woorden(tekens):
  woord = ''
  for i in tekens