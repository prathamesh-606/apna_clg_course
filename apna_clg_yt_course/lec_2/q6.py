#WAP to find greatest of 4 numbers entered by the user 
a = int(input("Enter your 1st number : "))
b = int(input("Enter your 2nd number : "))
c = int(input("Enter your 3rd number : "))
d = int(input("Enter your 4th number : "))
if(a==b ==c ==d):
    print("ALL numbers are same")
    print("Please enter different values")
elif(a==b ==c or b==c ==d or c==d == a or a==d ==b):
    print("Three numbers are same")
    print("Please enter different values")
elif(a==b or b==c or c==d or a==d):
    print("Two numbers are same")
    print("Please enter different values")
elif(a!=b !=c !=d !=a): 
    if(a>b and a>c and a>d):
        print("Your 1st number is greatest:",a)
    elif(b>c and b>d):
        print("Your 2nd number is greatest:",b)
    elif(c>d):
        print("Your 3rd number is greatest:",c)
    else:
        print("Your 4th number is greatest:",d)

    
