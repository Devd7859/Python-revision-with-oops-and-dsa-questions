def greatest(a,b,c):
    if(a>b and a>c):
        print("A is the greatest.")
        return a
    elif(b>a and b>c):
        print("B is the greatest.")
        return b
    else:
        print("C is the greatest.")
        return c

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
print(greatest(n1,n2,n3))