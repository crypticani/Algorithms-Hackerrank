#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    score_a = []
    score_b = []
    for i in range(3):
        if(a[i]>b[i]):
            score_a.append(1)
        elif(a[i]<b[i]):
            score_b.append(1)
        
    
    return [sum(score_a),sum(score_b)]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
