#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    total = 0
    counts = [0] * 201

    for day in range(d):
        counts[expenditure[day]] += 1

    if d%2 == 0: #even
        odd = False
    else: #odd
        odd = True

    oldest_day = 0
    for i in range(d, len(expenditure)):
        median = get_median(counts, odd, d)
        if expenditure[i] >= 2*median:
            total += 1
        counts[expenditure[oldest_day]] -= 1
        counts[expenditure[i]] += 1
        oldest_day += 1
    return total

def get_median(counts, odd, d):
    temp = 0
    left, right = -1, -1
    for i, v in enumerate(counts):
        temp += v
        if odd:
            if temp >= ((d//2)+1):
                return i
        else:
            if temp == (d//2):
                left = i
                right = i+1
                return (left+right) / 2
            if temp > (d//2):
                return i
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
