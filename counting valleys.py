#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    # result는 얼마나 많은 계곡을 지났는지 표시
    result = 0 
    # 현 상태에 대한 표시 
    depth = 0 
    for i in s:
        # 오르락 내리락함에 따라서 depth값 수정
        if i == "U":
            depth += 1
        else: 
            depth -= 1
        # depth가 0이 되고 올라온 순간에 계곡하나 지난것으로 판단
        if depth == 0 and i == "U":
            result += 1

    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
