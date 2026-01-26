
def minstens(x, lijst, verz):
    z = 0
    for e in lijst:
        if e in verz:
            z += 1
    return z >= x

print(minstens(3, [1, 2, 3, 4, 5, 1, 4, 2, 1, 5], {1, 3, 7}))





