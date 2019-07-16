#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    # s에서 m개를 선택해 합한뒤 d값이 나오면 result에 +1
    result = 0
    # d가 m*5보다 크면 고를 수 있는 선택지가 없음
    for i in range(len(s)-m+1):
        if sum(s[i:i+m])==d:
            result +=1
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
