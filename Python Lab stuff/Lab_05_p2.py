#Employee Tuple &amp; Dictionary Data Management System
emp_ids = (101, 102, 103, 104, 105, 102, 103, 106)
#display 4th element and 4th element from last in a tuple
print("4th element: ",emp_ids[3])
print("4th element from last: ",emp_ids[-4])
#all repeated items in employee id tuple
repeated = []
for i in emp_ids:
    if emp_ids.count(i) > 1 and i not in repeated:
        repeated.append(i)
print("Repeated employee id: ",repeated)
#check whether a given id exists or not
search_id = int(input("enter employee id to seaerch: "))
if search_id in emp_ids:
    print("Employee ID exists.")
else:
    print("Employee id does not exist.")
employees = [(101,"alice",50000), (102,"Bob",55000),(103,"Dev",75000)]
ids, names, salaries = zip(*employees)
print("Ids:", list(ids))
print("Names:",list(names))
print("Salaries:",list(salaries))
#replace the last value of each tuple with new value
bonus = 5000
updated_emp =[]
updated_emp = []
for emp in employees:
    updated_emp.append((emp[0], emp[1], bonus))
print("updated Employee Records: ")
for emp in updated_emp:
    print(emp)
#remove all empty tuples from a list
tuple_list = [(),(101,"Alice"),(),(102,"Bob"),(),(103,"Dev")]
cleaned_list = []
for t in tuple_list:
    if t:
        cleaned_list.append(t)
print("After removing empty tuples:")
print(cleaned_list)
#convert a list of tuple into a dictonary
salary_dict = {}
for emp_id,name,salary in employees:
    salary_dict[emp_id] = salary
print("Emplyoee Id -> Salary Dictionary: ")
print(salary_dict)

