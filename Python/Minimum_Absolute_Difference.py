#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    min_sum = 2 * arr[-1]     
    if len(arr) != len(list(set(arr))):
        return 0
    for i in range(len(arr)-1):
        min_sum = min ( abs(arr[i]-arr[i+1]), min_sum )   
    return(min_sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
