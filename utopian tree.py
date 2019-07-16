#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    result = 1
    # season이 0이면 spring, 1이면 summer 초기값은 봄이 지나서 result에 1을더하고 season을 여름으로 둠
    season = 0
    for i in range(n):
        if season == 0:
            result *= 2
            season = 1
        else:
            result += 1
            season = 0
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
