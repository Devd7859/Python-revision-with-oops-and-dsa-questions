def avg():
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    c = int(input("Enter the number: "))
    average = (a+b+c)/3
    print(average)

def factorial(n):
    if(n==1 or n == 0):
        return 1
    return n * factorial(n-1)


print(factorial(5))