"""
The factorial of the integer n, written n!, is defined as:

    n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1

Calculate and print the factorial of a given integer.

For example, if n = 30, we calculate 30 * 29 * 28 * ... * 2 * 1 and get 
265252859812191058636308480000000.

Function Description

Complete the extraLongFactorials function in the editor below. It should print the result and 
return.

extraLongFactorials has the following parameter(s):

    n: an integer

Note: Factorials of n > 20 can't be stored even in a 64 - bit long long variable. Big integers 
must be used for such calculations. Languages like Java, Python, Ruby etc. can handle big 
integers, but we need to write additional code in C/C++ to handle huge values.

We recommend solving this challenge using BigIntegers.

Input Format

Input consists of a single integer n

Constraints

1 <= n <= 100

Output Format

Print the factorial of n.

Sample Input

25

Sample Output

15511210043330985984000000

Explanation

25! = 25 * 24 * 23 * ... * 3 * 2 * 1
"""

import time

def extraLongFactorials(n):
    """
    Function that implements recursivity to 
    calculate the factorial of n
    """
    if n == 1:
        return n
    else:
        return n*extraLongFactorials(n-1)

def extraLongFactorials2(n):
    """
    Function that implements the for structure 
    of repeat to calculate the factorial of n
    """
    if n == 1:
        return n
    n_factorial = 1
    for i in range(2, n+1):
        n_factorial = n_factorial*i
    
    return n_factorial

if __name__ == '__main__':
    """
    Main function, where it calls the functions to
    calculate the factorial of a number introduced by
    standard input.

    It use time method of time library to get the 
    duration of each function called.
    """
    n = int(input())

    start = time.time()
    result = extraLongFactorials(n)
    end = time.time()
    print("Result1 - Time1: ", result, end-start)
    start = time.time()
    result = extraLongFactorials2(n)
    end = time.time()
    print("Result2 - Time2: ", result, end-start)
