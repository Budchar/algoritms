#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    lenth = 0
    for i in range(min([len(s), len(t)])):
        if s[i] == t[i]:
            lenth += 1
        else: 
            break
    if len(s) + len(t) - 2*lenth > k:
        return "No"
    elif (len(s) + len(t) - 2*lenth)%2 == k%2:
        return "Yes"
    elif len(s) + len(t) <k:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
