
#Schrijf een programma dat het grootste getal uit de lijst vindt (zonder max() te gebruiken).

lijst = [12, 45, 3, 67, 23, 9]

def vind_max(lijst):
    grootste = 0
    for i in range(len(lijst)):
        if lijst[i] > grootste: #lijst[i] is om de waarde op die index te krijgen
            grootste = lijst[i]
    return grootste
print(vind_max(lijst))