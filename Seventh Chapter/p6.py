num = int(input("enter the number: "))
factorail = 1

if num < 0:
    print("invalid number.")
elif num == 0 or num == 1:
    print("factorail is: ",factorail)
else:
    for i in range(1,num+1,1):
        factorail *= i
        i += 1
    print(f"the factorial of the given {num} is {factorail}")


