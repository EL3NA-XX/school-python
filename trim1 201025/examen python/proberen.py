import random
import time

# insertion sort

def insertion_sort(lst):
    for i in range(1, len(lst)):
        k = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > k:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = k

groottes = [100, 200, 400, 800]
rondes = 3

print("Insertion Sort timing:")
for size in groottes:
    td = []
    for _ in range(rondes):
        testlijst = [random.randint(0, 1000) for _ in range(size)]
        start = time.perf_counter()
        insertion_sort(testlijst)
        einde = time.perf_counter()
        td.append(einde - start)
    gemiddelde = sum(td) / rondes
    print("Lijstgrootte: " + str(size) + ", Gemiddelde tijd: " + str(gemiddelde) + " sec")

# selection sort

def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]


print("Selection Sort timing:")
for size in groottes:
    tijden = []
    for _ in range(rondes):
        testlijst = [random.randint(0, 1000) for _ in range(size)]
        start = time.perf_counter()
        selection_sort(testlijst)
        einde = time.perf_counter()
        tijden.append(einde - start)
    gemiddelde = sum(tijden) / rondes
    print("Lijstgrootte: " + str(size) + ", Gemiddelde tijd: " + str(gemiddelde) + " sec")

