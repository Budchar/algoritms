#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    result = 1
    for x in range(n):
        result *= x+1
    return result
if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
