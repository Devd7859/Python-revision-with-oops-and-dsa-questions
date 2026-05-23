#Question 1 Print system info date time day name and version name of python
import sys
from datetime import datetime
now = datetime.now()
print("Personal Information")
naam = "Dev"
Course = "B-TECH CSE WITH AI AND ML"
Gender = "Male"
dob = "09-12-2005"
print("Name: ",naam)
print("Course: ",Course)
print("Gender: ",Gender)
print("Date of Birth: ",dob)

print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("Current Day: ", now.strftime("%A"))
print("Python Version: ", sys.version)

#Question 2 print numeric pattern computation module
n = int(input("Enter the integer: "))
answer = n + ((n*10)+n) + ((n*100) + (n*10)+n) + ((n*1000)+ (n*100) + (n*10)+n)
print(answer)

#Question 3 Student profile Module
name = input("Enter the name of the student: ")
Reg_no = input("Enter the registration number of the student: ")
Age = int(input("Enter the age of the student: "))
Marks = []
for i in range(1,6,1):
    M1 = int(input("Enter the marks  of Subject: "))
    Marks.append(M1)
totalmarks = sum(Marks)
print(name)
print(Reg_no)
print(Age)
print("Total Marks: ",totalmarks)
average = totalmarks/5
print("Average: ",average)
if average >= 90:
    print("Grade: S")
elif average >= 80 and average <90:
    print("Grade: A")
elif average >= 70 and average <80:
    print("Grade: B")
elif average >= 60 and average <70:
    print("Grade: C")
elif average >= 50 and average <60:
    print("Grade: D")
else: 
    print("Fail")
if average <50:
    print("Fail")
else:
    print("Pass")

#Question 4 take the input of the year and check whether its a leap year or not
import calendar
while True:
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    if 1 <= month <= 12:
        break
    else:
        print("Invalid input of month.")
if calendar.isleap(year):
    print(" The year  is a LEAP YEAR.")
else:
    print(" The year  is NOT a leap year.")
print(calendar.month(year, month))