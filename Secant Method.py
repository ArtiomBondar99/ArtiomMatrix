# The creators are:
# Carmel Dor - 316015882
# Segev Chen - 322433400
# Gad Hasson - 207898123
# Artiom Bondar - 332692730
# github link - https://github.com/Carlechinno/Homework3-NumericalAnalysis3

from colors import bcolors


# Implementing Secant Method

def secant(x0, x1, e, N, f):
    print("\n\nSECANT METHOD IMPLEMENTATION")
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):  # Check if we divide by zero
            print(bcolors.FAIL, "Error f(x0) is equal to f(x1) which causes us to divide by ZERO")
            break

        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))  # The Secant Pattern
        print("Iteration-%d, x2 = %0.6f and f(x2) = %0.6f" % (step, x2, f(x2)))
        x0 = x1
        x1 = x2
        step = step + 1

        if step > N:  # Maybe needs to be changed? should consult with the others
            print("Not Convergent!")
            break

        condition = abs(f(x2)) > e
    print(bcolors.OKGREEN, "\nThe root is: %0.10f" % x2)


if __name__ == '__main__':
    f = lambda x: x**2 - 5*x + 2
    x0 = 80
    x1 = 100
    TOL = 1e-6
    N = 20

    secant(x0, x1, TOL, N, f)