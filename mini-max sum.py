#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    # 출력할 변수를 선언 및 최소합은 최소값을 빼고 최대합은 최소값을 뺀다. 
    mn = arr.copy()
    mn.remove(max(mn))
    mx = arr.copy()
    mx.remove(min(mx))

    # min과 max를 출력
    print(sum(mn), sum(mx))
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
