def som(n, getallen): #som moet 6 zijn van de tupels
    verz = set()
    for i in getallen: 
        for j in getallen:
            if i + j == n:
                verz.add((i,j))
    return verz
print(som(6, {1,2,3,4,5}))
