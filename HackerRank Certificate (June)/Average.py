#!/bin/python3

import os
import sys

def avg(*n):
    if not n:
        return '0.00'
    sum = 0
    for numbers in n:
        sum += numbers
        
    average = float(sum) / len(n)
    return '%.2f' % average

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nums = list(map(int, input().split()))
    res = avg(*nums)
    fptr.write(res + '\n')
    fptr.close()
