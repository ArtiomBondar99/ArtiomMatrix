import numpy as np

from colors import bcolors



def trapezoidal_rule(f, a, b, n):
    if a > b:
        a, b = b, a
    h = (b - a) / n
    T = f(a) + f(b)
    integral = ((b-a) * T) / 2  # Initialize with endpoints

    for i in range(1, n):
        x_i = a + i * h
        integral += f(x_i)

    integral *= h

    return abs(integral)


if __name__ == '__main__':
    f = lambda x: (3*x**2 + np.sin(x**4 + 5*x - 6)) / (2*np.exp(-2*x+5))
    result = trapezoidal_rule(f, 2.7, 4.1, 10)
    print(bcolors.OKBLUE, "Approximate integral:", result, bcolors.ENDC)
