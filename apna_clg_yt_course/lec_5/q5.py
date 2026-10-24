#Search for the number x in this Tuple using While Loop
#tup = (1 ,4 ,9 ,16 ,25 ,36 ,49 ,64 ,81 ,100)

tup = (1 ,4 ,9 ,16 ,25 ,36 ,49 ,64 ,81 ,100)
n = int(input("Enter number :"))
i = 0
while i < len(tup):
    if tup[i] == n :
        print("Found at Index :" , i)
    i += 1



    



