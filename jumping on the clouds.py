#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    pos = 0
    point = 100
    stop = 0
    while(stop != 1):
        pos += k
        if pos >= len(c):
            pos = pos%len(c)
            stop = 1
        point -= 1
        if c[pos] == 1:
            point -= 2

    return point
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
