#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    output = [0, 0]
    l = len(topic)
    le = len(topic[0])
    for i in range(l-1):
        for j in range(i+1, l):
            if topic[i][0] == '0' and topic[j][0] == '0':
                t = le - str(int(topic[i]) + int(topic[j])).count('0') - 1
            else:
                t = le - str(int(topic[i]) + int(topic[j])).count('0')
            if t > output[0]:
                output[0] = t
                output[1] = 1
            elif t == output[0]:
                output[1] += 1
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
