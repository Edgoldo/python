from __future__ import print_function
if __name__ == '__main__':
    # Number input
    n = int(raw_input())
    # Result variable
    r = 0
    """r = n/10
                mult = 0
                while r > 1:
                	mult += 1
                	r = r/10"""
    # Power selection
    p = 1
    # Counter
    count = 1
    # Repeat in the values range to print
    for val in range(1, n+1):
    	# Power increment in each scale of numbers
    	if count*10**p <= val:
    		p += 1
    	# Stores the sequence of values
        r = r*10**p + val
    print (r)


    1
    2
    3
    4
    5
    6
    7
    8
    9
    10