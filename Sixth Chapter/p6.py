Marks = int(input("enter the marks of the student: "))
if Marks > 100:
    print("Enter valid marks")
elif 100>=Marks>=90:
    print("S Grade")
elif 80 <= Marks <90:
    print("A Grade")
elif 70 <= Marks <80:
    print("B Grade")
elif 60 <= Marks <70:
    print("C Grade")
elif 50 <= Marks <60:
    print("D Grade")
else:
    print("F grade")