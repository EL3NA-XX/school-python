breedte = 41
midden = breedte // 2
for i in range(0,8):
    regel = ""
    for j in range(breedte):
        if abs(j-midden)<=i:
            regel += "*"
        else:
            regel += " "
    print(regel)