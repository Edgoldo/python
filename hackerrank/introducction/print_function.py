from __future__ import print_function
if __name__ == '__main__':
    # Input number
    n = int(raw_input())
    # Result variable
    r = 0
    for val in range(1, n+1):
        r = r*10 + val
    print(r)