from __future__ import print_function
if __name__ == '__main__':
    # Number input
    n = int(raw_input())
    r = 0
    for val in range(1, n+1):
        r = 100*r + val
    print (r)