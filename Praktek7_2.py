def OrdinalCheck(x):
    if x[-1] == "1":
        print(x, "st")
    elif x[-1] == "2":
        print(x, "nd")
    elif x[-1] == "3":
        print(x, "rd")
    else:
        return False
    
while True:
    angka = input("Angka: ")
    if OrdinalCheck(angka) == False:
        print(angka, "th")
    
    if angka == "0":
        break
        
print("bye bye :3")