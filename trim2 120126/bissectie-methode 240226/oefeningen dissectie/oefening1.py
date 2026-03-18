import numpy as np
import matplotlib.pyplot as plt

#DEEL 1: Tekenverandering zoeken
def f(x): 
    return x**3 - x - 2

x = np.linspace(-10, 10, 1000000)
y = f(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('grafiek van de functie')
plt.grid(True)
plt.show()

def bissectie_help(a, b):
    m = (a + b)/2
    if abs(a-b) < 1e-15:
        return m
    
    functiewaarde = f(m)
    if functiewaarde ==0:
        return m
    if functiewaarde < 0:
        return bissectie_help(m, b)
    if functiewaarde > 0:
        return bissectie_help(a, m)


def bissectie(a, b):
    functiewaarde_a = f(a)
    functiewaarde_b = f(b)
    if functiewaarde_a < 0 and functiewaarde_b > 0:
        return bissectie_help(a, b)
    elif functiewaarde_a > 0 and functiewaarde_b < 0:
        return bissectie_help(b, a)
    #als er geen tekenverandering is:
    else:
        return None
    
nulpunt = bissectie(-2, 2)
if nulpunt != None:
    print('x=', nulpunt, 'en f(x)', f(nulpunt))
else:
    print('geen tekenverandering, geen nulpunt gevonden')
    