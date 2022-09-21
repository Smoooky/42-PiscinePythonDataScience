#!/usr/bin/env python3

import timeit
from sys import argv
from functools import reduce


def loop_approach(final: int) -> int:
    i = 0
    res = 0
    while i <= final:
        res += i * i
        i += 1
    return res


def reduce_approach(final: int) -> int:
    def add_square(x, y):
        return x + y * y
    return reduce(add_square, range(1, final + 1))


def main(test: str, iterations: str, number: str):
    res = {
        'loop': loop_approach,
        'reduce': reduce_approach,
    }

    try:
        iterations = int(iterations)
        number = int(number)
    except ValueError:
        print("Number of iterations and number must be integer")
        return

    if test not in res.keys():
        print("Invalid test name")
        return

    print(timeit.timeit(lambda: res[test](number), number=iterations))


if __name__ == '__main__':
    if len(argv) == 4:
        main(argv[1], argv[2], argv[3])
