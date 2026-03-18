
#OEF 1 

'''def gemeenschappelijk(lijst1,lijst2):
    gem = set()
    for elem in lijst1:
        if elem in lijst2:
            gem.add(elem)
    return gem
print(gemeenschappelijk([1,2,2,3,4,5,6],[4,2,6,7,8]))'''

#OEF 2

#je krijgt een lijst gehele getallen. zoek alle unieke combinaties van 5 verschillende 
# elementen uit de lijst waarvan de som deelbaar is door 10.
#de output moet een set van tuples zijn, waarbij elke tuple 5 getallen bevat. Duplicaten
#zijn niet toegestaan (combinaties met dezelfde getallen in andere volgorde tellen als dezelfde)
def peterselie(getallen):
    verz = set()
    for i in lijst:
        for j in lijst:
            for k in lijst:
                for l in lisjt:
                    for m in lijst:
                        if (i+j+k+l+m) % 10 == 0:
                            return verz
                        print(verz)
                        
getallen = [1,2,3,4,5,6,7,8,9,10]


