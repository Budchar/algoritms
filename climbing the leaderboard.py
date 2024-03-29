#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    result = []
    score_set = sorted(set(scores), reverse=True)
    score_set.append(0)
    l = len(score_set)
    for a in alice:
        while (a >= score_set[l-1]) and (l>0):
            l -= 1
        result.append(l+1)
    return result

    # scores_set = list(set(scores))
    # scores_set.sort(reverse=True)
    # result = []
    # l = len(scores_set)
    # for s in alice:
    #     while (l>0) and (s >= scores_set[l-1]):
    #         l -= 1
    #     result.append(l+1)
    # return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
