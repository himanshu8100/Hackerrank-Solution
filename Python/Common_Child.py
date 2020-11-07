#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(x, y):
    z=[[0 for j in range(len(y)+1)] for i in range(len(x)+1)]
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            if a == b:
                z[i+1][j+1] = z[i][j] + 1
            else:
                z[i+1][j+1] = \
                    max(z[i+1][j], z[i][j+1])
    return z[-1][-1] 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
