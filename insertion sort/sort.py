# Insertion Sort in Python

def insertion_sort(array):
    """
    Sorteert de array in oplopende volgorde met Insertion Sort.
    """
    # Begin bij index 1 (niet 0)
    for i in range(1, len(array)):
        # Tijdelijke variabele voor de huidige waarde
        temp = array[i]
        
        # j wijst naar het element links van i
        j = i - 1
        
        # Verschuif elementen naar rechts zolang ze groter zijn dan temp
        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j -= 1
        
        # Plaats temp op de juiste positie
        array[j + 1] = temp

# Hoofdfunctie
if __name__ == "__main__":
    # Maak een array van integers
    array = [9, 1, 8, 2, 7, 3, 6, 5, 4]
    
    # Toon de array voor het sorteren
    print("Voor sorteren:", *array)
    
    # Roep de insertion sort functie aan
    insertion_sort(array)
    
    # Toon de array na het sorteren
    print("Na sorteren: ", *array)

