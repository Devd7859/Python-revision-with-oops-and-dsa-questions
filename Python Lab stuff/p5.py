#problem 5 solution of quadratic equation
import math 
a = float(input("enter the coeeficent of x2: "))
b = float(input("enter the coeeficent of x: "))
c = float(input("enter the value of constant: "))
d = b**2 - 4*a*c
if d > 0:
    x0 = (-b + math.sqrt(d))/(2*a) 
    x1 = (-b + math.sqrt(d))/(2*a) 
    print("Two real roots: ")
    print(x0)
    print(x1)
elif d == 0:
    y = -b/2*a
    print("one real root:")
    print(y)
else:
    real = -b / (2*a)
    imag = math.sqrt(-d)/2*a
    print("Complex roots: ")
    print(real,"+",imag,"i")
    print(real,"-",imag,"i")