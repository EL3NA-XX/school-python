#Schrijf een Pythonfunctie f(x) die deze functie voorstelt (visueel).
#f(x)=x3−2x−5

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 2*x - 5

x = np.linspace(0, 7500000, 1000)
y = f(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('grafiek van de functie')
plt.grid(True)
plt.show()

def bissectie_shork(a, b):
    m = (a+b)/2
    if abs(a-b) < 1e-15:
        return m
    functiew = f(m)
    if functiew == 0:
        return m
    if functiew < 0:
        return bissectie_shork(m, b)
    if functiew > 0:
        return bissectie_shork(a, m)
    
def bissectie(a, b):
    functiew_a = f(a)
    functiew_b = f(b)
    if functiew_a < 0 and functiew_b > 0: 
        return bissectie_shork(a, b)
    elif functiew_a > 0 and functiew_b < 0:
        return bissectie_shork(b, a)
    else:
        return None

#geef nu de nulpunten zoals gezien in de les.

nulpunt = bissectie(-1, 1) 
if nulpunt != None:
    print('x=', nulpunt, 'en f(x)', f(nulpunt))
else:
    print('geen nulpunt gevonden')

#shork 
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣷⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣳⡄⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀blub ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠠⠄⠂⣉⠍⠛⢠
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠲⣶⠒⠓⠒⠒⠤⠐⠈⢀⣤⣤⠊⠁⠁⠀⠸
#⠀⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡄⠀⠀⠀⠀⡀⠀⠘⡿⠋⣀⢤⣲⠶⡆
#⠀⢹⡿⢷⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠈⢇⠱⠀⡈⠀⠸⢿⣹⣷⡿⠀
#⠀⠀⢷⠀⠑⢄⠀⢀⠾⠷⠄⠔⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⢀⠂⠀
#⠀⠀⣨⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡌⠀⠀⠀⢀⠔⠁⡁⠀
#⠐⠯⠤⠤⠔⠒⠤⣀⣀⡀⠀⣀⡄⡄⠀⠀⠀⢹⠁⢀⡠⠔⠓⢄⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠰⠇⠚⠁⠀⡄⠀⠀⢠⠞⠉⠁⠀⠀⠀⠀⠋⠀⠀
#⠀⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⢡⡀⣤⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⣴⣦⠈⢁⠀⠀⠀⠀⠀⠀⠀⠘⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠰⢿⠇⠀⠀we love the internet⠀⠀

#Benadering van pi via Monte Carlo
#MONTE CARLO??? WHAT??? i don't rmbr that guy
#Leg in een commentaar in je code kort uit waarom: π≈4⋅punten in cirkel/totaal

#... ja fuck

# schrijf dan nu een functie die een schatting van pi geeft
# willekeurige punten  in het vierkant in interval [-1,1] × [-1,1]

#khoop nu zo hard da je het hierover hebt, ik herriner me alleen dit nog
#ma wie is monte carlo, da klinkt als een berg

#telt hoeveel punten in de cirkel liggen
# een benadering van π teruggeeft
import random
#bepaling of punt (x, y) in de cirjel zin (en mdidelpunt 0,0 is)
def in_circle(x, y):
    a = x**2 +y**2
    return a < 1
#coördinaten willekeurig punt in een vierkant met een zijde van deux en middelpunt (zero, zero)
#...en dit is een functie, moest dit relevante informatie zijn
def random_shark():
    x = random.random() *2 - 1
    y = random.random() *2 - 1
    return x, y
repeat = 10000 
amount_in_circle = 0
for i in range(repeat):
    x, y = random_shark() 
    if in_circle(x, y):
        amount_in_circle +=1
blahaj = amount_in_circle/repeat
#blähaj (= haai in het zweeds, denk ik)
print('kans = ', blahaj)
print('pi = ', 4*blahaj)

#uh... ok dus me code werkt ni echt.... NVM HIJ WERKT
#dit is alles wat ik nog weet, dus uhm, eig ben ik lowk wel trots op mezelf