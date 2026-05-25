a1 = int(input("enter the first number: "))
a2 = int(input("enter the second number: "))
a3 = int(input("enter the third number: "))
a4 = int(input("enter the fourth number: "))
if (a1 >a2 and a1 >a3 and a1>a4):
    print("The first number  {0} is the greatest number".format(a1))
elif(a2>a1 and a2>a3 and a2>a4):
    print("the second number {0} is the greatest number".format(a2))
elif(a3>a1 and a3>a2 and a3>a4):
    print("the third number {0} is the greatest number".format(a3))
else:
    print("the fourth number {0} is the greatest".format(a4))
