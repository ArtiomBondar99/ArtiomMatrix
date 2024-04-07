import math
import numpy as np
from colors import bcolors

"""
Receives 3 parameters:
    1.  a - start value.
    2.  b - end  value. 
    3.  err - value of tolerable error

Returns variables:
    1.  S - The minimum number of iterations required to reach the desired accuracy
"""


def max_steps(a, b, err):
    s = int(np.floor(- np.log2(err / (b - a)) / np.log2(2) - 1))
    return s


"""
Performs Iterative methods for Nonlinear Systems of Equations to determine the roots of the given function f
Receives 4 parameters:
    1. f - continuous function on the interval [a, b], where f (a) and f (b) have opposite signs.
    2. a - start value.
    3. b - end  value. 
    4. tol - the tolerable error , the default value will set as 1e-16

Returns variables:
    1.  c - The approximate root of the function f
"""


def bisection_method(f, a, b, tol=1e-6):
    c, k = 0, 0
    steps = max_steps(a, b, tol)  # calculate the max steps possible

    print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Iteration", "a", "b", "f(a)", "f(b)", "c", "f(c)"))

    # while the diff af a&b is not smaller than tol, and k is not greater than the max possible steps
    while abs(b - a) > tol and k <= steps:
        c = (a + b) / 2  # Calculation of the middle value

        if c == 0:
            return 0
        if f(c) == 0:
            return c  # Procedure completed successfully

        if f(c) * f(a) < 0:  # if sign changed between steps
            b = c  # move forward
        else:
            a = c  # move backward

        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f}".format(k, a, b, f(a), f(b), c, f(c)))
        k += 1

    return c  # return the current root


def find_all_roots(f, a, b, tol=1e-6):
    roots = []
    x = np.linspace(a, b, 1000)  # Divide the interval into smaller sub-intervals

    for i in range(len(x) - 1):
        if np.sign(f(x[i])) != np.sign(f(x[i + 1])):
            root = np.round(bisection_method(f, x[i], x[i + 1], tol), 7)
            if (not any(abs(x - root) < 0.000001 for x in roots)) and (0 == np.round(f(root), 2)):
                roots.append(root)

    return roots

# Date: 18.3.24
# Group members:
# Segev Chen 322433400
# Gad Gadi Hasson 207898123
# Carmel Dor 316015882
# Artiom Bondar 332692730
# Git:https://github.com/IMrMoon/SegevAnaliza.git
# Name: Segev Chen
if __name__ == '__main__':
    f = lambda x: (x**5 -6*x**2 -1) / (7*x**3 + 1)

    # Adjust the interval to avoid the singularity
    a = -2
    b = 2

    roots = find_all_roots(f, a, b)
    print(bcolors.OKBLUE, f"\nThe equation f(x) has approximate roots at {roots}", bcolors.ENDC)
