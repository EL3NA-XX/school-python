

'''import random
klaslijst = ["mats","nicholas","ibe", "alexander"]
getal= random.choice(klaslijst) 
print (getal)'''


def koningen(namen, nummers):
    nieuw = []
    for i in namen:
        for j in nummers:
            nieuw.append(i + ' ' + j)
    return nieuw
print(koningen(['mats','nicholas','ibe'], ['1','2','3']))
