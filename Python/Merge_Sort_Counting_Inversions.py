#!/bin/python3

import math
import os
import random
import re
import sys

total=0
# Complete the countInversions function below.
def MergeSort(arr):
    if len(arr) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(arr)//2
        L= arr[:r]
        M= arr[r:]

        # Sort the two halves
        MergeSort(L)
        MergeSort(M)
        
        i = j = k= 0
        global total

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] <= M[j]:
                arr[k]= L[i]
                i += 1
            else:
                arr[k]= M[j]
                j += 1
                total += len(L)-i
            k += 1 
            
        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            arr[k]=L[i]
            i += 1
            k += 1
        while j < len(M):
            arr[k]=M[j]
            j += 1
            k += 1

def countInversions(arra):
    global total
    init = total
    MergeSort(arra) 
    
    return total-init

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
