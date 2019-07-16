#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
# O(2n)
def workbook(n, k, arr):
    # n은 챕터 갯수, k는 챕터별 페이지 제한, arr은 챕터당 페이지 수
    error = 0
    pages = list()
    # 챕터 갯수, i는 챕터의 페이지 수
    for i in arr:
        page = [i for i in range(1, i+1)]
        pages.extend([page[i:i+k] for i in range(0, len(page), k)])
    
    for num, li in enumerate(pages):
        if num+1 in li:
            error += 1
    return error
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
