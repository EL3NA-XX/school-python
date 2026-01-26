#random sort

def is_gesorteerd(lijst):
    for i in range(1,len(lijst)): #er staat "1," omdat je met index 1 begint
        if lijst [i] < lijst[i-1]: #als het huidige element kleiner is dan het vorige element
            return False 
    return True 


#functiewissel

def wissel(lijst, index1, index2):
    tmp = lijst[index1]  #tmp is "tijdelijk"
    lijst[index1] = lijst[index2]
    lijst[index2] = tmp #kdenk dak hier later uitleg over moet opzoeken

from random import randint #randint is voor random getallen
def willekeurige_indexen(rij):
    return(randint(0, len(rij)-1), randint(0, len(rij)-1)) #komma omda die een tuple wil weergeve


#nu gaan we weer naar het sorteer gedeelte

def random_sort(rij):
    teller = 0 
    while not is_gesorteerd(rij):
        indexen = willekeurige_indexen(rij)
        wissel(rij, indexen[0], indexen[1])
        teller += 1
    print('gesorteerd na', str(teller) + ' willekeirige wissels')
    return rij 
print(random_sort([3,6,1,9]))


#selection sort

def selection_sort(lst): #lst is lijst
    for i in range(len(lst)-1):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst [min_index]:
                if lst[j] < lst[min_index]:
                    min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst
print(selection_sort([64, 25, 12, 22, 11]))

