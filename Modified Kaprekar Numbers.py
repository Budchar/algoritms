#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    output = list()
    for i in range(p, q):
        le = len(str(i))
        squre_i = pow(i, 2)
        list_squre_i = str(squre_i)
        if list_squre_i[:le] + list_squre_i[le:] == i:
            output.append(i)
    return output
if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)