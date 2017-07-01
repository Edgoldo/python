"""
Calculates and print the hash function on a tuple of integers.
The input is the number of integers and the integers separates by a blank space
"""
if __name__ == '__main__':
	# Number of integers
    n = int(raw_input())
    # Integers numbers separeted by blank space converted in a tuple
    integer_tuple = tuple(map(int, raw_input().split()))
    print(hash(integer_tuple))