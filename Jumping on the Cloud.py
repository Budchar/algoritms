#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    result = 0
    index = 0
    while index < len(c)-1:
        if len(c) - index > 2:
            if c[index+2] == 0:
                print('2')
                index += 2
            else:
                print('1')
                index += 1
        else:
            print('1')
            index += 1
        result += 1
    
    return result
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
