def print_pascals_triangle(n, memo={}):
    if n == 0:
        return

    for i in range(1, n+1):
        for j in range(0, n-i+1):
            print(' ', end='')

        # Check if the value is already memoized
        if (n, i) in memo:
            C = memo[(n, i)]
        else:
            # Calculate the value using Binomial Coefficient
            C = 1
            for j in range(1, i+1):
                print(' ', C, sep='', end='')
                C = C * (i - j) // j
            memo[(n, i)] = C

        print()

# Test the function
n = 8
print_pascals_triangle(n)
