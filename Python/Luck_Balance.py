#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    
    total = sum([contests[x][0] for x in range (len(contests))])
    
    imp = [contests[x][0] for x in range (len(contests)) if contests[x][1]==1]
    imp.sort()
    
    minus = max(len(imp)-k, 0)
    if minus!=0:
        minus=sum(imp[0:minus])
    
    return(total-2*minus)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
