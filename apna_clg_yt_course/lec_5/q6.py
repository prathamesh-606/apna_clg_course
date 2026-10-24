#Search for the number x in this Tuple using For Loop
#tup = (1 ,4 ,9 ,16 ,25 ,36 ,49 ,64 ,81 ,100)

tup = (1 ,4 ,9 ,16 ,25 ,36 ,49 ,64 ,81 ,100)
n = int(input("Enter number :"))
idx = 0
for num in tup :
    if num == n :
        print("Number found at Index :" , idx)
    idx += 1