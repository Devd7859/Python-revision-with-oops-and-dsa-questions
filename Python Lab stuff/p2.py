#problem 11 distance between two poitns
import math
z1 = float(input("enter the x1: "))
z2 = float(input("enter the x2: "))
y2 = float(input("enter the y1: "))
y3 = float(input("enter the y2: "))
d1 = (z1 - y2)**2
d2 = (z2 - y3)**2
dist = math.sqrt(d1 + d2)
print("Eucldiean distance between two points",dist)
print(math.sqrt(8))