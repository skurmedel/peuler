__author__ = 'Skurmedel'

import problem as pm

@pm.problem(1, "Multiples of 3 and 5")
def problem1():
    multiples = []
    for i in range(1, 1000):
        mod1, mod2 = i % 3, i % 5
        if mod1 == 0 or mod2 == 0:
            multiples.append(i)

    return sum(multiples)

if __name__ == "__main__":
    pm.run_problems()