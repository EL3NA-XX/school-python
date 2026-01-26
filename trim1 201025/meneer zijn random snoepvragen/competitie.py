hoogte = 7
breedte = 5

# maak elke letter in een lijst (1 string per rij)

# D
D = []
for rij in range(hoogte):
    line = ""
    for kolom in range(breedte):
        if kolom == 0 or (rij == 0 or rij == hoogte-1) and kolom < breedte-1 or kolom == breedte-1 and rij != 0 and rij != hoogte-1:
            line += "* "
        else:
            line += "  "
    D.append(line)

# I
I = []
for rij in range(hoogte):
    line = ""
    for kolom in range(1):   # kolom=0 → gewoon 1 kolom breed
        line += "* "
    I.append(line)

# nog een D
D2 = D.copy()

# nog een D
D3 = D.copy()

# Y
Y = []
for rij in range(hoogte):
    line = ""
    for kolom in range(hoogte):
        if (rij == kolom and rij < hoogte // 2) or (rij + kolom == hoogte - 1 and rij < hoogte // 2):
            line += "* "
        elif rij >= hoogte // 2 and kolom == hoogte // 2:
            line += "* "
        else:
            line += "  "
    Y.append(line)

# Zet alles naast elkaar
letters = [D, I, D2, D3, Y]

for rij in range(hoogte):
    for letter in letters:
        print(letter[rij], end="   ")  # spaties tussen letters
    print()
    
