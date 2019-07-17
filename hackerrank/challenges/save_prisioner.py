#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    """
    Find the chair to warn. That is, the prisoner number to give the last sweet
    
    Next comments is for analysis of exercise

    Cases           N1      N2      N3      N4
    n: prisoners   100     100     4       1
    m: sweets       20      20      13      1
    s: chair        80      90      3       1

    # Reach to deliver one sweet maximum to each prisoner
    if m <= n:
        # When give from selected chair, all sweets are delivered with out pass to chair number 1
        # if s <= (m - 1):
        # warn_chair = s + (m - 1)
        # if s > (m - 1):
        #     warn_chair = n - warn_chair
        if s + (m - 1) <= n:
            warn_chair = s + (m - 1)
        if s + (m - 1) > n:
            warn_chair = s + (m - 1)
            warn_chair = n - warn_chair
    else:
        # Get decimal part of division of m and n, then multiplies n
        rest_sweets = int(modf(m/n)[0]*n)
        m = rest_sweets

    # In conclusion, the result is:
    if n < m:
        # Get decimal part of division of m and n, then multiplies n
        rest_sweets = int(modf(m/n)[0]*n)
        m = rest_sweets
    if s + (m - 1) <= n:
        warn_chair = s + (m - 1)
    elif s + (m - 1) > n:
        warn_chair = s + (m - 1)
        warn_chair = n - warn_chair
    """

    if n < m:
        # Get decimal part of division of m and n, then multiplies n
        # print("More sweets")
        # rest_sweets = math.modf(m/n)[0]*n
        rest_sweets = math.modf(m/n)[1]*n
        # print("rest_sweets 1:", rest_sweets)
        # if math.modf(rest_sweets)[0] >= 0.5:
        #     rest_sweets = rest_sweets + 1
        rest_sweets = int(m - rest_sweets)
        # rest_sweets = int(rest_sweets)
        m = rest_sweets
        # print("rest_sweets 2:", m)
    if s + (m - 1) <= n:
        # print("Deliver...")
        warn_chair = s + (m - 1)
    elif s + (m - 1) > n:
        # print("Calculating...")
        warn_chair = s + (m - 1)
        warn_chair = warn_chair - n

    # Solving like other user
    rest_sweets = s + (m - 1)
    if rest_sweets > n:
        if rest_sweets%n == 0:
            rest_sweets = n
        rest_sweets = rest_sweets%n
    rest_sweets = rest_sweets

    if warn_chair != rest_sweets:
        print(n, m, s)
        print(warn_chair, rest_sweets, warn_chair == rest_sweets)

    return warn_chair == rest_sweets

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)
        
        print(str(result) + '\n')
    """
    i = 0
    result = True
    while (result and i<1e6):
        n = random.randint(1, 1e10)
        m = random.randint(1, 1e10)
        s = random.randint(1, n)
        result = saveThePrisoner(n, m, s)
        i = i + 1
    """
        # fptr.write(str(result) + '\n')

    # fptr.close()
