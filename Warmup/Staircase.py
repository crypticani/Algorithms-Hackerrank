#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    num = int(n)
    for stairs in range(1, num):
        print (' ' * (num-stairs-1), '#' * stairs)
        n -= 1
    print ('#' * num)
    

if __name__ == '__main__':
    n = int(input())

    staircase(n)
