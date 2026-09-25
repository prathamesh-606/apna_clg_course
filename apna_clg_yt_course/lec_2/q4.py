# WAP to find greatest of 3 numbers entered by the user 
a = int(input("Enter your 1st number : "))
b = int(input("Enter your 2nd number : "))
c = int(input("Enter your 3rd number : "))
if(a==b ==c):
    print("Three numbers are same")
    print("Please enter different values")
elif(a==b or b==c): 
    print("Two numbers are same")
    print("Please enter different values")
if(a!=b and b!=c):
    if(a>b and a>c):
        print("Your 1st number is greatest:",a)
    elif(b>c):
        print("Your 2nd number is greatest:",b)
    else:
        print("Your 3rd number is greatest:",c)






