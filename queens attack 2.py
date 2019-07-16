#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    up = max(n-r_q, 0)
    down = max(r_q-1, 0)
    right = max(n-c_q, 0)
    left = max(c_q-1, 0)
    ur = min(up, right)
    dr = min(down, right)
    ul = min(up, left)
    dl = min(down, left)
    for obs in obstacles:
        # 장애물과 퀸 사이의 거리
        r = obs[0] - r_q 
        c = obs[1] - c_q 
        # 수평상에 있다면
        if r == 0:
            # r0 c+
            if c > 0:
                right = min(right, c-1)
            # r0 c-
            else:
                left = min(left, -c-1)
        # 수직상에 있다면
        elif c == 0:
            # r+ c0
            if r > 0:
                up = min(up, r-1)
            # r- c0
            else:
                down = min(down, -r-1)
        # 대각선상에 있다면
        elif abs(r) - abs(c) == 0:
            # r +
            if r > 0:
                # r+ c+
                if c > 0:
                    ur = min(ur, r-1)
                # r+ c-
                else:
                    ul = min(ul, r-1)
            # r-
            else:
                # r- c+
                if c > 0:
                    dr = min(dr, -r-1)
                # r- c-
                else:
                    dl = min(dl, -r-1)
    return up + down + right + left + ur + dr + ul + dl

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
