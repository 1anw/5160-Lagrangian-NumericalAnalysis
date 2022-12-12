# IRF_Test.py
#   Improved Regula Falsi method by Soumen Shaw and Basudeb Mukhopadhyay Test Cases
# By: Andy Shapiro

import math
import matplotlib.pyplot as plt
from tabulate import tabulate


# manually rename function from f#(x) to f(x) in order to test it, change bounds manually to fit function case in main()
def f1(x):
    # set a= -1, and b= 1 in main()
    return x * math.exp(x) - 1


def f2(x):
    # set a= 0.1, and b= 0.9 in main()
    return 11 * (x ** 11) - 1


def f3(x):
    # set a= 2.8, and b= 3.1 in main()
    return math.exp(x ** 2 + 7 * x - 30) - 1


def f4(x):
    # set a= -1.3, and b= -0.5 in main()
    return (1 / x) - math.sin(x) + 1


def f5(x):
    # set a= 2, and b= 3 in main()
    return x ** 3 - 2 * x - 5


def f6(x):
    # set a= 0.5, and b= 1.5 in main()
    return (1 / x) - 1


def f7(x):
    # set a= 0.5, and b= 1.5 in main()
    return math.log(x)


def main():
    tolerance = 1E-10

    a = 0.5
    b = 1.5

    f_a = f(a)
    f_b = f(b)

    count = 0
    x = a
    error = abs(f_a)

    data = []

    while error > tolerance:
        c = (a * f_b - b * f_a) / (f_b - f_a)
        f_c = f(c)

        if f_a * f_c < 0:
            # Uncomment BOTH if/else cases for desired k value
            k = (abs(f_c) % abs(f_b)) / (abs(f_b))
            # k = 0
            # k = 0.5

            x = ((k - 1) * b * f_a + a * f_b) / ((k - 1) * f_a + f_b)
            f_x = f(x)

            if f_a * f_x < 0:
                b = x
                f_b = f_x
            else:
                a = x
                f_a = f_x

                b = c
                f_b = f_c
        else:
            # Uncomment BOTH if/else cases for desired k value
            k = (abs(f_c) % abs(f_a)) / (abs(f_a))
            # k = 0
            # k = 0.5

            x = ((k - 1) * a * f_b + b * f_a) / ((k - 1) * f_b + f_a)
            f_x = f(x)

            if f_a * f_x < 0:
                a = c
                f_a = f_c

                b = x
                f_b = f_x
            else:
                a = x
                f_a = f_x

        count = count + 1
        error = abs(f_x)
        data.append([count, x, error])

    col_names = ["i", "x^(i)", "|error|"]
    print(tabulate(data, headers=col_names))
    print(x)


main()
