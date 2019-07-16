#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    # 1부터 29까지 0 = '', 20 = 'twenty ', 15 = 'quarter'
    exp1 = ['', 'one minute', 'two minutes', 'three minutes', 'four minutes', 'five minutes', 'six minutes', 'seven minutes', 'eight minutes', 'nine minutes']
    exp2 = ['ten minutes', 'eleven minutes', 'twelve minutes', 'thirteen minutes', 'fourteen minutes', 'quarter', 'sixteen minutes', 'seventeen minutes', 'eighteen minutes', 'nineteen minutes']
    exp3 = [f'twenty {i}' for i in exp1]
    exp = [exp1, exp2, exp3]
    hour_exp = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    if m > 30:
        if h == 12:
            hour = hour_exp[0]
        else:
            hour = hour_exp[h]
    else:
        hour = hour_exp[h-1]

    if m == 30:
        return f'half past {hour}'
    elif m > 30:
        mm = f'0{60-m}' if len(str(60-m)) == 1 else str(60-m)
        return f'{exp[int(mm[0])][int(mm[1])]} to {hour}'
    else:
        # m이 30보다 작은 경우 0~29
        mm = f'0{m}' if len(str(m)) == 1 else str(m)
        if mm == '00':
            return f"{hour} o' clock"
        else:
            return f"{exp[int(mm[0])][int(mm[1])]} past {hour}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
