__author__ = 'Simon Otter'

problems = []

class EulerProblem:
    def __init__(self, n, name, runner):
        if not callable(runner):
            raise TypeError("the runner is not callable.")
        self._n = n
        self._name = name
        self._runner = runner

    @property
    def number(self):
        return self._n

    @property
    def name(self):
        return self._name

    def __call__(self, *args, **kwargs):
        return self._runner()

class problem:
    def __init__(self, n, name, suite=problems):
        self._args = (n, name)
        self._suite = suite

    def __call__(self, f):
        n, name = self._args
        p = EulerProblem(n, name, f)
        self._suite.append(p)
        return p

def run_problems(suite=problems):
    div = "-" * 75
    for p in suite:
        print("{0:03}. {1}.".format(p.number, p.name))
        res = p()
        print("Result: {0}".format(res))
        print(div)


