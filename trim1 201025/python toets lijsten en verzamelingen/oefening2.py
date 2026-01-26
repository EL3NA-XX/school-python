
lijst = [2, 15, 25]

def ov(lijst):
    for i in range(len(lijst) - 1, -1, -1):
        print(lijst[i])
    return lijst
print(ov(lijst))


