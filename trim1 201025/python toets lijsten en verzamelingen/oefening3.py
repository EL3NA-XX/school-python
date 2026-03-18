#uh ja dus j kan zo de lijst aanpasse
lijst = [3, 7, 9, 2, 1, 8]

# A het vinden van de grootste getal in de lijst
def gg(lijst):
    for i in range(len(lijst)):
        if i == 0:
            gr = lijst[i]
        elif lijst[i] > gr:
            gr = lijst[i]
    return gr
print("Het grootste getal in de lijst is:", gg(lijst))


# B Het tellen van het aantal even getallen in de lijst
def aeg(lijst):
    a = 0
    for i in range(len(lijst)):
        if lijst[i] % 2 == 0:
            a += 1
    return a
print("Het aantal even getallen in de lijst is:", aeg(lijst))


# C het berekenen van het gemiddelde van de lijst
def g(lijst):
    som = 0
    for i in range(len(lijst)):
        som = som + lijst[i]
        g = som / len(lijst)
    return g
print("Het gemiddelde van de lijst is:", g(lijst))




