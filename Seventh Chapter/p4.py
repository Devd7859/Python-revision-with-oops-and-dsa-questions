import math 
num = int(input("enter the number to check: "))
is_prime = True
print(math.sqrt(num))
if num<1:
    is_prime = False
else:
    for i in range(2,int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"the {num} is a prime number.")
else:
    print(f"the {num} is not a prime number.")