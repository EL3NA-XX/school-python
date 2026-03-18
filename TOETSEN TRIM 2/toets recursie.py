# Opdracht: Schrijf een recursieve functie som(n) die de som berekent van alle getallen van 1 tot en met n.

def som(n):
    if n == 1:
        return 1
    else:
        return n + som(n-1)
print("functie som:", som(5))

# Geef de iteratieve en recursieve functie van de Fibonacci reeks

def fibo_iter(n):
    a, b = 0, 1
    for _ in range(n): 
        a, b = b, a + b
    return a
print("fibonacci reeks iteratief: ", fibo_iter(8)) 

def fibo_recur(n):
    if n <= 1:
        return n
    else:
        return fibo_recur(n-1) + fibo_recur(n-2)
print("fibonacci reeks recursief: ", fibo_recur(8))



# Ali en Bob spelen een spel met n lucifers op tafel. Ze zijn om beurt aan zet.

# Als Ali aan de beurt is, neemt hij een lucifer weg en geeft hij de beurt aan Bob.
# Als Bob aan de beurt is, zorgt hij dat het overblijvende aantal lucifers even is door er 1 of 2 weg te nemen. Dan geeft hij de beurt aan Ali.
# De speler die geen lucifer meer weg kan nemen, verliest het spel.

# Implementeer dit spel in de functies speel_ali(n) en speel_bob(n). Zorg ervoor dat er een string van de vorm Ali wint! of Bob wint! wordt geprint.

def luci(n):
    def ali(n):
        if n == 0:
            return "Ali wint"
        else:
            return bob(n - 1)

    def bob(n):
        if n == 0:
            return "Bob wint"
        elif n % 2 == 0:
            return ali(n - 2)
        else:
            return ali(n - 1)
    return ali(n)
print("lucifer spel: ", luci(1)) # bij 1 wint bob, voor de rest ali denk ik, geen idee of dat klopt :/

# \(°-°)/ 
#   |_| 
#  _| |_

# geef het algo van binair zoeken of merge sort. Je mag kiezen

def merge_sort():
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(a):
        if len(a) <= 1:
            return a
        mid = len(a) // 2
        left = sort(a[:mid])
        right = sort(a[mid:])
        return merge(left, right)
    return sort
print("merge sort: ", merge_sort()([6, 7, 2, 4, 3, 5, 1]))


