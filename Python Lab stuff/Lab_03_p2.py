import math
#Part 1 of the question
Amount = int(input("Enter the Transaction Amount: "))
Flag = False
if (900 <= Amount <= 1100) or (1900 <= Amount <= 2100):
    Flag = True

if Flag:
    print("The transaction is Suspicious.")
else:
    print("The transaction is fine.")
#Part 2 of the question
Temp = float(input("Enter The Temperature in Celsius: "))
diff = abs(Temp - 17)
if Temp > 17:
    result = 2 * diff
    print(f"Temperature is above  17°C. Result = {result} ")
else:
    result = diff
    print(f"Temperature is below 17°C. Result = {result}")

#part 3 of the question:
Employees = int(input("enter the number of employees: "))
if Employees < 0:
    print("The number of employess can not be negative.")
else:
    print(f"the total Seating arrangement possible is: {math.factorial(Employees)}")

#Part 4 of the Question:
year = int(input("enter the year to check for leap year calculation: "))
if year < 0:
    print("year can not be negative.") 
else:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year. Correct Hospital Scheduling Applied.")
    else:
        print(f"{year} is not a leap year.")