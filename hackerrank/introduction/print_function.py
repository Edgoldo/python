"""
Print a sequence of n numbers in a row.
The input is the n value.
The output is the row of n numbers.
"""
from __future__ import print_function
if __name__ == '__main__':
    # Number input
    n = int(raw_input())
    # Result variable
    r = 0
    # Power selection
    p = 1
    # Basic value for power selection
    b = 1
    # Repeat in the values range to print
    for val in range(1, n+1):
    	# Power increment in each scale of numbers
    	if b*10**p <= val:
    		p += 1
    	# Stores the sequence of values
        r = r*10**p + val
    print (r)