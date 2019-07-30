#!/bin/python3

import math
import os
import random
import re
import sys
import time

# Complete the squares function below.
def squares(a, b):
    """
    Get the number of integers which square is in range of
    a to b, including that limits

    @date 28/07/2019
    @param <b>{int}</b> a Minimal value of the range
    @param <b>{int}</b> b Maximal value of the range
    @return <b>{int}</b> Number of integers

    Constraints:
    1 <= a <= b <= 10e9
    """
    sqrt_integers = 0
    value_sqrt = round(math.sqrt(a))
    value_power = value_sqrt**2
    while value_power <= b:
        if a <= value_power:
            sqrt_integers += 1
        value_sqrt += 1
        value_power = value_sqrt**2
    return sqrt_integers

def squares2(a, b):
    """
    Same functionality of square but is not optimized
    """
    sqrt_integers = []
    for num in range(a, b+1):
        sqrt_num = math.sqrt(num)
        if math.modf(sqrt_num)[0] == 0:
            sqrt_integers.append(num)
    
    return len(sqrt_integers)

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        start = time.time()
        result = squares(a, b)
        end = time.time()
        time0 = end-start
        print(str(result) + ' in time: ' + str(end-start) + '\n')

        start = time.time()
        result = squares2(a, b)
        end = time.time()
        time1 = end-start
        print(str(result) + ' in time: ' + str(end-start) + '\n')
        print("Is better time the square function: ", time0 <= time1)
