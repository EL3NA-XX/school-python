import numpy as np
import matplotlib.pyplot as plt

def  f(x):
    return x**2 - 7500000 * x + 1.5

x = np.linspace(0, 7500000, 1000)
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

#voorwaarde om te starten: pas starten bij een tekenverandering

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

#test:
nulpunt = bissectie(-1, 1)
if nulpunt != None:
    print('x=', nulpunt, 'en f(x)', f(nulpunt))
else:
    print('geen tekenverandering, geen nulpunt gevonden')
    