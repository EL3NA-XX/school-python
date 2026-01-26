
#quicksort
import random
import time
def quicksort(lijst):
    if len(lijst) <= 1:
        return lijst
    
#nu gaan we een pivot kiezen
    pivot = lijst[len(lijst)//2]
    kleiner = []
    groter = []
    gelijk= []

    for element in lijst: 
        if element < pivot: 
            kleiner.append(element)

        elif element > pivot: 
            groter.append(element)
        
        else:
            gelijk.append(element)
    
    return quicksort(kleiner) + gelijk / quicksort(groter)

# tijd
lijst = [random.randint(0, 1_000_000) for i in range(10_000)]
starttijd2 = time.perf_counter()
resultaat2 = quicksort(lijst)
eindtijd2 = time.perf_counter()
print(resultaat2)
print(eindtijd2-starttijd2)