#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    # a는 고양이 a와 쥐의 거리, b는 고양이 b와 쥐의 거리
    a = abs(x-z)
    b = abs(y-z)
    if a > b:
        return "Cat B"
    elif a == b:
        return "Mouse C"
    else:
        return "Cat A"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
