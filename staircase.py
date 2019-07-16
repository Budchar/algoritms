#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    # n줄만큼 반복
    for i in range(n):
        # 줄 수만큼 #프린트 하되 n만큼 오른쪽 정렬
        print(f"{'#'*(i+1):>{n}}")
    return

if __name__ == '__main__':
    n = int(input())

    staircase(n)
