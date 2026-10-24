#WAP to find the sum of natural number n using While Loop

n = int(input("Enter Number : "))
sum = 0
i =1
while i <= n :
    sum += i
    i += 1 
print("Sum of natural number" ,n ,"is",sum)
