#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the nonDivisibleSubset function below.
# 주어진 숫자열 s랑 숫자 k에서 임의의 두 숫자를 더해서 k로 나눠지지 않는 s의 subset의 최대 길이를 구하라
def nonDivisibleSubset(k, S):
    # k로 나눈 a, b 나머지의 합이 k라면 a+b도 k의 배수
    # reminders는 어레이의 나머지 정보
    reminders = [0] * k
    for s in S:
        reminders[s % k] += 1
    
    result = min(reminders[0], 1)
    for i in range(1, math.ceil(k/2)):
        if i != k-i:
            result += max(reminders[i], reminders[k-i])
    if k%2 == 0:
        result += 1

    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, S)

    fptr.write(str(result) + '\n')

    fptr.close()
