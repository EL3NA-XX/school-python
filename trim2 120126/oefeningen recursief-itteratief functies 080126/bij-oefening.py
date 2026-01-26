#Wiskundig kan je dit schrijven als 𝑓(𝑛)=𝑓(𝑛−1)+𝑓(𝑛−2) met 𝑓(0)=1 en 𝑓(1)=1.

def bijen(n):
    if n == 0 or n == 1:
        return 1
    return bijen(n-1) + bijen(n-2)
print(bijen(6))


