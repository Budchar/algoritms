#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s_noblank = s.replace(' ', '')
    row_len = math.floor(math.sqrt(len(s_noblank)))
    col_len = math.ceil(math.sqrt(len(s_noblank)))
    matrix = ['']*col_len
    row = 0
    col = 0
    for c in s_noblank:
        matrix[row] += c
        row += 1
        if row == col_len:
            row = 0
            col += 1
    return matrix
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write('\n'.join(result))

    fptr.close()
