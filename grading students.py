#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    f_grades = []
    for g in grades:
        if g < 38:
            f_grades.append(g)
            continue

        if g%5 >= 3:
            f_grades.append(int(g/5+1)*5)
        else:
            f_grades.append(g)

    return f_grades
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
