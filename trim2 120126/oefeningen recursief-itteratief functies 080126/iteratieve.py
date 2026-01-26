''''
def fac(n):
    resultaat = 1
    for i in range(1, n+1):
        resultaat *=i
    return resultaat
print(fac(5))
'''

def prod(lst):
    if len(lst) == 0:
        return 1
    return lst[0] * prod(lst[1:])

l = [95, 85, 21, 44]
print(prod(l))  # prints 7461300

#Iteratieve functie 
#Wat: Gebruikt lussen (for/while) en verandert variabelen stap voor stap.
#Voordeel: Meestal efficiënter qua geheugen en snelheid.
