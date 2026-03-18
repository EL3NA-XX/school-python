def palindroom(woord):
    if len(woord) <= 1:
        return True
    return woord[0] == woord[-1] and palindroom(woord[1:-1])

print(palindroom("lepel")) 
