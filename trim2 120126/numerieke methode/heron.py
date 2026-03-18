def wortel(getal):
    if getal != 0:
        benadering = getal / 2
    else:
        benadering = 1
    vorige_benadering = 0
    iteraties = 0
    while benadering != vorige_benadering and iteraties < 100:
        vorige_benadering = benadering
        benadering = (benadering + getal / benadering) / 2
        iteraties += 1
    return benadering
print("wortel 4 is", wortel(4))
