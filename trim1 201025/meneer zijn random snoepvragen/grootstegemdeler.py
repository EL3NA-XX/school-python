#maak een functie die de grootste gemeenschappelijke deler van twee getallen a en b
#algoritme van eucledes
import math
def ggd(a ,b): # != betekend "verschillend van"
    while a != b:
        if a > b:
            a-=b
        else:
            b-=a
    return a
print(ggd(6, 12))
    