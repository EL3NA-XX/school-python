
#Vervang elk element door het dubbele van zijn waarde. 
# Na afloop moet de lijst [4, 8, 12, 16] zijn.

getallen = [2, 4, 6, 8]

def duplicaten(getallen):
    nieuw = []
    for i in getallen:
        nieuw.append(i*2)
    return nieuw    
print(duplicaten(getallen))

