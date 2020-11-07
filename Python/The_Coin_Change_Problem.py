#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    # Write your code here
    list_op=[]
    for index,i in enumerate(c):
        list_temp=[1]
        for j in range (n):
            if index==0 and (j+1)%i==0:
                list_temp.append(1)
            elif index==0 and (j+1)%i!=0:
                list_temp.append(0)
            elif i>(j+1):
                list_temp.append(list_op[index-1][j+1])
            elif i<=(j+1):
                a = list_op[index-1][j+1]
                b = list_temp[j+1-i]
                list_temp.append(a+b)
            
        list_op.append(list_temp)
    
    print (list_op)        
    return(list_op[len(c)-1][n])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
