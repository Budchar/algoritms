#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    result = []
    # O(n)
    for n, i in enumerate(a):
        if a.count(i)>1:
            for m, j in enumerate(a[n+1:]):
                if i == j:
                    result.append(m+1)
                    break
    return min(result) if result else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
