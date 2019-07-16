#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    # le_ri는 왼쪽에서 오른쪽으로 가는 diagonal ri_le는 오른쪽에서 왼쪽으로 가는 diagonal
    le_ri = 0
    ri_le = 0
    lenth = len(arr)

    # arr길이만큼 돌면서 le_ri는 (i,i)값을 ri_le는 (len(arr)-i,i)값을 더해준다
    for i in range(lenth):
        le_ri += arr[i][i]
        ri_le += arr[lenth-i-1][i]

    # 두 diagonal의 차이 절대값을 return한다
    return abs(le_ri-ri_le)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()