#problem 8 Swapping of two numbers with and without using third variable
num1 = int(input("enter the 1st number: "))
num2 = int(input("enter the 2nd number: "))
print("the number before swapping: ",num1,num2)
temp = num1
num1 = num2
num2 = temp
print("the number after swapping: ", num1,num2)

#without third variable
n1 = int(input("enter the n1: "))
n2 = int(input("enter the n2: "))
print("numbers before swapping: ",n1,n2)
n1,n2 = n2,n1
print("numbers after swapping: ",n1,n2)