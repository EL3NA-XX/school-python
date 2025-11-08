#lijsten= datastructuren waarbij de volgorde heel belangrijk is, en het element hoeft niet uniek te zijn.

'''klaslijst = ["mats","nicholas","ibe","elena","alek", "lukaz", "alexander"]'''

#klaslijst.append("joke") voegt een element toe aan het einde van de lijst (MAAR DAS VR 1)
#klaslijst.extend(["joke", "jeffry"])   voegt meerdere elementen toe aan het einde van de lijst
#ittereren = ieder element appart bekijken in de lijst
#i is nu een element in de klaslijst

'''def extend(lijst1, lijst2): #voegt lijst2 toe aan lijst1
    for i in lijst2:
        lijst1.append(i) #plakt 1 element
    return lijst1'''


'''klaslijst = ["mats","nicholas","ibe","elena","alek", "lukaz", "alexander"]
klaslijst.insert(4,'sander')  #instert voegt een element toe
print(klaslijst)

def insert(lijst, index, element):
    nieuw= [] #we maken ee nieuwe lijst aan
    for i in range(len(lijst)): #range = bereik 
        if i == index: #als i gelijk gesteld wordt aan bv een naam uit de lijst (dus soort van de plaats waant wnr j (4,sander)  -
            #had werd sander op plaats 4 geplaatst en dan wordt die element daar toegevoegd
            nieuw.append(element) 
        nieuw.append(lijst[i]) #het nieuw element wordt toegevoegd
    if index >= len(lijst):
        nieuw.append(element)
    return nieuw'''

klaslijst = ["mats","nicholas","ibe","elena","alek", "lukaz", "alexander"]
klaslijst.insert(4,'sander')  #instert voegt een element toe
klaslijst.reverse()
def reverse(lijst):
    nieuw = []
    for i in range(len(lijst), -1):
        nieuw.append(lijst[i-1])
    return nieuw
print(klaslijst)

#tupel = meerdere elementen schrijven door een komma