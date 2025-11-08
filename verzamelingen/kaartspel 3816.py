
def kaartspel(getallen, kleuren):
    a = set()
    for i in getallen:
        for j in kleuren:
            a.add((i,j))
    return a
print(kaartspel({'A',2,3,4,5,6,7,8,9,10,'B','V','H'},{'♥','♣','♠','♦'}))  

#verschill tussen tuple en lijst is da een tuple onveranderlijk is, een lijst kanj aanpasse met append, ...
