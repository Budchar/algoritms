#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    smallest = min(arr)
    check_arr = arr
    result_arr = list()
    # 더이상 smallest 보다 큰 숫자가 없을때 까지
    while(len([x for x in check_arr if x > smallest]) != 0):
        # 자를 수 있는 숫자를 나눠주고
        result_arr.append(len(check_arr))
        # 리스트를 갱신
        check_arr = [x - smallest for x in check_arr if x >= smallest +1]
        # 가장 작은 숫자도 갱신
        smallest = min(check_arr)
    # 제일 작은 수만 모여 있는 숫자를 더해주자
    result_arr.append(len(check_arr))
    return result_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
