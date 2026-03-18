import random
import time

lijst = [random.randint(0, 1000000) for i in range(1000)]


def quicksort(lst):
    if len(lst) <= 1:
        return lst
    
    pivot = lst[len(lst)//2]
    kl = []
    gr = []
    gl = []

    for e in lst:
        if e < pivot:
            kl.append(e)
        elif e > pivot:
            gr.append(e)
        else:
            gl.append(e)

    return quicksort(kl) + gl + quicksort(gr)

lijst_sorted = quicksort(lijst)

bt = time.perf_counter()
et= time.perf_counter()
print ('time it took to sort list: ', et-bt)

print('sorted list: ', lijst_sorted[:20])  