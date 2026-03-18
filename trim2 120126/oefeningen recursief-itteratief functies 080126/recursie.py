'''
def fac(n):
    if n == 1:
        return 1
    return n* fac(n-1)
print (fac(5))'''

#Recursieve functie 
#Wat: Roept zichzelf aan met kleinere of eenvoudigere argumenten; heeft altijd een basisgeval en een recursief geval.
#Voordeel: Vaak eleganter voor bomen, divide-and-conquer en wiskundige definities.
#Nadeel: Meer stapelgeheugen (call stack); Python ondersteunt geen tail-call optimalisatie.


#bevat in een lijst
'''
namen = ['a', 'b', 'c']
print('a' in namen)

def bevat(lijst, element):
    for i in range(len(lijst)):
        lijst_element =lijst[i]
        if lijst_element == element:
            return True
        def bevat_recursief(lijst, element):
            if len(lijst) == 0:
                return False
            if lijst[0] == element:
                return True
            return bevat_recursief(lijst[1:], element)
    return False
print( bevat_recursief(namen, 'a'))  #True
print( bevat_recursief(namen, 'x'))  #False
'''

#veel efficienter is de binaire zoekmethode
namen = ['a', 'b', 'c']
def zoek_binair(lijst, element):
    if len(lijst) == 0:
        return False

    mid = len(lijst)//2
    if lijst[mid] == element:
        return True
    elif lijst[mid] < element:
        return zoek_binair(lijst[mid+1], element)
    else:
        return zoek_binair(lijst[:mid], element)
