def three_max(s):
    max_1 = max_2 = max_3 = float('-inf')
    min_1 = min_2 = float('inf')

    for x in range(0, len(s)):
        if s[x] > max_1:
            max_3 = max_2
            max_2 = max_1
            max_1 = s[x]
        elif s[x] > max_2:
            max_3 = max_2
            max_2 = s[x]
        elif s[x] > max_3:
            max_3 = s[x]

        if s[x] < min_1:
            min_2 = min_1
            min_1 = s[x]
        elif s[x] < min_2:
            min_2 = s[x]

    return max(min_1 * min_2 * max_1, max_1 * max_2 * max_3)


def _three_max(s):
    s = sorted(s)
    return max(s[0] * s[1] * s[-1], s[-3] * s[-2] * s[-1])


print(three_max([-3, -3, -1, -3, -3]))
print(three_max([-10, -10, 5, -2]))
print(three_max([-10, -10, -5, 2]))
print(three_max([-10, 10, 5, 2]))
