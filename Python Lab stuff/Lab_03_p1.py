Roll_no = int(input("Enter the roll number: "))
if (Roll_no % 2 == 0):
    print("Student Assigend to : Lab A")
else:
    print("Student Assigend to : Lab B")
Marks = []
for i in range(1,4):
    score = float(input(f"Enter Marks for the Subject {i} :"))
    Marks.append(score)
total_marks = sum(Marks)
print(total_marks)
first_marks = Marks[0]
if_Equal = True
for score in Marks:
    if score != first_marks:
        if_Equal = False
        break
if if_Equal:
    bonus = total_marks * 3
    print(f"Scholarship bonus Marks: {bonus}")
else:
    print("No Scholarship bonus Marks Awarded.")
Max_Marks = max(Marks)
print(f"Highest Mark Performace: {Max_Marks}")
