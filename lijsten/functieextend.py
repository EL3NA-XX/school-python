def poke(rijst,proteine,groente):
  combo = []
  for r in lijst:
    for p in proteine:
      for ge in groente:
        combo.append([r,p,ge]) #dit is de tupel
    return combo   
print(poke['bruin', 'wit'], ['vlees', 'kip', 'ei'], ['sla', 'komkommer', 'tomaat'])

