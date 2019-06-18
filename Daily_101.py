# Implementation of the sieve of erastotenes required to solve the problem.
def get_primes(n):
    solution = [True] * (n + 1)
    solution[0] = solution[1] = False

    x = 2
    while x <= int(n**0.5):
        for z in range(x * x, n + 1, x):
            solution[z] = False

        x += 1
        while not solution[x]:
            x += 1

    primes = []
    for pos, x in enumerate(solution):
        if x:
            primes.append(pos)
    return primes


# Cost O(n) if we convert the sequence of primes into a set otherwise 0(n^2)
# being n the number of primes to consider.
# The solution is formed by two primes, iterate over the primes and check if the
# subtraction of the value we got minus the current prime is also a prime if that
# is the case we got a solution. If the sequence of primes is sorted we warranty
# that the first solution we obtain is also the smallest lexicographically.
def p_101(primes, v):
    p = set(primes)

    for x in primes:
        if v - x in p:
            return x, v - x

    return None


primes = get_primes(100)
print(p_101(primes, 4))
print(p_101(primes, 8))
print(p_101(primes, 24))
