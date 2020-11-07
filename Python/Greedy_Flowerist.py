#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, a):
    ''' c=sorted(a,reverse=True)
    total = 0
    print(c,k)
    for i in range(0,len(c),k):
        if i+k<=len(c):
            total+= ((i//k)+1) * sum(c[i:k])
        else:
            total+= ((i//k)+1) * sum(c[i:])
    return total'''
    a.sort(reverse=True)
    return sum((v * (i // k + 1) for i, v in enumerate(a)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
