#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # ar를 돌며 새로운 숫자는 arr에 넣고 arr을 확인해서 같은게 있으면 result값 +1
    result = 0
    arr = []
    for a in ar:
        if a in arr:
            result += 1
            arr.remove(a)
        else:
            arr.append(a)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()