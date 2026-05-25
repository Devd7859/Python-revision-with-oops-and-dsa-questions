#problem 2 addition,multiplication,division and subtraction of two numbers
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
choice = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: "))
if choice == 1:
    print("addition of both numbers: ", a + b)
elif choice == 2:
    print("Subtraction of both numbers: ",a - b)
elif choice == 3:
    print("a division b: ", a/b)
elif choice == 4:
    print("a multiplication b: ", a * b)
else:
    print("enter valid choice")