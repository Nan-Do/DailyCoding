from random import randint


# Cost O(n), memory O(n)
# First version of the function.
# Basic idea:
# Compute the array of the valid numbers, that is v = set(range(n)).difference(r)
# Then generate a valid number x between 0 and n - r and return v[r]
def P90_v1(n, r):
    v = []

    for x in range(n):
        if x in r:
            continue
        v.append(x)

    return v[randint(0, n - len(r) - 1)]


# Cost 0(n), memory 0(1)
# We can improve the previous solution given that r is a sorted list.
# We have to find the first value on r in which the difference between
# the value and its index is greater than v (being v the random value
# (n - k) generated), when this condition is met we know the final value
# we are looking for is between r[j] and r[j+1]. We know this because the
# difference between the index value and the real value indicates how many
# values are in the array of valid choices. To compute the number we use the next
# formula r[j] + v - (r[j] - j):
#  r[j] is the base number (the number we are looking is between r[j] and r[j+1])
#  v this is the position on the final array
#  r[j] - j this is how many positions have already been occupied on the final array
def P90_v2(n, r):
    v = randint(0, n - len(r) - 1)

    if v == 0:
        if r[0] != 0:
            return 0

    for j in range(0, len(r)):
        if r[j] - j > v:
            if j != 0:
                j -= 1
            break

    x = r[j] + 1 + v - (r[j] - j)
    return x


# Finally we can achieve a log(n) solution by turning the linear search into a binary search, (the corner cases are quite tricky in this problem)
def P90_v3(n, r):
    lo = 0
    hi = len(r) - 1
    v = randint(0, n - len(r) - 1)

    j = len(r) - 1
    if v == 0:
        if r[0] != 0:
            return 0
        if r[-1] - (len(r) - 1) > 0:
            j = 0

    while lo < hi:
        mid = int((lo + hi) / 2)
        s1 = r[mid] - mid
        s2 = r[mid + 1] - (mid + 1)
        if (v - s1) >= 0 and (v - s2) < 0:
            j = mid
            break

        if s1 - v > 0:
            lo = mid + 1
        else:
            hi = mid - 1

    x = r[j] + 1 + v - (r[j] - j)
    return x


n = 7
# # r = set([0, 1, 5])
r = [0, 3, 6]
res = [0] * n
for _ in range(100):
    res[P90_v3(n, r)] += 1
print(res)
