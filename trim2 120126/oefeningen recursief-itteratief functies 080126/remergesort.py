def mergesort(lst):
    if len(lst) <= 1:
        return lst
    m = len(lst) // 2 
    left_half = mergesort(lst[:m])
    right_half = mergesort(lst[m:]) #gwn de ":" verzetten
    return merge(left_half, right_half)

def merge(left, right):
    merged = [] #VERGEET GEEN NEIWUE LIJST AAN TE MAKE
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
print(mergesort([38, 27, 43, 3, 9, 82, 10]))

