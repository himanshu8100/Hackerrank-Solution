#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):
    x = sorted(x)

    count_trans = 0
    last = x[0]
    i = 0
    while(i < n):
        count_trans = count_trans + 1
        next_point = x[i] + k
        while(i < n and x[i] <= next_point):
            i = i + 1
        next_point = x[i-1] + k
        while(i < n and x[i] <= next_point):
            i = i + 1

    return (count_trans) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
