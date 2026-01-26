def gemeenschappelijk(lijst1,lijst2):
    gem = set()
    for elem in lijst1:
        if elem in lijst2:
            gem.add(elem)
    return gem
print(gemeenschappelijk([1,2,3],[1,2,3,4]))