#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    le = len(arr)
    top = float('-inf')
    for row in range(1, le-1):
        for col in range(1, le-1):
            ul = arr[row-1][col-1]
            u = arr[row-1][col]
            ur = arr[row-1][col+1]
            c = arr[row][col]
            dl = arr[row+1][col-1]
            d = arr[row+1][col]
            dr = arr[row+1][col+1]
            s = ul + u + ur + c + dl + d + dr
            print(row, col, s)
            if s > top:
                top = s
    return top

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
