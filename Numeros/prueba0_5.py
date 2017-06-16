"""!
Imprime la segunda pontencia de i, donde 0 <= i < n
y 1 <= n <= 20
"""
if __name__ == '__main__':
    # Number input
    n = int(raw_input())
    # Verifying constraints
    if (n >= 1 and n <= 20):
        for i in range(0, n):
            # Print i to the power 2
            print(i**2)