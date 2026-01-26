#maak een functie vervang(woord) die de letter 's' omzet naar hoofdletter'S'
def vervang(woord):
    resultaat = "" #hij is leeg en op het einde geven we een woord als parameter
    for letter in woord:
        if letter == 's': #bij if's altijd é isgelijkaans, dus "=="
            resultaat += 'S' # += is hetzelfde als resultaat = resultaat + 'S'
            #we gebruiken hier +=  bij resultaat omdat we de letter willen toevoegen aan het resultaat
        else:
            resultaat += letter #we gebruiken += omdat we de letter willen toevoegen aan het resultaat
    return resultaat
print (vervang('succes')) #hier kan je je woord ingeven en wordt s vervangen door S

