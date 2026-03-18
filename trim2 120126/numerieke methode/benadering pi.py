import random 
#bepaling of het punt (x, y) in de cirkel zit
#middelpunt is (0, 0)
def in_cirkle(x, y):
    a = x**2+y**2
    return a < 1
#deze functie geeft de coördinaten van een willekeurig punt in het 
# vierkant met zijde 2 en middelpunt (0, 0)
def wil_p():
    x = random.random() *2 - 1
    y = random.random() *2 -1
    return x,y

herhalingen = 10000000
aant_in_cirk =  0
for i in range(herhalingen):
    x,y = wil_p()
    if in_cirkle(x, y):
        aant_in_cirk += 1
kans = aant_in_cirk/herhalingen
print('kans is ', kans)
print('pi is ', 4*kans)
