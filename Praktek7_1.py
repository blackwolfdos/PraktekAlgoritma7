bilangan = float(input("angka: "))

def CekPrima(x):
    pembagi = 2
    
    if x == 1:
        return False
    while pembagi < x:
        if x % pembagi == 0:
            return False
        pembagi+=1
    return True

def Output(y):
    if CekPrima(y) == False:
        print("Bukan bilangan prima")
    else:
        print("Adalah bilangan prima")
        
Output(bilangan)