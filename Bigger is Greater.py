#!/bin/python3
# for _ in range(int(input())):
#     s = input()
#     has_greater = False
#     for i in range(len(s)-1)[::-1]:
#         if ord(s[i]) < ord(s[i+1]):
#             for j in range(i+1,len(s))[::-1]:
#                 if ord(s[i]) < ord(s[j]):
#                     lis = list(s)
#                     lis[i],lis[j]=lis[j],lis[i]
#                     print("".join(lis[:i+1]+lis[i+1:][::-1]))
#                     has_greater = True
#                 if has_greater == True:
#                     break
#         if has_greater == True:
#             break
#     if has_greater == False:
#         print("no answer")
import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    sorted_w = sorted(w, reverse=True)
    if w == ''.join(sorted_w):
        return 'no answer'
    for idx in range(len(w)-1)[::-1]:
        if ord(w[idx+1]) < ord(w[idx]):
            for jdx in range(idx, len(w))[::-1]:
                if ord(w[idx]) < ord(w[jdx]):
                    print(f'answer is {w[:idx] + w[jdx] +w[idx:jdx] +w[idx] + w[jdx:]}')
                    return w[:idx] + w[jdx] +w[idx:jdx] +w[idx] + w[jdx:]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()