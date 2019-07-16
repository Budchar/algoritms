#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr, n):
    # plus, minus, zero를 발견하면 순서에 맞게 증가한다.
    num = [0, 0, 0]

    for a in arr:
        if a == 0:
            num[2] += 1/n
        elif a < 0:
            num[1] += 1/n
        else: 
            num[0] += 1/n

    for n in num:
        print(f"{n:0.6f}")

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)
