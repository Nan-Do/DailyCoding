# To obtain the probabilities if they are not given we can simulate 100000 (or a high number) of
# coin tosses by the law of big numbers the real probabilities will arise

from random import random


def unfair_coin(p=0.5):
    def _():
        x = random()
        if x < p:
            return 'H'
        else:
            return 'T'

    return _


def simulate_fair_with_unfair(f):
    c1 = c2 = 'H'

    while c1 == c2:
        c1 = f()
        c2 = f()

    return c1


p = 0.99
unfair_coin = unfair_coin(p)
d = {'H': 0, 'T': 0}
for _ in range(10000):
    d[simulate_fair_with_unfair(unfair_coin)] += 1
print(d)
