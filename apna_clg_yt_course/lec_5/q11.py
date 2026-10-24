#WAP to find the Factorial of a number n using For Loop

n = int(input("Enter Number : "))
fac = 1
for i in range(1 ,n+1):
    fac *= i
print("Factorial of " ,n ,"is",fac)