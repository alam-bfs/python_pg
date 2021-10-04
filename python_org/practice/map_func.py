"""
    map function in python returns iterator over a list.
    map takes two arguments, first argument takes function and the second one take list, tuple or other iterable object

    Structure of Map:

    Data = A1, A2, A3, ..., An

    Function: f

    map(f, Data)
        return iterator over
        f(A1), f(A2), f(A3), ..., F(An)

"""
import math
from random import random

radii = [2, 5, 7.1, 0.3, 10]


def area(r):
    return math.pi * (r ** 2)


if __name__ == '__main__':
    # print(list(map(area, radii)))
    temps = [("Berlin", 20), ("Cairo", 36), ("Los Angeles", 26)]
    f = lambda data: (data[0], (9 / 5) * data[1] + 32)
    print(list(map(f, temps)))

    l = [[2], [3], [4]]

    d = lambda p: (p[1] ** 2)
    print(d(temps[0]))
    print(list(map(d, temps)))

    dd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    # d1 = lambda p: "Fizz" if p % 3 == 0 else "Buzz"
    print(list(map(lambda p: "Fizz" if p % 3 == 0 else "Buzz", [1, 2, 3, 5])))

    print(list(map(lambda p: random() if p % 3 == 0 else "Buzz", [1, 2, 3, 5])))

    n = lambda: "hello world"
    print(n())

    # factorial function in python
    y = lambda q: 1 if q == 1 else q * y(q-1)
    print(y(5))
