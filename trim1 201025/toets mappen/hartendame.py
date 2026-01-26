#Nero speelt poker. Hij heeft 5 kaarten getrokken en ze op kleur gesorteerd in de map kaarten. In het
#kaartspel zijn de kleuren niet rood en zwart, maar harten, ruiten, schoppen en klaveren.

#Voor elke kleur (harten, ruiten, schoppen, klaveren) waarvan Nero kaarten heeft, bevat de map een sleutel.
#De waarde bij elke kleur is een verzameling met de waarden van de kaarten in die kleur (1, ... ,10, boer, dameheer).
#Schrijf de code die nagaat of Nero de harten dame in zijn hand heeft. Sla de waarde op in de variabele hartendame.

kaarten = {'harten': {1, 5}, 'ruiten': {7,'dame'}, 'schoppen': {'boer', 'heer'}}
hartendame = {}
if 'harten' in kaarten:
    if 'dame' in kaarten['harten']:
        hartendame = True
    else:
        hartendame = False 
return hartendame
print(hartendame)