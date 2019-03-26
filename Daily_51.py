import random
from collections import defaultdict

def swap(seq, x, y):
    temp = seq[x]
    seq[x] = seq[y]
    seq[y] = temp


def permutate(seq):
    k = len(seq) - 1

    for x in xrange(len(seq)-1, -1, -1):
        new_pos = random.randint(0, x)
        swap(seq, x, new_pos)


d = defaultdict(int)

for _ in xrange(15000):
    a = ['a','b','c','d']
    permutate(a)
    d[tuple(a)] += 1

print d
