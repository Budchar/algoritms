#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    # n열의 합과, n행의 합이 갖다면 거기 한 [][]에 모을수 있다.
    l = len(container)
    colli = []
    rowli = []
    for n in range(l):        
        col = 0
        row = 0
        for c in range(l):
            col += container[n][c]
        for r in range(l):
            row += container[r][n]
        colli.append(col)
        rowli.append(row)
    print(colli, rowli)
    # sort한 col과 row의 짝만 맞으면 됨 container1에 type1만 모여야할 필요는 없기 떄문
    return 'Possible' if sorted(colli) == sorted(rowli) else 'Impossible'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()