#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    # root_a와 root_b 사이의 정수 숫자를 구하면 된다
    root_a = a**0.5
    # root_b의 경우는 반올림으로 해서 정수 하나를 포함 할수 있도록 만든다
    # ex root_a = 2.5, root_b = 3.4이면 3을 포함 해야하므로 반올림 해준다 또한 b가 square면 이를 포함 해줄수 있도록 +1해준다
    root_b = math.ceil(b**0.5) if math.ceil(b**0.5) != b**0.5 else math.ceil(b**0.5)+1
    return int(abs(root_a-root_b))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
