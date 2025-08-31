import numpy as np

def f(x):
    # Input: a real number x
    # Output: the value of f(x)
    return 1 / (1 + x ** 2)


def main():
    # This function generates a polynomial of a degree n that will be an approximation of
    # the function f(x) = 1/(x^2+1)

    N = 15 # The degree of the polynomial

    k = np.arange(0, N + 1)
    x = 2 * k / N - 1 # Array of x values
    y = f(x) # Array of y values

    V = np.vander(x, increasing = True) # The vandermonde matrix

    a = np.linalg.solve(V, y) # Solving for the coefficients
    print(a)

if __name__ == '__main__':
    main()