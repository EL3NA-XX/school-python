import math 
def omtr_ingeschreven(n):
    return n* math.sin(math.radians(180/n))
def omtr_omgeschreven(n):
    return n* math.tan(math.radians(180/n))
n = 3
while n < 100:
    print ('bij', n, 'hoeken ligt pi tussen', omtr_ingeschreven(n), 'en', omtr_omgeschreven(n))
    n*=2