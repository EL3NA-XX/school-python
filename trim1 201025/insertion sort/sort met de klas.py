import time
import random

def insert_sort(lst):
    for i in range(1, len(lst)):
        sleutel = lst[i]
        j = i-1

        while j >= 0 and lst[j] > sleutel:
            lst[j+1] = lst[j] #dit is gewoon wisselen van plaats
            j -= 1 
        lst[j+1] = sleutel
    return lst
lst = [random.randint(0, 1_000_000) for i in range(10_000)]

starttijd1 = time.perf_counter() #zorgt r vr da we tot de nanoseconden kunnen gaan
resultaat1 = insert_sort(lst)
eindtijd1 = time.perf_counter()
print('gesorteerde lijst', resultaat1)
print('tijd', eindtijd1-starttijd1)


