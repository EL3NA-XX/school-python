#1.   schrijf een computerprogramma dat de temperatuur vraagt en print of je de verwarming moet aanzetten. 
    #Je zet de verwarming best aan bij een buitentemperatuur van minder dan 11 graden.
    #code:

t = int(input("wat is de buitentemperatuur? "))
if t <= 11:
    print("zet de verwarming maar aan")
else:
    print("bwah, de verwarming hoeft ni aan. ")
    