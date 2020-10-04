#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr, n):
    pos = []
    neg = []
    zero = []
    for i in range(n):
        if(arr[i]>0):
            pos.append(1)
        elif(arr[i] == 0):
            zero.append(1)
        else:
            neg.append(1)

    print("{0:.6f}".format(pos.count(1)/n))
    print("{0:.6f}".format(neg.count(1)/n))
    print("{0:.6f}".format(zero.count(1)/n))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)
