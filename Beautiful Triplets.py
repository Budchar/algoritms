#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    n = len(arr)
    res = 0
    for i in range(n-2):
        initiate = arr[i]
        try:
            j = arr[i+1:].index(initiate + d)
            try:
                k = arr[j+1:].index(initiate+2*d)
                res += 1
            except ValueError:
                pass
        except ValueError:
            pass

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
