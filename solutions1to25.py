import functools
import math
import operator

__author__ = 'Skurmedel'

import problem as pm
import itertools

def sieve(n):
    candidates = list(range(2, n))

    c = 2
    end = False
    while not end:
        for i in range(2, n):
            m = c * i
            if m >= n:
                break
            candidates[m - 2] = -1

        f = False
        for next in candidates[c - 1:]:
            if next == -1:
                continue
            f = True
            c = next
            break

        end = not f

    return filter(lambda x: x != -1, candidates)




@pm.problem(1, "Multiples of 3 and 5")
def problem1():
    multiples = []
    for i in range(1, 1000):
        mod1, mod2 = i % 3, i % 5
        if mod1 == 0 or mod2 == 0:
            multiples.append(i)

    return sum(multiples)


@pm.problem(2, "Even Fibonacci numbers")
def problem2():
    fibs = [1, 2]

    p, c = fibs
    while c <= 4e6:
        p, c = c, p + c
        fibs.append(c)

    def even(x): return x % 2 == 0

    return sum(filter(even, fibs))


@pm.problem(3, "Largest prime factor")
def problem3():
    n = 600851475143

    upper = int(math.sqrt(n))

    factors = list(filter(lambda x: n % x == 0, sieve(upper)))

    return factors[-1]

if __name__ == "__main__":
    pm.run_problems()