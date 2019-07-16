#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    count_dict = {"1":0,"2":0,"3":0,"4":0,"5":0}
    for i in arr:
        count_dict[str(i)] += 1

    for k, v in count_dict.items():
        if v == max(count_dict.values()):
            return k

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
