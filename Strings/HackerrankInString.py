#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    if re.search(r'.*h.*a.*c.*k.*e.*r.*r.*a.*n.*k.*',s):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
