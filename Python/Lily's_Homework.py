#!/bin/python3

import math
import os
import random
import re
import sys

def lilysHomework(ar):
    temp=[]
    temp.extend(ar)
    sorte= list(ar)
    sorte.sort()
    temp.sort(reverse=True) 
      
    c1 = total(ar,sorte)
    print(ar, sorte, temp)
    c2 = total(ar,temp)
    if c1>=c2:
        return c2
    else:
        return c1
    
def total(ar, sorted_a):    
    m = {}
    a=list(ar)
    for i in range(len(a)):
        m[a[i]] = i 
    ret = 0
    
    for i in range(len(a)):
        if a[i] != sorted_a[i]:
            ret +=1
                        
            ind_to_swap = m[ sorted_a[i] ]
            m[ a[i] ] = m[ sorted_a[i]]
            a[i],a[ind_to_swap] = sorted_a[i],a[i]
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
