def allemaal(lijst, verz):
    for elem in lijst:
        if elem not in verz:
            return False
    return True
print(allemaal([1,2,3],[1,2,3,4,5]))  # Verwachte output: True
print(allemaal([1,6,3],[1,2,3,4,5]))  # Verwachte output: False