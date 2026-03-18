
regenlijst = [ 0, 10, 15, 20, 18, 15, 13, 14, 16, 34, 12, 10, 0, 0, 0, 1, 2, 0, 4, 8, 0, 0, 1, 2, 1, 10, 8, 1 ]

for i in range(len(regenlijst)):
    if i == 0: 
        mr = regenlijst[i] 
        dag = i + 1
    elif regenlijst[i] > mr:
        mr = regenlijst[i] 
        dag = i + 1
print("op dag", dag, "viel er het meeste regen met een hvl'heid van", mr, "mm.")

