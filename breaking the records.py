#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mini = scores[0]
    maxi = scores[0]
    Min = 0
    Max = 0
    for i in range(1, len(scores)+1):
        if scores[i] > maxi:
            maxi = scores[i]
            Max += 1
        elif scores[i] < mini:
            mini = scores[i]
            Min += 1
    return Max, Min

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
