#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year < 1918:
        result = '12.09.'+str(year) if year%4 ==0 else '13.09.'+str(year)
    elif year == 1918:
        result = '26.09.1918'
    else:
        # 윤년인지 확인하고 날짜를 하루 조정
        result = '12.09.'+str(year) if (year%4 ==0 and year%100 != 0) or (year%400 == 0) else '13.09.'+str(year)
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
