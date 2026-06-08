def calculate_marks(marks):
    total = sum(marks)
    average = total/len(marks)
    
    if average> 100:
        grade = "Enter valid marks."
    elif average >=90:
        grade = "S"
    elif 90 > average >=80:
        grade = "A"
    elif 80 > average >= 70:
        grade = "B"
    elif 70 > average >= 60:
        grade = "C"
    elif 60 >average >= 50:
        grade = "D"
    elif 50 >average >= 40:
        grade = "E"
    else:
        grade = "F"
    return total, average,grade

def main():
    students = []
    n = int(input("enter the number of student: "))
    for i in range(n):
        print(f"enter the details of the {i+1} student: ")
        roll_no = input("enter the roll no: ")
        name = input("enter the name of the student: ")
        print("Enter the marks of 5 subjects: ")
        marks = []
        for j in range(5):
            mark = float(input(f"Enter the marks of {j+1} subject: "))
            marks.append(mark)
        total,average,grade = calculate_marks(marks)
        student_record = {
            "Roll_No" : roll_no,
            "Name" : name,
            "marks" : marks,
            "total" : total,
            "average" : average,
            "grade" : grade
        }
        students.append(student_record)
    if not students:
        return 
    topper = max(students,key = lambda x : x["average"])
    lowest_score = min(students,key = lambda x : x["average"])
    print(f"Topper marks: {topper}")
    print(f"lowest marks: {lowest_score}")
    sort_students = sorted(students,key =lambda x : x["average"],reverse = True)
    print("Students displaying in descending order: ")
    for s in sort_students:
        print(f"Roll no: {s['Roll_No']} | Name: {s['Name']} | Total : {s['total']} | Average : {s['average']} | Grade : {s['grade']}")

if __name__ == "__main__":
    main()


