#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    # 1페이지 기준으로 전체 페이지와 찾고자하는 페이지
    whole_page = int(n/2)+1
    index_page = int(p/2)+1
    if whole_page - index_page > index_page - 1 :
        return index_page - 1
    else:
        return whole_page - index_page

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
