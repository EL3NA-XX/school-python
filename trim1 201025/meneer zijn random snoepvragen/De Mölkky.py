score = 0 
misses = 0

# De Mölkky
while True:
    print('hoeveel blokjes heb je omgegooid? ')
    aantal = int(input())
    if aantal == 0:
        misses += 1
        if misses == 3:
            print('je hebt 3 keer gemist, je score is', score, 'je verliest!')
            break
        else:
            print('je hebt gemist, je hebt nu', misses, 'misses')
    elif aantal > 50:
        score = aantal / 2
    else:
        score += aantal
    

