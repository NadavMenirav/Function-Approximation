import numpy as np

def f(x):
    # Input: a real number x
    # Output: the value of f(x)
    return 1 / (1 + x ** 2)


def main():
    # This function generates a polynomial of a degree n that will be an approximation of
    # the function f(x) = 1/(x^2+1)

    N = 5 # The degree of the polynomial
    x = [] # Array of the x values
    y = [] # Array of the y values

    for k in range(N):
        x.append(2 * k - 1)
        y.append(f(x[k]))


if __name__ == '__main__':
    main()