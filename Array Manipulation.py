#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    lis = [0 for _ in range(n)]
    for q in queries:
        a, b, k = q
        lis[a-1] += k
        if b < n:
            lis[b] -= k
    # 실제 숫자를 더하는 것이 아니라 방향 지시등같은 느낌 여기서부턴 더해라 같은?
    prev = 0
    for i in range(len(lis)):
        prev += lis[i]
        lis[i] = prev
    return max(lis)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
