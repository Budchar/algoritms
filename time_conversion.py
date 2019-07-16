#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    am_pm = s[-2:]
    mil_time = s[2:-2]
    if am_pm == 'PM':
        hour = s[0:2] if s[0:2] == '12' else str(int(s[0:2])+12)
    else:
        hour = '00' if s[0:2] == '12' else s[0:2]
        
    mil_time = hour + mil_time
    return(mil_time)
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
