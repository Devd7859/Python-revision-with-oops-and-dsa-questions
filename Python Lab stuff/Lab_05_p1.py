#Student Marks List Processing & Report Generator
#Largest Mark
marks = [78, 92, 45, 67, 89, 92, 34, 56, 81]
largest = max(marks)
print("Largest Marks: ", largest)
#Second Largest Mark
uniq = list(set(marks))
uniq.sort(reverse= True)
second_largest = uniq[1]
print("Second largest Mark: ",second_largest)
#Separate Even And Odd Marks
even_marks = [mark for mark in marks if mark % 2 == 0]
odd_marks = [mark for mark in marks if mark % 2 != 0]
print("even_marks: ", even_marks)
print("odd marks: ",odd_marks)
#merge two sections and sort
Section_a = [78,92,45,67]
Section_b = [89,34,56,81]
merged_marks = Section_a + Section_b
merged_marks.sort()
print("Merged & sorted Marks: ",merged_marks)
#sort student records by marks
students = [["Alice",78],["Bob",92],["Charlie",45],["David",67]]
students.sort(key = lambda x : x[1])
print("Student Sorted by marks: ")
for student in students:
    print(student)
#second largest marks using bubble sort
bubble_marks = marks.copy()
n = len(bubble_marks)
for i in range(n):
    for j in  range(0,n-i-1):
        if bubble_marks[j] > bubble_marks[j+1]:
            bubble_marks[j], bubble_marks[j+ 1] = bubble_marks[j+1], bubble_marks[j]

print("Second Largest Mark(Bubble Sort): ", bubble_marks[-2])
#sort student names based on length
names = ["Dev","Shivani","Aesha","Chetanya", "Khushi","Krishi","Anshul"]
names.sort(key = len)
print("Names sorted by length: ", names)
#find union from two classes
class1 = [78, 92, 45, 67]
class2 = [89, 92, 34, 67]
union_marks = set(class1).union(set(class2))
print("Union of Marks: ",union_marks)
inter_marks = set(class1).intersection(set(class2))
print("Intersection of marks: ",inter_marks)
#print marks at odd index positions
print("marks at the odd index positions: ")
for i in range(1,len(marks),2):
    print(marks[i],end = " ")

