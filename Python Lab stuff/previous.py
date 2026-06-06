#Pronic number
""" Start = int(input("enter the starting number: "))
End = int(input("enter the ending number: "))
for i in range (Start,End,1):
    n = i*(i+1)
    if n < End:
        print(n, end =" ")
"""
"""
def reverse_fibonacci_pattern(first_term, second_term, rows):
    total_terms = rows * (rows + 1) // 2

    seq = [first_term, second_term]

    while len(seq) < total_terms:
        seq.append(seq[-2] - seq[-1])

    index = 0

    for i in range(rows, 0, -1):
        for j in range(i):
            print(seq[index], end=" ")
            index += 1
        print()

first_term = int(input("Enter first term: "))
second_term = int(input("Enter second term: "))
rows = int(input("Enter number of rows: "))

reverse_fibonacci_pattern(first_term, second_term, rows)
"""
import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

for i in range(3):
    for j in range(3):
        print(matrix[i][j], end=" ")
    print()